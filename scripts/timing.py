"""Turn a song's BPM, length and section start times into a bar grid.

Reads  songs/<folder>/song.md
Writes songs/<folder>/timing.json

Run from the project folder:
    python scripts/timing.py songs/2026-11-king-of-nothing
Add --overwrite to replace an existing timing.json.
Add --out <path> to write somewhere else (used for testing).

Uses only Python's standard library. Nothing to install.
"""

import argparse
import json
import re
import sys
from pathlib import Path


def parse_time(text):
    """'1:23' or '1:23.5' -> seconds as float. 'TBD' or blank -> None."""
    text = text.strip()
    m = re.fullmatch(r"(\d+):(\d{1,2}(?:\.\d+)?)", text)
    if not m:
        return None
    return int(m.group(1)) * 60 + float(m.group(2))


def fmt_time(seconds):
    if seconds is None:
        return None
    minutes = int(seconds // 60)
    rest = seconds - minutes * 60
    return f"{minutes}:{rest:05.2f}"


def field(text, name):
    m = re.search(rf"^- \*\*{re.escape(name)}:\*\*\s*(.+)$", text, re.MULTILINE)
    return m.group(1).strip() if m else None


def read_song(path):
    text = path.read_text(encoding="utf-8-sig")
    title = text.splitlines()[0].lstrip("# ").strip() if text else path.parent.name

    bpm_raw = field(text, "BPM") or "TBD"
    bpm = float(bpm_raw) if re.fullmatch(r"\d+(\.\d+)?", bpm_raw) else None

    sig_raw = field(text, "Time signature") or "4/4"
    sig = re.fullmatch(r"(\d+)\s*/\s*(\d+)", sig_raw)
    beats_per_bar = int(sig.group(1)) if sig else 4

    length = parse_time(field(text, "Length") or "TBD")

    sections = []
    timing_block = re.search(r"## Section timing\s*\n(.*?)(\n## |\Z)", text, re.DOTALL)
    if timing_block:
        for line in timing_block.group(1).splitlines():
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 2 or not cells[0].startswith("["):
                continue
            name = cells[0].strip("[]").strip()
            sections.append({"name": name, "start": parse_time(cells[1])})

    return title, bpm, sig_raw, beats_per_bar, length, sections


def build_grid(title, bpm, sig_raw, beats_per_bar, length, sections):
    missing = []
    warnings = []
    if bpm is None:
        missing.append("BPM")
    if length is None:
        missing.append("total length")
    unknown = [s["name"] for s in sections if s["start"] is None]
    if unknown:
        missing.append("start times for: " + ", ".join(unknown))

    bar_seconds = beats_per_bar * 60 / bpm if bpm else None
    total_bars = round(length / bar_seconds, 2) if (bar_seconds and length) else None

    # Check that known start times run in order.
    known = [s for s in sections if s["start"] is not None]
    for a, b in zip(known, known[1:]):
        if b["start"] <= a["start"]:
            warnings.append(f"'{b['name']}' starts before or at '{a['name']}'. Check the times.")

    out_sections = []
    for i, s in enumerate(sections):
        start = s["start"]
        # The section ends where the next section with a known time starts, or at the song end.
        end = None
        if start is not None:
            for nxt in sections[i + 1:]:
                if nxt["start"] is not None:
                    end = nxt["start"]
                    break
            else:
                end = length
            # If the very next section has no time, this section's end is unknown.
            if i + 1 < len(sections) and sections[i + 1]["start"] is None:
                end = None

        entry = {
            "index": i + 1,
            "name": s["name"],
            "start": fmt_time(start),
            "start_seconds": round(start, 3) if start is not None else None,
            "end_seconds": round(end, 3) if end is not None else None,
            "start_bar": None,
            "bars": None,
        }
        if bar_seconds and start is not None:
            entry["start_bar"] = round(start / bar_seconds, 2) + 1
            if end is not None:
                bars = (end - start) / bar_seconds
                entry["bars"] = round(bars, 2)
                if abs(bars - round(bars)) > 0.25:
                    warnings.append(
                        f"'{s['name']}' is {bars:.2f} bars long, not close to a whole bar. "
                        "The start time or BPM may be off."
                    )
        out_sections.append(entry)

    return {
        "song": title,
        "bpm": bpm,
        "time_signature": sig_raw,
        "beats_per_bar": beats_per_bar,
        "bar_seconds": round(bar_seconds, 4) if bar_seconds else None,
        "length": fmt_time(length),
        "length_seconds": length,
        "total_bars": total_bars,
        "complete": not missing,
        "missing": missing,
        "warnings": warnings,
        "sections": out_sections,
    }


def main():
    parser = argparse.ArgumentParser(description="Build the bar grid for one song.")
    parser.add_argument("folder", help="the song folder, e.g. songs/2026-11-king-of-nothing")
    parser.add_argument("--overwrite", action="store_true", help="replace an existing timing.json")
    parser.add_argument("--out", help="write to this path instead of <folder>/timing.json")
    args = parser.parse_args()

    folder = Path(args.folder)
    song = folder / "song.md"
    if not song.exists():
        sys.exit(f"Stopped: {song} does not exist. Run /new-video first.")

    out = Path(args.out) if args.out else folder / "timing.json"
    if out.exists() and not args.overwrite:
        sys.exit(f"Stopped: {out} already exists. Add --overwrite to replace it.")

    grid = build_grid(*read_song(song))
    out.write_text(json.dumps(grid, indent=2) + "\n", encoding="utf-8")

    print(f"Wrote {out}")
    if grid["bar_seconds"]:
        print(f"One bar = {grid['bar_seconds']:.3f} s at {grid['bpm']:g} BPM ({grid['time_signature']})")
    if grid["total_bars"]:
        print(f"Song length {grid['length']} = {grid['total_bars']} bars")
    for m in grid["missing"]:
        print(f"Missing: {m}")
    for w in grid["warnings"]:
        print(f"Warning: {w}")


if __name__ == "__main__":
    main()
