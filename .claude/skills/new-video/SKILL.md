---
name: new-video
description: Step 0 of MV Studio. Starts a new music-video project for one song - creates the song folder in songs/ and writes song.md with the lyrics, timing and channel profile. Use when the user types /new-video or asks to start a video for a new song.
argument-hint: [song title]
disable-model-invocation: true
---

# /new-video: start a song project

1. **Gather.** Ask in one message for anything not already given:
   - Song title (the argument, if one was passed).
   - Full lyrics with section headers like `[Verse 1]`, `[Chorus]`, `[Bridge]`.
   - BPM and total length (m:ss). Section start times are optional and can be added later.
   - Channel. Default `dark-nord`. List folders in `channels/` if unsure.
2. **Load the profile.** Read `channels/<channel>/profile.md`. If it is missing, stop
   and say so. Check `docs/song-projects.md` for notes on this song and quote any match.
3. **Name the folder.** `songs/<YYYY-MM>-<slug>/`: today's year and month, slug from
   the title in lowercase words joined by hyphens, no punctuation.
   If the folder exists, stop and ask. Never overwrite.
4. **Write `song.md`** from `song-template.md` beside this file. Paste the lyrics
   exactly as given. Leave unknown fields as `TBD`.
5. **Report.** Show the folder path, a summary of the fields, any `TBD` values,
   and the next step: `/song-read`.

Do not analyse the song or suggest concepts here. That is step 1 and 2.
