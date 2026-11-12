# Grok Imagine: Still Images

Last checked: 2026-11-12 (source: docs/research.md; xAI docs as updated October 2026)
Re-check monthly against https://docs.x.ai/developers/model-capabilities/images/prompting-guide

## Model and settings

- Model: **Imagine Image 2.0** (replaced "Grok Aurora" guidance in August 2026).
- Resolution 1K or 2K. Aspect ratio is a **setting in the composer**: choose 16:9
  (21:9 also exists). Never write it in the prompt.
- Image editing takes up to five source images: character, location and prop
  references in one frame.
- There are **no in-prompt flags**. `--ar`, `--stylize` and `--v` are Midjourney
  syntax with no documented meaning in Grok. Never write them.

## The six sentences, in this order

Four to six plain sentences. Subject first, style last.

| # | Sentence covers | Example |
|---|---|---|
| 1 | Subject: who, their state, what supports them, the setting | A skeleton cowboy stands at the bar of a burned-out saloon, one gloved hand around a whiskey glass. |
| 2 | Details: wardrobe, materials, counts, camera angle | The channel's character block, pasted word for word. |
| 3 | Art direction: two or three named props and surfaces | The bar top is scorched oak, with a shattered mirror and three empty bottles behind him. |
| 4 | Light: source, direction, hardness, readable exposure | Hard orange firelight comes through the doorway on the left, with dim blue fill from a broken window; the skull stays clearly readable. |
| 5 | Color: subject colors against background colors | Rust orange and bone white against charcoal. |
| 6 | Composition: shot size, crop, focus, lens | Medium shot at eye level, framed from the waist up with open space on the right, 35mm film still with fine grain. |

Worked example, extreme wide:

```
A lone skeleton cowboy sits on a gaunt dark horse at the crest of a bare ridge above a burning prairie. He has a cracked skull, a broken-brimmed cowboy hat over sparse long hair, a dark bandana around his neck, a tattered brown leather duster and black gloves. Two charred fence posts and one leaning wooden cross stand in the foreground. Low sun behind him turns rider and horse into a sharp silhouette against the glow, while the fire lights the smoke orange from below. Burnt orange and smoke grey against a pale ash sky. Extreme wide shot from a low angle, the rider small in the upper third of the frame, 35mm film still with fine grain, everything sharp.
```

## Rules

- **Lead with the subject.** A prompt that opens on mood or film stock returns a
  styled scene with a stand-in subject.
- **Describe what you want to see.** Long avoid-lists are ignored, and what they name
  tends to show up anyway.
- **State a texture once, physically.** Repeated texture words get painted onto the
  wrong surface.
- **Ask for light that keeps the subject readable.** Words like underexposed or crushed
  shadows pull the whole frame dark.
- **Leave out dust, scratches and lens fringing.** The model draws them as defects.
- **In a series,** keep the same sentence order and aspect ratio, and save each prompt
  beside its image.
- **Edit instead of regenerating** when subject and layout are right: name one to three
  changes, then one sentence that keeps everything else.

## Frames that will be animated

- Choose the moment **just before** the action, and leave room in the frame for the movement.
- Paste the character block word for word in every prompt. Paraphrase causes drift.
- Build a reference set per character: front, three-quarter and full body. Place the
  character into new scenes by image edit.

## Replacing the old Dark Nord prompt habits

| Old | New | Why |
|---|---|---|
| `--ar 16:9 --stylize 550-700 --v 6` | Delete; choose 16:9 in the composer | Midjourney parameters; xAI lists no in-prompt flags |
| "Grok Aurora" | Imagine Image 2.0 | Model and guidance changed August 2026 |
| Stacked style words (hyper-detailed, epic, rich cinematic grading) | One physical texture and one named light source | Generic style words crowd out the subject |
| "Dark, moody, atmospheric" | Name the light; ask for a readable skull | Mood words pull the whole frame dark |
| "Video start images use the same prompt" | A start-frame variant with room for motion | The still decides what can move |
