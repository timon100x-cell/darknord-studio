# Cinematic Music Video Studio: Research and Build Plan

Nov 12, 2026 · Tim

Build this as a Claude Code project folder of skills for Dark Nord, not an app. Each song becomes a folder of plain files that moves through seven steps, and you approve three of them. I assumed you paste prompts into Grok Imagine by hand at first; API generation is the last, optional phase.

Five findings shape the design:

- **Story:** the strongest videos tell a second story that the lyric only implies, and they leave gaps. Showing each line literally is the weakest option.
- **Country:** the genre keeps one coherent story and cuts on bars, slower than pop. Its best videos add one turn the lyric never states.
- **Opening:** YouTube scores the intro at 30 seconds. The most arresting image belongs in the first five.
- **Grok stills:** subject first, style last, four to six plain sentences. The `--ar --stylize --v 6` block in your current prompts is Midjourney syntax with no documented meaning in Grok.
- **Grok motion:** the still carries the look. The motion prompt names one action, one camera move, the atmosphere and the sound.

## What makes a cinematic music video work

A music video holds attention when the pictures tell a story beside the lyric, and when the cut follows the song's form.

Andrew Goodwin's 1992 book *Dancing in the Distraction Factory* sorts videos by how the image treats the lyric ([summary](https://www.goconqr.com/note/1484660/illustration-amplification-and-disjuncture)). The tool uses his three modes as a dial.

| Mode | What the picture does | Use in the tool |
| --- | --- | --- |
| Illustration | Shows what the line says | The title line and one anchor line per section |
| Amplification | Adds meaning the lyric leaves out | The spine of every video |
| Disjuncture | Ignores or contradicts the lyric | Irony, or the moment a twist lands |

Carol Vernallis adds the second rule: music video editing does not serve a continuous story the way film editing does, and it answers to the music first ([Caston on Vernallis](https://repository.uwl.ac.uk/4706/1/EditingDossiermsmi.2017.6.pdf)). Videos show charged moments and leave gaps. The tool therefore writes a gapped story: key moments, no connective scenes, closure held back.

A study of 548 official videos confirms that editors cut to musical structure ([Prétet, Richard and Peeters, ISMIR 2021](https://arxiv.org/abs/2108.00970)). The editor it interviewed speeds up cutting toward climaxes in verses and choruses and slows it in bridges. The study labels 227 of the videos concept, 160 narrative, 74 performance and 62 dance, so story and concept dominate.

Each song section gets one story job. This table is my synthesis of those sources.

| Section | Story job | Picture and cut |
| --- | --- | --- |
| Intro | Cold open on the most charged image; raise a question | One or two long shots; natural sound can play before the vocal |
| Verse 1 | Who, where, what they want; plant an object | Bar-length shots, wide and medium, calm camera |
| Pre-chorus | Pressure builds toward a choice | Shorter shots, slow push-ins |
| Chorus 1 | The theme as one image that can return | Strongest composition of the video |
| Verse 2 | New information that changes verse 1 | New place or time; higher stakes |
| Chorus 2 | The chorus image again, visibly changed | Same framing, different state |
| Bridge | The turn: reveal, memory or low point | Longest takes; a shift in light or color |
| Final chorus | Payoff; the chorus image at its extreme | Fastest cutting; callbacks to earlier shots |
| Outro | Aftermath; an image that re-reads the opening | One held shot |

## Country and dark country

Country videos keep one coherent story where pop videos fragment, and the memorable ones add a turn the lyric never states.

The tradition is documented. Country videos kept storytelling and genre icons prominent to stay distinct from MTV's quick-cut style ([Fenster 1988, summarised here](https://blog.richmond.edu/spring2020-mus235-03/?p=175)). The ISMIR data agrees: in its small country sample of 34 videos, 29% had a dominant shot length of one bar, the highest of any genre, and only 47% cut at beat level, the lowest ([source](https://arxiv.org/abs/2108.00970)). For the tool this means bar-paced cutting and a story a viewer can follow with the sound off.

| Video | What the picture adds to the song | Technique to reuse |
| --- | --- | --- |
| [HARDY and Lainey Wilson, "wait in the truck"](https://en.wikipedia.org/wiki/Wait_in_the_Truck), dir. Justin Clough | Stages the lyric scene by scene, through the testimony to the prison visit | When the song is already a story, play it straight at film scale |
| [Carly Pearce and Chris Stapleton, "We Don't Fight Anymore"](https://americansongwriter.com/3-country-music-videos-that-tell-a-shocking-story/) | The house burns while the couple stand apart and watch | One metaphor made physical |
| [Cole Swindell and Lainey Wilson, "Never Say Never"](https://americansongwriter.com/3-country-music-videos-that-tell-a-shocking-story/) | The on-off couple turn out to be a prison guard and an inmate | A reveal that re-reads the lyric |
| [Reba McEntire and Linda Davis, "Does He Love You"](https://americansongwriter.com/3-country-music-videos-that-tell-a-shocking-story/) | A boat explodes, then the scene is shown to be a film set | A frame story with a double turn |
| [Johnny Cash, "Hurt"](https://stereogum.com/2204405/johnny-cash-hurt-american-iv-the-man-comes-around/reviews/the-anniversary), dir. Mark Romanek | A derelict museum and footage of the young Cash against the frail singer | Objects and decay as story; then against now |
| [The Dead South, "In Hell I'll Be in Good Company"](https://www.creativesask.ca/music-video-scores-16-million-views/), dir. Zach Wilson | The band performs in place while the backdrop keeps changing | One visual rule held for a whole song |

The Dead South video passed 440 million views on that single idea ([Wikipedia](https://en.wikipedia.org/wiki/The_Dead_South)). It is cheap to copy with AI: same figure, same pose, a new location on every bar.

Dark country draws on gothic country's subjects: crime, religious imagery, death, ghosts, the devil, betrayal, alcohol and murder ([Wikipedia](https://en.wikipedia.org/wiki/Gothic_country)). Its camera grammar comes from westerns ([No Film School](https://nofilmschool.com/wide-shots-from-classic-westerns)):

- Extreme wide with a small figure, which turns personal drama into fate.
- Extreme close-up on eyes, hands or one object, cut straight against the wide.
- A doorway or window as a frame inside the frame, for a character who cannot belong.
- My additions: silhouette against fire or low sun, and a slow push-in on a still figure.

The Dark Nord profile follows from this.

- **Story:** the skeleton cowboy is the constant, as Eddie is for Iron Maiden. Each video is a chapter. Endings are consequence or defiance, never redemption.
- **Look:** firelight and deep shadow with a readable skull; locked camera and slow push-ins; extreme wide cut against extreme close.

## Lessons from other genres

Each genre contributes one technique the tool can apply to country and dark country.

| Genre | Reference | What it does | What the tool takes |
| --- | --- | --- | --- |
| Hip-hop | [Childish Gambino, "This Is America"](https://www.kodak.com/en/motion/blog-post/hiro-murai-larkin-seiple/), dir. Hiro Murai | Six long choreographed shots; a calm performance in front, chaos behind | A second story in the background that rewards a rewatch |
| K-pop | [The BTS Universe](https://rollingstoneindia.com/building-the-bts-cinematic-universe) | One storyline spread across many videos since 2015, never officially explained | Recurring symbols across songs and a channel-level story bible |
| Metal | [Iron Maiden's Eddie](https://en.wikipedia.org/wiki/Eddie_%28Iron_Maiden%29) | One mascot who takes a new guise for each album | A new guise per song, same silhouette and marks |
| Pop | [ISMIR study of 548 videos](https://arxiv.org/abs/2108.00970) | Pop cuts cluster on section boundaries more than any other genre | Change location or look exactly where the section changes |
| R&B and editing craft | [Same study](https://arxiv.org/abs/2108.00970) | Cuts land on downbeats, or just before them for surprise | Place cuts a few frames ahead of the downbeat at climaxes |

Metal videos are performance-led by convention, which Goodwin lists as a genre trait. For a doom-leaning channel, the mascot's signature action in the chorus fills the role of the band performance.

## Keeping viewers watching

YouTube's intro metric is the share of viewers still watching after 30 seconds, so the video's best idea belongs in its first moments ([YouTube Help](https://support.google.com/youtube/answer/9314415)).

What YouTube states:

- A strong intro means the opening matched what the thumbnail and title promised, and kept interest.
- If your top moments come late, move that material earlier, because audiences shrink as a video plays.
- Spikes are parts that were rewatched or shared. Dips are parts that were skipped or where viewers left.
- Typical retention compares a video with your last 10 of similar length. Key moments need a video of 60 seconds or more and 100 views.

YouTube's own creator advice also recommends a cold opening that starts inside the action ([YouTube Blog](https://blog.youtube/creator-and-artist-stories/four-tips-to-hook-your-viewers-on/)).

The tool turns this into checks. These rules are design choices built on the sources above, not YouTube policy.

1. The first shot contains the thumbnail's subject.
2. The video opens on the story's most charged moment, then goes back. Your "Don't Push Me" storyboard already does this.
3. Every section opens one question and answers the previous one.
4. Something visible changes at every section boundary: place, time or light.
5. No shot returns unchanged. The chorus image comes back altered each time.
6. The reveal sits in the bridge or the final chorus, and the outro re-reads the opening.
7. After upload, dips and spikes are logged by timestamp in the channel profile for the next video.

## Grok Imagine today

Grok Imagine now runs on Imagine Image 2.0 for stills and Imagine Video 1.5 for clips, and both call for different prompts than the older models did. The facts below come from xAI's documentation as last updated in October 2026.

| Area | Current state | What it means for a music video |
| --- | --- | --- |
| Stills | [Image 2.0](https://docs.x.ai/developers/model-capabilities/images/generation): 1K or 2K; aspect ratio is a setting, with 16:9 and 21:9 available | Make every start frame at 16:9 from the start |
| Editing | [Up to five source images](https://docs.x.ai/developers/model-capabilities/images/multi-image-editing) per edit | Character, location and prop references in one frame |
| Clips | [Video 1.5](https://docs.x.ai/developers/model-capabilities/video/overview): 1 to 15 seconds, native 1080p from text or an image | One shot per clip; generate longer than you need |
| Budget model | Video 1.5 Lite: text and image to video only, at the lowest price | Drafts and background plates |
| References | [Up to 14 reference images](https://docs.x.ai/developers/model-capabilities/video/reference-to-video), tagged `<IMAGE_0>` onward, with a 720p ceiling | A recurring character without fixing the first frame |
| Pinned frames | First frame, last frame and up to four keyframes | Match cuts, time passing, loops |
| Audio | Native sound with lip-synced speech; public users get preset voices only | The clip's audio is not your song, so you mute it |
| Fix and extend | The older video model edits clips up to 8.7 seconds and extends by 2 to 10 seconds | Repair one detail; lengthen a held shot |

Image-to-video output always matches the still's aspect ratio. In text-to-video the model renders a first frame and then animates it, so "still first, then motion" is how the system works either way.

API prices per second are $0.14 at 720p and $0.25 at 1080p on Video 1.5, and $0.03 at 720p on Lite. A 3:30 song needs 210 seconds of footage. At three times that for takes and trims, 630 seconds costs about $19 on Lite, $88 on 1.5 at 720p, or $158 at 1080p.

In the app, clip length and resolution depend on your plan. A third-party tracker reports that the plans changed on 12 October 2026 and no longer list limits per tier, so check the composer ([Framesurfer](https://framesurfer.com/blogs/grok-imagine-video)).

Lip-sync follows speech the model generates. xAI limits voice references from your own audio files to trusted partners. Elon Musk posted Grok-made music videos on 14 October 2026 ([report](https://www.basenor.com/blogs/news/grok-can-now-make-music-videos-what-you-need-to-know)), but I found no xAI documentation of a feature that takes your own track. Plan to cut to your song yourself.

## Prompting Grok Imagine for images

A start frame is four to six plain sentences in a fixed order, subject first and style last. This follows xAI's [image prompting guide](https://docs.x.ai/developers/model-capabilities/images/prompting-guide) for Image 2.0.

| Order | The sentence covers | Dark country example |
| --- | --- | --- |
| 1 Subject | Who, their state, what supports them, the setting | A skeleton cowboy stands at the bar of a burned-out saloon, one gloved hand around a whiskey glass. |
| 2 Details | Wardrobe, materials, counts, camera angle | He has a cracked skull with thin glowing red fissures, a broken-brimmed hat, a tattered brown leather duster and one silver sheriff star. |
| 3 Art direction | Two or three named props and surfaces | The bar top is scorched oak, with a shattered mirror and three empty bottles behind him. |
| 4 Light | Source, direction, hardness, readable exposure | Hard orange firelight comes through the doorway on the left, with dim blue fill from a broken window; the skull stays clearly readable. |
| 5 Color | Subject colors against background colors | Rust orange and bone white against charcoal. |
| 6 Composition | Shot size, crop, focus, lens | Medium shot at eye level, framed from the waist up with open space on the right, 35mm film still with fine grain. |

The same order produces the extreme wide that cuts against it:

```
A lone skeleton cowboy sits on a gaunt dark horse at the crest of a bare ridge above a burning prairie. He has a cracked skull with thin glowing red fissures, a broken-brimmed hat, a tattered brown leather duster and one silver sheriff star. Two charred fence posts and one leaning wooden cross stand in the foreground. Low sun behind him turns rider and horse into a sharp silhouette, with only the red fissures glowing, while the fire lights the smoke orange from below. Burnt orange and smoke grey against a pale ash sky. Extreme wide shot from a low angle, the rider small in the upper third of the frame, 35mm film still with fine grain, everything sharp.
```

The guide's rules, in short:

- Lead with the subject. A prompt that opens on mood or film stock returns a styled scene with a stand-in subject.
- Describe what you want to see. Long avoid-lists are ignored, and the things they name tend to show up anyway.
- State a texture once, physically. Repeated texture words get painted onto the wrong surface.
- Ask for light that keeps the subject readable. Words like underexposed or crushed shadows pull the whole frame dark.
- Leave out dust, scratches and lens fringing. The model draws them as defects.
- In a series, keep the same sentence order and aspect ratio, and save each prompt beside its image.
- When subject and layout are right, edit instead of regenerating. Name one to three changes, then one sentence that keeps everything else.

Three additions for frames that will be animated:

- Choose the moment just before the action, and leave room in the frame for the movement ([Elser](https://www.elser.ai/blog/grok-image-to-video-guide)).
- Paste the character block word for word in every prompt. Paraphrase causes drift ([PC Tech Magazine](https://pctechmag.com/2026/09/from-song-to-screen-an-ai-music-video-workflow-with-gpt-image-2-5-and-seedance-2-5/)).
- Build a reference set per character: front, three-quarter and full body. Place the character into new scenes by image edit.

What to change in your current Dark Nord prompt skill:

| Now | Change to | Why |
| --- | --- | --- |
| `--ar 16:9 --stylize 550-700 --v 6` | Delete it; choose 16:9 in the composer | These are Midjourney parameters. xAI documents ratio, resolution and quality as settings and lists no in-prompt flags |
| "Grok Aurora" | Imagine Image 2.0 | The model and its guidance changed in August 2026 |
| Stacked style words: hyper-detailed, epic, rich cinematic grading | One physical texture and one named light source | Generic style words crowd out the subject |
| "Dark, moody, atmospheric" | Name the light and ask for a readable skull | Dark-mood words pull the whole frame dark |
| "Video start images use the same prompt" | A start-frame variant with room for motion | The still decides what can move |

## Prompting Grok Imagine image-to-video

The still carries the look, so the motion prompt says only what changes: one action, one camera move, the atmosphere and the sound.

| Part | Write | Example |
| --- | --- | --- |
| Action | One subject action in up to three beats, with speed words | He lifts the glass an inch, stops, and sets it down slowly. |
| Camera | One named move, or a locked camera | Locked camera. |
| World | What the environment does | Embers drift through the doorway light and the duster hem stirs. |
| Hold | What must not change | Hat, badge and bottles stay unchanged. |
| Sound | Ambience only | Sound: fire crackle, low wind, glass on wood. No music, no talking. |

Rules, from [Replicate's Video 1.5 prompting guide](https://replicate.com/blog/grok-imagine) and xAI's documentation:

- Never re-describe or contradict the still. The model already sees it.
- The camera stays still unless you ask. A locked camera with patient motion reads as more cinematic than a needless move.
- Camera phrases that work: slow push-in, tracking shot alongside, camera drifts gently left, aerial push-in, locked, static.
- Speed and force words set intensity: slowly, then faster, with full force.
- Keep to about three beats. Focused prompts beat sprawling ones.
- Write the sound line like a sound designer. "No music" works well, and "no talking" should keep mouths still.
- My recommendation: generate two or three takes of each shot at about six seconds, then cut the best two to four.

Three patterns cover most shots:

```
Stillness: He lifts the glass an inch, stops, and sets it down slowly. Locked camera. Embers drift through the doorway light and the duster hem stirs. Hat, badge and bottles stay unchanged. Sound: fire crackle, low wind, glass on wood. No music, no talking.

Travel: She steps off the porch and walks toward the gate, slowly at first, then with purpose. Tracking shot alongside at walking pace. Dry grass bends in the wind. Sound: boots on gravel, wind, a distant truck. No music, no talking.

Reveal: Slow push-in toward the open Bible on the pulpit as two pages lift in a draft. Dust moves through the window light. Sound: wood creak, soft wind. No music.
```

Singing shots need a decision, because Grok syncs lips to speech it generates and not to your track:

1. Default: keep mouths unreadable. Use profiles, wides, backs, hat shadow and hands on the instrument.
2. Approximate: put the exact sung line in quotes in the prompt, mute the clip, and align it by eye in the edit.
3. Exact: run the clip and the real audio through a separate lip-sync tool.

The skeleton cowboy has no lips, so option 2 is forgiving for Dark Nord. A human singer is not.

For API work, reference-to-video keeps a character without fixing the first frame, and first, last and key frames give controlled transitions. Make pinned frames by editing one still, so only the intended element changes ([xAI docs](https://docs.x.ai/developers/model-capabilities/video/reference-to-video)).

## AI music video production workflow

Lock the character and look first, plan shots on the bar grid, approve stills before paying for motion, then cut to the track.

1. **Bible.** Write the character, wardrobe, palette and one lens-and-grain line once. Reuse them word for word.
2. **References.** Make three to five stills of each recurring character and main location. A reference cannot rescue prompts that contradict each other ([DIY AI](https://diyai.io/ai-tools/video-generation/best-ai-music-video-generators/)).
3. **Timing map.** Note the section timestamps and the BPM. In 4/4, one bar lasts 240 divided by BPM seconds: 2.67 seconds at 90 BPM.
4. **Shot list.** Give each shot one, two or four bars. Hold wides longer than close-ups, and tighten toward each climax.
5. **Stills.** Generate, then judge each against its prompt: right subject, every named element, right count, bright enough.
6. **Motion.** Animate only approved stills, and mute the generated audio.
7. **Edit.** Cut on downbeats, or a few frames early at climaxes. Change place or light at section boundaries.
8. **Silent check.** Watch once with the sound off. If the story does not read, fix the shot list, not the prompts.

A 3:30 song at 90 BPM has about 79 bars, so two bars per shot gives roughly 40 shots. DIY AI's estimate for a four-minute video is about 48 clips and keyframes.

## The tool

The tool turns lyrics into a locked story and a shot list in seven steps, and writes two prompts for every shot.

Pipeline: lyrics and timing → song read → three concepts (you pick or mix) → beat sheet (you approve) → shot list on the bar grid (you approve) → prompts per shot, still then motion → critic check with fresh context (a failed rule sends the work back to the shot list) → storyboard page → retention notes after upload, which feed the next video.

| Step | You type | Claude does | File written |
| --- | --- | --- | --- |
| 0 | `/new-video` | Creates the song folder and loads the channel profile | `song.md` |
| 1 | `/song-read` | Finds the narrator, want, conflict, turn and title line; marks what the lyric leaves unsaid; builds the bar grid | `analysis.md`, `timing.json` |
| 2 | `/concepts` | Writes three treatments, each with a logline, chorus image, opening shot and turn | `treatment.md` |
| 3 | `/beats` | Gives every section one story job, one question and one payoff | `beats.md` |
| 4 | `/shots` | Lays shots on the bar grid with size, action, purpose and lyric link | `shots.json` |
| 5 | `/prompts` | Writes a still prompt and a motion prompt per shot, with the character block pasted exactly | `prompts.md` |
| 6 | `/check` | A critic with fresh context tests continuity, lyric fit, retention rules and Grok rules | `review.md` |
| 7 | `/board` | Builds one page with every shot, copy buttons and a status tick | `storyboard.html` |

The three concepts always differ in kind: one shows the song's story, one tells the story beside it, and one is built on a reveal. You pick or mix, as you do with lyric options.

The story steps follow six rules:

- Find the gap first: what happened before the song, what happens after it, and who else was there.
- Amplify by default. At most one literal line per section.
- One chorus image that returns changed each time.
- One turn, placed in the bridge or the final chorus.
- One object that passes through at least three sections.
- Channel rules win. For Dark Nord that means no redemption.

## Build plan in Claude Code

Build one project folder where skills hold the craft, small scripts do the arithmetic, and every song is a folder of plain files. Phases 1 to 4 need no API key and no code written by you.

| Piece | What it is | Why it fits |
| --- | --- | --- |
| `CLAUDE.md` | A file Claude Code reads at the start of every session | Holds the pipeline order and file names; kept short |
| Skill | A folder with a `SKILL.md`. You run it with `/name`, or Claude loads it when relevant | One per pipeline step. The body loads only when used |
| Reference file | Markdown beside `SKILL.md`, read on demand | Carries this report's knowledge at no cost until needed |
| Subagent | A helper with its own context, defined in `.claude/agents/` | The critic reviews without the writer's assumptions |
| Script | A small Python program Claude writes and runs | Bar arithmetic, validation and the storyboard page must be exact |
| Channel profile | One Markdown file for Dark Nord | Character bible, palette, story rules, lessons learned |

Skill behavior is taken from the [Claude Code skills documentation](https://code.claude.com/docs/en/skills). It recommends keeping `SKILL.md` under 500 lines and moving detail into supporting files. Custom slash commands are now the same thing as skills.

```
mv-studio/
  CLAUDE.md
  docs/research.md                 this report, exported as Markdown
  .claude/
    skills/
      new-video/SKILL.md
      song-read/SKILL.md
      concepts/SKILL.md            + story-craft.md, genre-playbooks.md
      beats/SKILL.md               + retention.md
      shots/SKILL.md               + shot-grammar.md
      prompts/SKILL.md             + grok-image.md, grok-video.md, examples.md
      check/SKILL.md
      board/SKILL.md
    agents/
      critic.md
  channels/
    dark-nord/profile.md
  scripts/
    timing.py                      BPM and timestamps to a bar grid
    validate.py                    rule checks on shots.json and prompts.md
    board.py                       renders storyboard.html
  songs/
    2026-11-song-title/            one folder per song, one file per step
```

| Phase | Build | Done when |
| --- | --- | --- |
| 1 Foundation | Folder, `CLAUDE.md`, the Dark Nord profile, reference files cut from this report, `/new-video` | A new song folder appears with the Dark Nord profile |
| 2 Story | `/song-read`, `/concepts`, `/beats` | A finished song yields three clearly different concepts and a beat sheet you would shoot |
| 3 Shots and prompts | `timing.py`, `/shots`, `/prompts`, `validate.py` | The validator passes, and five prompts tested in Grok give the stills they describe |
| 4 Review and board | Critic subagent, `/check`, `board.py` | The critic catches errors you plant on purpose, and the page opens with copy buttons |
| 5 Automation, optional | Audio analysis, xAI API batch generation with a spending cap, retention log | One song is generated end to end inside the cap |

Test Phase 2 on a song you already storyboarded by hand, so you can compare the tool with your own judgment.

Phase 5 has two parts. Audio analysis can start with librosa for tempo and beats. [allin1](https://pypi.org/project/allin1/) also labels verse, chorus and bridge, but it needs PyTorch and is harder to install on Windows. API generation calls `grok-imagine-image-2.0` for stills and `grok-imagine-video-1.5` or its Lite version for clips, which run as submit, poll and download. Generated URLs are temporary, so the script must save each file at once.

One note on your existing skills. Skills enabled on your claude.ai account sync into Claude Code when you sign in with that account, and local edits to the synced copies are overwritten. Update the Dark Nord prompt skill on claude.ai, or turn it off once `/prompts` replaces it, so two rule sets do not compete.

## Kickoff prompt

Start Claude Code in an empty folder, type `/plan` to enter plan mode, and paste the prompt below. In plan mode Claude proposes its approach before it edits anything.

Before you start, export this document as Markdown to `docs/research.md`, and have your existing Dark Nord skill files ready to paste.

```
I want to build "MV Studio" in this folder: a set of Claude Code skills that turn the
lyrics of my Dark Nord songs into a music-video story, a shot list and Grok Imagine
prompts.

Read docs/research.md first. It is my research report and the spec for this project.

Rules for the build:
- Work in the phases listed in the report's build plan. Build Phase 1 only, then stop
  and show me what you made.
- Each pipeline step is a skill in .claude/skills/<name>/SKILL.md. Keep every SKILL.md
  short and put knowledge in reference files beside it.
- Keep CLAUDE.md under 60 lines: pipeline order, folder layout, file names, and
  "never skip an approval step".
- Every step reads and writes plain files in songs/<date>-<slug>/. No database.
- Steps that need my choice (concepts, beat sheet, shot list) present options and wait.
- Scripts are Python and use no paid services. Tell me how to run each one.
- I am not a programmer. Explain choices in plain language and ask before installing
  anything.

Phase 1 deliverables:
1. The folder layout from the report.
2. CLAUDE.md.
3. channels/dark-nord/profile.md. Ask me for the character bible and style rules; I will
   paste my existing Dark Nord skill files. Rewrite the image rules to follow the
   report's Grok sections: subject first, no Midjourney flags.
4. Reference files cut from the report: story-craft.md, genre-playbooks.md,
   shot-grammar.md, retention.md, grok-image.md, grok-video.md. Each starts with a
   "last checked" date.
5. The /new-video skill.

Before writing anything, show me your plan and the list of files you will create.
```

Working habits that keep the build on track:

- One phase per session. Ask Claude to commit to git after each, so any step can be undone.
- Test each skill in a fresh session. Leftover context hides gaps in the written instructions.
- When a Grok result is wrong, tell Claude what the picture got wrong and have it fix the reference file, not only that prompt.
- Ask Claude to re-check the xAI docs monthly and update the "last checked" date in the two Grok files.

## Risks and open decisions

Four risks need a plan before the first full video.

| Risk | Handling |
| --- | --- |
| Grok's public documentation offers no lip-sync to your own track | Write stories that avoid sung close-ups; decide whether to add a lip-sync tool |
| Character drift, worst on human faces | Reference set, word-for-word bible, edit instead of regenerate, locked camera on face shots |
| Moderation of violent scenes; clips are reportedly checked more strictly than stills ([Atlas Cloud](https://www.atlascloud.ai/blog/guides/grok-image-is-moderated)) | Show the moment before and the aftermath in plain physical words; keep an alternate for every risky shot |
| Grok changes monthly | Keep all Grok rules in two dated reference files and nowhere else |

Open questions for you:

- [ ] Paste prompts by hand, or generate through the xAI API from Phase 5?
- [ ] One continuing Dark Nord story across videos, or standalone chapters?
- [ ] Windows or Mac? It decides the audio-analysis library.

Not researched here: YouTube's disclosure and monetization rules for AI-made music videos. Check them before scaling uploads.

## Sources

Read in full:

- xAI: [Image Prompting Guide](https://docs.x.ai/developers/model-capabilities/images/prompting-guide), [Image Generation](https://docs.x.ai/developers/model-capabilities/images/generation), [Multi-Image Editing](https://docs.x.ai/developers/model-capabilities/images/multi-image-editing), [Video Overview](https://docs.x.ai/developers/model-capabilities/video/overview), [Reference-to-Video](https://docs.x.ai/developers/model-capabilities/video/reference-to-video)
- Replicate: [How to prompt Grok Imagine Video 1.5](https://replicate.com/blog/grok-imagine)
- Basenor: [Grok Can Now Make Music Videos](https://www.basenor.com/blogs/news/grok-can-now-make-music-videos-what-you-need-to-know)
- Prétet, Richard and Peeters: [Is there a "language of music-video clips"?](https://arxiv.org/abs/2108.00970), ISMIR 2021
- YouTube Help: [Measure key moments for audience retention](https://support.google.com/youtube/answer/9314415)
- YouTube Blog: [Four tips to hook your viewers](https://blog.youtube/creator-and-artist-stories/four-tips-to-hook-your-viewers-on/)
- American Songwriter: [3 Country Music Videos That Tell a Shocking Story](https://americansongwriter.com/3-country-music-videos-that-tell-a-shocking-story/)
- University of Richmond course blog: [Distinguishing Its Country Genre](https://blog.richmond.edu/spring2020-mus235-03/?p=175)
- Anthropic: [Extend Claude with skills](https://code.claude.com/docs/en/skills), Claude Code documentation

Read as excerpts through search:

- Emily Caston: [The First Cut is the Deepest](https://repository.uwl.ac.uk/4706/1/EditingDossiermsmi.2017.6.pdf), on Vernallis
- GoConqr: [notes on Goodwin's three modes](https://www.goconqr.com/note/1484660/illustration-amplification-and-disjuncture)
- Wikipedia: [Wait in the Truck](https://en.wikipedia.org/wiki/Wait_in_the_Truck), [The Dead South](https://en.wikipedia.org/wiki/The_Dead_South), [Gothic country](https://en.wikipedia.org/wiki/Gothic_country), [Eddie](https://en.wikipedia.org/wiki/Eddie_%28Iron_Maiden%29)
- Creative Saskatchewan: [The Dead South video](https://www.creativesask.ca/music-video-scores-16-million-views/)
- Stereogum: [Johnny Cash, "Hurt"](https://stereogum.com/2204405/johnny-cash-hurt-american-iv-the-man-comes-around/reviews/the-anniversary)
- Kodak: [Hiro Murai and Larkin Seiple](https://www.kodak.com/en/motion/blog-post/hiro-murai-larkin-seiple/)
- Rolling Stone India: [Building the BTS Cinematic Universe](https://rollingstoneindia.com/building-the-bts-cinematic-universe)
- No Film School: [Wide shots from classic westerns](https://nofilmschool.com/wide-shots-from-classic-westerns)
- Grok practice: [Framesurfer](https://framesurfer.com/blogs/grok-imagine-video), [Elser](https://www.elser.ai/blog/grok-image-to-video-guide), [Atlas Cloud](https://www.atlascloud.ai/blog/guides/grok-image-is-moderated)
- AI video workflow: [PC Tech Magazine](https://pctechmag.com/2026/09/from-song-to-screen-an-ai-music-video-workflow-with-gpt-image-2-5-and-seedance-2-5/), [DIY AI](https://diyai.io/ai-tools/video-generation/best-ai-music-video-generators/), [allin1](https://pypi.org/project/allin1/)
