# Grok Imagine: Image to Video

Last checked: 2026-11-12 (source: docs/research.md; xAI docs as updated October 2026)
Re-check monthly against https://docs.x.ai/developers/model-capabilities/video/overview

## Model facts

| Area | Current state | What it means |
|---|---|---|
| Clips | Imagine Video 1.5: 1 to 15 s, native 1080p, from text or an image | One shot per clip; generate longer than you need |
| Budget | Video 1.5 Lite: text/image to video only, lowest price | Drafts and background plates |
| References | Up to 14 reference images, tagged `<IMAGE_0>` onward, 720p ceiling | A recurring character without fixing the first frame |
| Pinned frames | First frame, last frame, up to four keyframes | Match cuts, time passing, loops. Make them by editing one still |
| Audio | Native sound with lip-synced speech; preset voices only | The clip's audio is not your song: mute it |
| Fix and extend | Older model edits clips up to 8.7 s; extends by 2 to 10 s | Repair one detail; lengthen a held shot |

- Image-to-video output always matches the still's aspect ratio.
- Text-to-video renders a first frame, then animates it. Still first, then motion.
- App limits per plan changed on 12 October 2026 and are no longer listed per tier:
  check the composer.
- API prices per second: $0.14 (720p) and $0.25 (1080p) on Video 1.5; $0.03 (720p) on
  Lite. A 3:30 song at three times footage (630 s) costs about $19 on Lite, $88 on
  1.5 at 720p, $158 at 1080p.

## The motion prompt: five parts

The still carries the look. The motion prompt says only what changes.

| Part | Write | Example |
|---|---|---|
| Action | One subject action in up to three beats, with speed words | He lifts the glass an inch, stops, and sets it down slowly. |
| Camera | One named move, or a locked camera | Locked camera. |
| World | What the environment does | Embers drift through the doorway light and the duster hem stirs. |
| Hold | What must not change | Hat, bandana and bottles stay unchanged. |
| Sound | Ambience only | Sound: fire crackle, low wind, glass on wood. No music, no talking. |

## Rules

- Never re-describe or contradict the still. The model already sees it.
- The camera stays still unless you ask. Locked camera with patient motion reads as
  more cinematic than a needless move.
- Camera phrases that work: slow push-in, tracking shot alongside, camera drifts gently
  left, aerial push-in, locked, static.
- Speed and force words set intensity: slowly, then faster, with full force.
- About three beats. Focused prompts beat sprawling ones.
- Write the sound line like a sound designer. "No music" works well; "no talking"
  should keep mouths still.
- Generate two or three takes of each shot at about six seconds; cut the best two to four.

## Three patterns

```
Stillness: He lifts the glass an inch, stops, and sets it down slowly. Locked camera. Embers drift through the doorway light and the duster hem stirs. Hat, bandana and bottles stay unchanged. Sound: fire crackle, low wind, glass on wood. No music, no talking.

Travel: He steps off the porch and walks toward the gate, slowly at first, then with purpose. Tracking shot alongside at walking pace. Dry grass bends in the wind. Sound: boots on gravel, wind, a distant truck. No music, no talking.

Reveal: Slow push-in toward the open Bible on the pulpit as two pages lift in a draft. Dust moves through the window light. Sound: wood creak, soft wind. No music.
```

## Singing shots

Grok syncs lips to speech it generates, not to your track. Choose per video:

1. **Default:** keep mouths unreadable: profiles, wides, backs, hat shadow, hands on
   the instrument.
2. **Approximate:** put the exact sung line in quotes in the prompt, mute the clip,
   align it by eye in the edit. Forgiving for the skeleton cowboy (no lips); not for a
   human singer.
3. **Exact:** run the clip and the real audio through a separate lip-sync tool.

No xAI documentation shows a feature that takes your own track. Cut to the song yourself.

## Moderation

Clips are reportedly checked more strictly than stills. Describe the moment before and
the aftermath in plain physical words, and keep an alternate for every risky shot.
