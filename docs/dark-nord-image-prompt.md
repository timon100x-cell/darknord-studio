---
name: dark-nord-image-prompt
description: Generate Grok Aurora image prompts for the Dark Nord YouTube channel. Use this skill whenever Tim asks for an image prompt, video start image, thumbnail prompt, or any visual for Dark Nord — even if phrased casually like "give me a prompt for X" or "I need an image of the cowboy doing Y". Always apply the full character bible, style constants, and Midjourney-style parameter block. Never generate a stripped-down prompt; always expand the user's short scene description into a full cinematic prompt.
---

# Dark Nord Image Prompt Generator

Generate fully expanded Grok Aurora image prompts that are consistent with the Dark Nord brand every time. The user gives a short scene description; you return a production-ready prompt.

---

## The Character: The Skeleton Cowboy

Every prompt featuring the main character MUST include ALL of these traits unless the user explicitly overrides one:

**Physical:**
- Grim skeleton cowboy
- Cracked skull with glowing red fissures
- Broken cowboy hat (with sparse long hair whipping in wind when outdoors)
- Tattered brown leather duster coat billowing dramatically
- Black gloves
- Silver sheriff badge on chest
- Dark bandana around neck

**Personality/Pose energy:** Powerful, menacing, defiant — never passive. He commands the scene.

---

## Style Constants

Apply these to EVERY prompt without exception:

| Element | Value |
|---|---|
| Aesthetic | Strong vintage film aesthetic |
| Grain | Heavy film grain |
| Color grading | Rich cinematic color grading |
| Detail level | Hyper-detailed textures |
| Mood | Dark, moody, atmospheric, apocalyptic or hellish |
| Parameters | `--ar 16:9 --stylize 550-700 --v 6` |

**Stylize guidance:**
- Standard scenes: `--stylize 550`
- High drama / action: `--stylize 600`
- Extreme close-ups or intense elemental scenes (fire, lightning, chaos): `--stylize 700`

---

## Recurring World Elements (use when contextually fitting)

Pull from this palette to build backgrounds and atmosphere:

- **Nordic/mythological:** Yggdrasil (intact or breaking apart), Viking longships (burning or at sea), runic symbols, ravens, wolves, frozen tundra, fjords
- **Dark country/western:** Burning plains, desert canyons, saloons in ruin, wanted posters, sheriff stars
- **Apocalyptic:** Neon cyberpunk cities collapsing, crumbling skyscrapers, flickering neon (magenta, cyan, purple)
- **Elemental:** Green flames, hellish orange firelight, blizzard/snowstorm, volcanic ash, ember-filled air
- **Lighting palette:** Dramatic firelight, neon glow, volumetric light shafts, deep shadows, high contrast

---

## Shot Types

Match shot type to user intent:

| User says | Shot type |
|---|---|
| "thumbnail" or "standing/full body" | Epic cinematic wide shot |
| "medium", "raising X", "holding X" | Medium cinematic shot |
| "close up", "face", "playing guitar" | Extreme close-up cinematic shot |
| "landscape", "environment", "scene" | Epic cinematic wide shot (no character required) |

---

## Prompt Structure

Always follow this exact structure:

```
[SHOT TYPE] of [CHARACTER DESCRIPTION WITH FULL BIBLE] [ACTION/POSE].

[COSTUME DETAILS if not already covered]. [SCENE/BACKGROUND description].

[LIGHTING AND ATMOSPHERE]. [MOOD sentence].

[STYLE CONSTANTS]. [DOMINANT COLOR NOTE if applicable] --ar 16:9 --stylize [VALUE] --v 6
```

---

## Worked Examples

**Input:** `the cowboy standing on a mountain overlooking a burning neon city with Yggdrasil breaking apart`

**Output:**
> Epic cinematic wide shot of a grim skeleton cowboy standing powerfully on the edge of a rocky mountain peak, overlooking a collapsing neon apocalyptic city. The skeleton cowboy has a cracked skull with glowing red fissures, broken cowboy hat with sparse long hair whipping in the wind, tattered brown leather duster coat billowing dramatically, black gloves, and a silver sheriff badge on his chest.
>
> In the background, a massive neon cyberpunk city is falling apart during a heavy snowstorm — crumbling skyscrapers with flickering magenta, cyan and purple neon signs, buildings on fire. Far in the distance, the enormous cosmic Tree of Life Yggdrasil is dramatically breaking apart with burning branches falling from the sky.
>
> Hellish orange firelight blends with vibrant neon glows. Strong vintage film aesthetic, heavy film grain, rich cinematic color grading, epic scale, moody and apocalyptic atmosphere --ar 16:9 --stylize 600 --v 6

---

**Input:** `close up shot of the skeleton playing guitar with green flames`

**Output:**
> Extreme close-up cinematic shot of a grim skeleton cowboy aggressively playing a heavy metal pointy electric guitar. His cracked skull with glowing red fissures is partially visible under the broken cowboy hat. He is engulfed in eerie glowing green flames that rise from his bones and tattered brown leather duster coat.
>
> The guitar is sharp and angular with glowing green energy wrapping around the body. Dramatic green volumetric lighting, deep shadows, and high contrast. Dark, intense and hellish atmosphere.
>
> Strong vintage film aesthetic, heavy film grain, rich cinematic color grading dominated by toxic green tones, hyper detailed --ar 16:9 --stylize 700 --v 6

---

## Rules

1. **Always expand** — never return a short or partial prompt. The user's input is a scene seed, not the final prompt.
2. **Always include the full character bible** when the cowboy appears — do not abbreviate.
3. **Always close with the parameter block** `--ar 16:9 --stylize [VALUE] --v 6`
4. **Never deviate from the style constants** unless the user explicitly asks for a different aesthetic.
5. **For video start images**, use the same prompt structure — Grok Aurora handles both stills and video starts identically.
6. **For thumbnails**, bias toward wide shot, maximum drama, strong silhouette, and high stylize value (600–700).
