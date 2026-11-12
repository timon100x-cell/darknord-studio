# MV Studio

Turns the lyrics of a Dark Nord song into a music-video story, a shot list and
Grok Imagine prompts. The spec is `docs/research.md`. The user is not a programmer:
explain choices in plain language and ask before installing anything.

## Pipeline (run in order, one song at a time)

| Step | Command      | Writes                      | Approval |
|------|--------------|-----------------------------|----------|
| 0    | `/new-video` | `song.md`                   |          |
| 1    | `/song-read` | `analysis.md`, `timing.json`|          |
| 2    | `/concepts`  | `treatment.md`              | user picks or mixes 1 of 3 |
| 3    | `/beats`     | `beats.md`                  | user approves |
| 4    | `/shots`     | `shots.json`                | user approves |
| 5    | `/prompts`   | `prompts.md`                |          |
| 6    | `/check`     | `review.md`                 | a failed rule goes back to step 4 |
| 7    | `/board`     | `storyboard.html`           |          |

Built so far: Phase 1 (step 0 only). See the build plan in `docs/research.md`.

## Rules

- **Never skip an approval step.** Present the options, then stop and wait.
- Never start a step until the file from the step before it exists.
- Every step reads and writes plain files in `songs/<YYYY-MM>-<slug>/`. No database.
- Never overwrite an existing song folder or an approved file without asking.
- Read `channels/<channel>/profile.md` before any story or prompt work. Channel rules win.
- Paste the character block from the profile word for word. Never paraphrase it.
- Grok rules live only in `prompts/grok-image.md` and `prompts/grok-video.md`.
- In this project, do not use the claude.ai skill `dark-nord-image-prompt` if an old
  copy is still active (Midjourney flags, old character text). Use the profile instead.
- Scripts are Python and use no paid services. Tell the user how to run each one.

## Folder layout

```
CLAUDE.md
docs/research.md                 spec and research report
docs/dark-nord-*.md              original claude.ai skills (reference only)
docs/song-projects.md            Dark Nord song list
.claude/skills/
  new-video/                     SKILL.md, song-template.md
  concepts/                      story-craft.md, genre-playbooks.md
  beats/                         retention.md
  shots/                         shot-grammar.md
  prompts/                       grok-image.md, grok-video.md
.claude/agents/                  critic.md (Phase 4)
channels/dark-nord/profile.md    character, look, story rules, lessons
scripts/                         timing.py, validate.py, board.py (Phases 3-4)
songs/<YYYY-MM>-<slug>/          one folder per song, one file per step
```

Slugs are lowercase words joined by hyphens: `2026-11-blood-on-the-trail`.
