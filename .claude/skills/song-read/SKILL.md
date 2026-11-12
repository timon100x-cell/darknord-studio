---
name: song-read
description: Step 1 of MV Studio. Reads one song's lyrics and finds the narrator, want, conflict, turn and title line, marks what the lyric leaves unsaid, maps each section's energy and cut points, and builds the bar grid. Writes analysis.md and timing.json. Use when the user types /song-read.
argument-hint: [song folder, e.g. 2026-11-king-of-nothing]
disable-model-invocation: true
---

# /song-read: read the song

1. **Find the song.** Use the folder passed as the argument. With none, list folders in
   `songs/` that have `song.md` but no `analysis.md`. One match: use it. Several: ask.
   If `song.md` is missing, stop: run `/new-video` first.
2. **Never overwrite.** If `analysis.md` or `timing.json` already exists, stop and ask.
3. **Load.** Read `song.md`, `channels/<channel>/profile.md` (the channel is in
   `song.md`) and `.claude/skills/concepts/story-craft.md`. Check
   `docs/song-projects.md` for notes on this song.
4. **Build the bar grid.** Run `python scripts/timing.py songs/<folder>`. Do not do bar
   arithmetic by hand. Copy the missing fields and warnings it prints into the report.
   Missing times are fine at this step; `/shots` (step 4) needs them.
5. **Read the lyric.** Fill `analysis-template.md` beside this file and save it as
   `songs/<folder>/analysis.md`. Rules:
   - Quote lyric lines exactly. Every claim points to a line or a section.
   - Read the performance notes in the section headers (`[Verse 2 | double time ...]`)
     and the Suno style prompt as evidence of energy, silence and drops.
   - Separate what the lyric **says** from what it **leaves unsaid**. The gaps are the
     raw material for `/concepts`; list them as open questions, not answers.
   - Treat joik and instrumental passages as texture, not story (profile rule).
   - Flag anything that pulls toward redemption, or any "not mythology-forward" note.
6. **Report.** Show a short summary: narrator, want, conflict, turn, title line, the
   three strongest gaps, the bar length and what timing is still missing.
   Next step: `/concepts`.

Do not suggest concepts, worlds, shots or prompts here. That is step 2 onward.
