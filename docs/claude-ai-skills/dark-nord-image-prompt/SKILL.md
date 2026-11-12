---
name: dark-nord-image-prompt
description: Generate Grok Imagine image prompts (Imagine Image 2.0) and image-to-video motion prompts for the Dark Nord YouTube channel. Use this skill whenever Tim asks for an image prompt, video start image, motion prompt, thumbnail prompt, or any visual for Dark Nord, even if phrased casually like "give me a prompt for X" or "I need an image of the cowboy doing Y". Always expand a short scene description into a full prompt in the fixed six-sentence order, with the character block pasted word for word.
---

# Dark Nord Image Prompt Generator

Last checked: 2026-11-12. Grok changes often; re-check xAI's prompting guide monthly.

The user gives a short scene seed; return a production-ready Grok Imagine prompt.
Never return a stripped-down prompt.

## The character: the Skeleton Cowboy

The only recurring element across videos. When he appears, paste this block **word for
word** as sentence 2. Never paraphrase, shorten or add to it:

> He has a cracked skull, a broken-brimmed cowboy hat over sparse long hair, a dark bandana around his neck, a tattered brown leather duster and black gloves.

Energy: powerful, menacing, defiant, never passive. He commands the frame.
He has no sheriff badge.

## Still prompt: six plain sentences, in this order

1. **Subject:** who, their state, what supports them, the setting.
2. **Details:** the character block (or wardrobe, materials, counts for others).
3. **Art direction:** two or three named props and surfaces.
4. **Light:** one named source, its direction and hardness, a dim fill, and
   "the skull stays clearly readable".
5. **Color:** subject colors against background colors.
6. **Composition:** shot size, angle, crop, focus, then `35mm film still with fine grain`.

## Rules

- **No parameter flags.** Never write `--ar`, `--stylize` or `--v`: they are
  Midjourney syntax and mean nothing to Grok. Remind Tim to pick 16:9 in the composer.
- **Subject first, style last.** Never open on mood or film stock.
- **No mood words** like dark, moody, underexposed, crushed shadows: they darken the
  whole frame. Name the light instead.
- **No stacked style words** (hyper-detailed, epic, rich cinematic grading). One
  texture, stated once.
- **No dust, scratches or lens fringing**: the model draws them as defects.
- **No avoid-lists.** Describe only what should be seen.
- **Any world is allowed.** Nordic, western, apocalyptic and elemental worlds are
  starting points, not limits. Nordic and western may share a frame.
- **Edits:** if subject and layout are right, write an edit instead: one to three
  changes, then "Keep everything else exactly the same."

## Shot types

| Tim says | Sentence 6 starts with |
|---|---|
| thumbnail, standing, full body | Extreme wide or wide shot; strong silhouette |
| medium, raising X, holding X | Medium shot at eye level |
| close up, face, playing guitar | Extreme close-up |
| landscape, environment | Extreme wide shot (character optional) |

Thumbnails: wide, strong silhouette against fire or low sun, maximum drama, subject
readable at small size.

## Video start frames and motion

For a start frame, pick the moment **just before** the action and leave space in the
frame for the movement. Then also give a motion prompt of five parts:

1. **Action:** one action in up to three beats, with speed words.
2. **Camera:** one named move (slow push-in, tracking shot alongside, camera drifts
   gently left) or "Locked camera." Locked is the default.
3. **World:** what the environment does (embers drift, the duster hem stirs).
4. **Hold:** "Hat, bandana and duster stay unchanged."
5. **Sound:** ambience only, then "No music, no talking."

Never re-describe the still in the motion prompt. Remind Tim to mute the clip's audio.

## Worked example

Seed: `the cowboy on a ridge above a burning prairie at sunset`

Still:
> A lone skeleton cowboy sits on a gaunt dark horse at the crest of a bare ridge above a burning prairie. He has a cracked skull, a broken-brimmed cowboy hat over sparse long hair, a dark bandana around his neck, a tattered brown leather duster and black gloves. Two charred fence posts and one leaning wooden cross stand in the foreground. Low sun behind him turns rider and horse into a sharp silhouette against the glow, while the fire lights the smoke orange from below. Burnt orange and smoke grey against a pale ash sky. Extreme wide shot from a low angle, the rider small in the upper third of the frame, 35mm film still with fine grain, everything sharp.

Motion:
> The horse shifts its weight and lowers its head slowly. Locked camera. Smoke rolls across the ridge and the duster hem lifts in the wind. Hat, bandana and duster stay unchanged. Sound: fire crackle, low wind, a horse snorting. No music, no talking.
