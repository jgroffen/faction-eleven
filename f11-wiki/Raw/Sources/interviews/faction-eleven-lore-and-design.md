---
Title: "Interview: Faction Eleven lore and game design"
Author: "Jim Groffen"
Reference: "Interview with the project author, 2026-08-08"
ContentType:
  - "interview"
Created: 2026-08-08
Processed: true
tags:
  - "source"
---

# Interview: Faction Eleven lore and game design

> Raw source material. Preserve the original context here. Do not rewrite this into a finished Wiki note — compile it into notes under `Wiki/` instead.

## Content

### Round 1 — 2026-08-08

**Q1 — What is Faction Eleven, in one sentence of format?** (genre, perspective, player count,
session shape, digital or tabletop)

> An open-world exploration computer game where you play through ten different stories as the
> main protagonist of each faction. Factions have different game mechanics in a mostly platform
> or top-down exploration game. The stories intertwine over time into a single story as the main
> protagonists discover the other factions and interact with each other.

**Q2 — Is "Eleven" literal, and is it a name from inside the fiction or outside it?**

> The eleventh faction is the mysterious antagonist of the game. The player discovers the
> eleventh faction, uncovering it's goals and motivations as they explore the story of each
> faction.

**Q3 — What does the player actually do, minute to minute?**

> While the game has a common gameplay style of a combination of platforming and top-down, each
> faction has unique gameplay mechanics, such as incremental, tower defence, rpg,
> platform-focused.

**Q4 — What is this project, practically?** (team, engine, commercial intent, prior material)

> A solo hobby computer game development project. Tech decided as godot based, goal is shippable
> commercial game. No prior code but extensive lore in my head.

### Round 2 — 2026-08-08

**Q5 — What kind of world is this?** (genre, era, tone, scale)

> It's a multiverse - each faction exists in it's own reality. Each reality has a different mood,
> feel and art-style. The realities go through cycles where they go from easy to almost impossible
> to traverse between them. The game is set after an extended period of disconnection between the
> realitites.

**Q6 — Give me the ten.**

> I have some old notes on the factions from when I developed a prototype - review
> `../../factions-retro/README.md` as your starting point on information for the factions, but we
> will need to go through each to determine what has changed.

(That document is captured as `Raw/Sources/factions-retro-readme.md`.)

**Q7 — One shared world, ten separate spaces, or one world with per-faction slices?**

> It's B, with ways of moving between the realities. The realities do have a concept of 'nearness'
> to each other. 'Close' realities are easier to traverse between.

**Q8 — How does "intertwine over time" actually work?** (shared vs sequential timeline; fixed,
free or gated order)

> Overlapping timeline - the player will be able to swap between faction protagonists to progress
> that story, but there will be story reasons that progress will become blocked for a faction
> while it's waiting for an event in another faction's story. Flow of time between the factions is
> story driven and doesn't have to be consistent.

**Q9 — What ships first, and what would you cut?**

> I'm thinking that the game will be released in chapters that progress the overall story.
> Factions I have the most concrete ideas around are the Ninja (from Institute of Eight faction),
> Robots, Knight from the Celestials, Gargoyle from the Green Skins, and the Conjurer from the
> mystics. I would focus on the Ninja first.

### Round 3 — 2026-08-08

**Q10 — Are the Ancients the eleventh faction?**

> Yes eleventh faction is 'the ancients' and this faction has unknown reasons for causing this
> cycle to be extended. All awareness of an eleventh faction has been lost, and rediscovering their
> existence, what they did, and why is part of the mystery to solve.

**Q11 — What caused the disconnection — the cycle, or someone?**

> There is a natural cycle but it has been extended to the point where the existence of other
> factions has become a myth to most factions. Each faction reality has gates to near-by realities
> that were built by the ancients. The gates are static and always allow traversal even when other
> ways don't. These gates have been locked and are guarded as well.

**Q12 — Templar or Knight, and is the rest of the roster still current?**

> It's Templar. Rosters from the factions-retro readme are still pretty accurate. The concept of
> six classes and each faction having a 'faction class' that fulfils the role of that class for
> that faction is also current, but more a lore the faction stories can leverage than rigid
> mechanics. Currencies are lore-only, may matter for some game types, and I'm thinking of
> simplifying it. Death mechanics is an idea I had around how to 'justify' repeated death as a
> mechanic. Keep as lore only for now. I think this will need a heavy review especially for game
> style and mechanics.

**Q13 — Do the realities have names?**

> Agree with recommendation. I added an image to `Raw/Files/` of a faction diagram with each
> faction numbered and arranged in a circle, showing 'near' faction realities. Starting from
> Institute of Eight as Faction 1, then Robots, Celestials, Mystics, Fey Folk, Pirates, Werebeasts,
> The Damned, Green Skins, Aliens. Factions that are opposite each other in the diagram are also
> historically enemies. Neighbours are historically friendly.

(The diagram is captured as `Raw/Sources/faction-diagram.md`.)

**Q14 — The genre list doesn't match — which is current?**

> The genre list has moved. We need to dive into each of them. Some may not be fully locked down
> like Fey Folk. Robots has changed for sure.

**Q15 — What is a chapter?**

> First chapter will be Robots mainly with a bit of Ninja and Templar. Ninja and Templar will seem
> like a mini-games in the first chapter, while the Robot story line will be main plot progression
> for first chapter.

### Round 4 — 2026-08-08

**Q16 — Is "platforming and top-down" the shell or the game?**

> It's the shell. Some faction-realms (maybe we use the term realm instead of realities?) have
> additional mechanics but should build on the shell to do so.

**Q17 — Where did "incremental" come from?** (interviewer's recommendation: Robots is now the
incremental faction)

> Agreed - it's an exploration platformer where you grow incrementally by collecting parts and
> other currencies, and repairing robots. Exploration is gated by unlocking skills through an
> incrementally unlocked skill tree, for example needing wall-crawling to access some areas.

**Q18 — How much of the review is rewrite versus recall?** (recommendation: deep on the
chapter-one three, medium on Green Skins and Mystics, leave the other five explicitly unsettled)

> Agree.

**Q19 — Robots first: what has it become?** (recommendation: keep the fiction, replace the
strategy layer with an incremental production/automation layer)

> Agree.

### Round 5 — 2026-08-08

**Q20 — What is the Ninja's game style now, and what were the "audio game cues"?**

> Ninja is a skill-based platformer more like Super Meat Boy with longer, difficult levels that
> have short sections between respawn points that are fast to retry, fast respawns and
> pattern-learning. Should be fast action. Each short section has music that has beats which are
> hints to user inputs, a bit like an old game called bit-trip-beat. When the ninja jumps or
> attacks it makes a sound. If timed well it'll line up with the music. Training sessions teach the
> player about timing and teach new moves that are needed to progress.

**Q21 — Chapter one shows Ninja as a "mini-game". What does that mean?** (options: vertical slice /
genuinely reduced / diegetic mini-game)

> Genuinely reduced - a single cycle of boss-fight, defeat, train. There will be some lore-building
> and the mini-fix bot in the family shrine.

**Q22 — When does the Ninja's gate open, relative to chapter one?**

> Gate doesn't open in Chapter 1. Ninja won't get it open until after all factions have been
> introduced.

**Q23 — How does the Ninja connect to the Robots in chapter one?** (recommendation: through the
mini-fix bot in the family shrine)

> Agree, There will be a story event in the robot's story where he gets an ability to remote
> communicate with his auto-fix bots. This wil wake up the auto-fix bot in the ninja's shrine.

### Round 6 — 2026-08-08

**Q24 — What is the Templar's game style now?** (recommendation: tower defence with the Templar as
a platformer hero inside it)

> Good recommendation but the gameplay really needs to be top-down. Other factions like pirates and
> probably wraith from the damned will be top-down. Templar will be a hero unit that moves around
> the top-down TD field.

**Q25 — Is the Templar in chapter one "genuinely reduced" like the Ninja?**

> Minigame is the templar at an outpost. It's a very simple TD game that the templar loses in the
> last wave when the siege machine comes. Templar leads his people in retreat to a Templar Monastry
> - which will be the setting for celestial faction-realm in Chapter 2.

**Q26 — Does the Celestials' story touch the Robots' in chapter one?**

> There won't be a connection until the end of Chapter 2. In Chapter 2 the Templar will again lose
> to the war machine and have to retreat to a Templar Monastry. The templar chooses this location
> as he believes the celestials need to find ancient allies to defeat the war machine. Between TD
> levels the templar will explore the ancient parts of the monastary in a platform game. Before
> retreating he will find and use two ancient devices to signal ancient allies for aid - an autofix
> bot that he is able to turn back on, and a wand. This will send a signal that the autofix robots
> (with their restored remote comms) and the mystics will receive. The mystics-realm will be a major
> setting in Chapter 2. Lets add clay jar to the ninja's family shrine too that contains an alien
> egg which can be activated to signal the aliens. The clay jar has a symbol on it that will reveal
> the nature of the jar to the player.

**Q27 — The Ninja's generational death — which reconciliation?** (recommendation: generations apply
only to boss defeats)

> Agree - but need an in-universe explanation - he doesn't die except in boss-fights, he can recover
> from other failures.

### Round 7 — 2026-08-08

**Q28 — Are the signalling devices the Ancients' work?** (recommendation: yes, and that's the
reveal)

> The signals are not made by the ancients. They were a means of allied factions to contact each
> other for aid. When the factions became sealed the signals couldn't cross the faction realms. I
> propose that the ninja fails the boss fight but before the end of Chapter 1 the boss battle causes
> a crack in the gate. This crack allows comms between the minifix bot and teh autofix bot.

**Q29 — Why does the Ninja die only in boss fights?** (recommendation: the mini-fix bot repairs
them, but cannot reach the gate)

> Agreed - the minifix bot can 'repair' the ninja whenever near him but cannot get near the gate
> warden, so cannot save the ninja in boss battles.

**Q30 — What are the faction unique features?** (recommendation: name only the three built —
Robots repair/remote comms, Institute timing, Celestials hero defence)

> Agreed.

**Q31 — Is there anything you've been holding back?**

> I want the high-level outline of the entire story, key story points, and the role of each faction
> in it before starting any development.

### Round 8 — 2026-08-08

**Resolving the open gate-geometry question from `the-cracked-gate`.**

> Lets resolve the gap - I want the ninja gate to be to the robot-realm. In chapter 2 the minifix
> bot states it can detect another minifix bot signal, different than the signal through the cracked
> gate. This leads the ninja to an old abandoned gate in an ancient ruin which is already cracked.
> This is the gate of the green-skins. This leads the ninja to the gargoyle. The gargoyle is himself
> very ancient and wants to stop the war the Green-skins are fighting with the celestials. He will
> work with the Ninja to find the minifix bot ... which the templar has.

## Notes for Compilation

- Ten playable factions, each with its own protagonist and its own story; an eleventh faction is
  the antagonist and is not (per this round) playable.
- Round 3 confirmed the Ancients **are** the eleventh faction; `the-ancients` was folded into
  `faction-eleven-antagonist` as an alias rather than kept as a separate note.
- Round 3 **rejected** the interviewer's Q15 recommendation (Institute of Eight + Green Skins as
  chapter one) in favour of Robots-led with Ninja and Templar as mini-games.
- Round 3 **rejected** the interviewer's Q12 recommendation (rename Templar to Knight).
- Outstanding after round 3: the per-faction deep dive on game style and mechanics, which the
  author describes as a heavy review. Robots first — it has changed for certain and leads
  chapter one.
- Round 4 settled **terminology**: *realm* replaces *reality* as the canonical term, at the
  author's suggestion. The wiki was renamed accordingly, with *reality* kept as an alias.
- Round 4 settled the Robots' game style and confirmed the shared exploration loop is a **shell**
  that faction genres build on.
- Round 5 settled the Institute of Eight. The interviewer's Q20 guess that the audio cues meant
  fighting blind was **wrong** — they are a rhythm layer, with the music's beats hinting at inputs.
- Round 5 produced the first concrete story-gating event, `the-shrine-bot-awakens`.
- Round 6 settled the Celestials and specified chapter one end to end. The interviewer's Q24
  recommendation (platforming hero inside a TD) was **partly rejected**: the field is top-down, not
  platforming, though the hero unit is still directly controlled.
- Round 6 introduced **ancient signalling devices** as the mechanism of convergence, and with them
  the wiki's first item notes.
- Round 7 **rejected** the interviewer's Q28 recommendation. The signalling devices are **not** the
  Ancients' work: they are old allied-faction technology, silenced by the sealing rather than
  confiscated. `ancient-signalling-devices` was renamed `allied-faction-signals` and rewritten.
- Round 7 added `the-cracked-gate`: the Ninja's *defeat* fractures the gate, and that crack is what
  lets the two bots hear each other. Chapter one is now one causal chain rather than three parallel
  demos.
- Round 7 closed the interview with a project constraint: **no development until the whole story
  exists at outline level** (`story-outline-requirement`).
- Round 8 settled the gate geometry: the guardian's gate faces **realm-02 (the robots)**,
  superseding the prototype notes, which had it facing the green-skins. Realm-01 has a *second*
  gate to realm-09 — abandoned, unguarded, already cracked — in a new location, `the-ancient-ruin`.
  Gates are therefore ten separate doors, not one membrane.
- Round 8 gave the Gargoyle a motive (stop the green-skins' war on the Celestials) and an age
  ("very ancient"), and made chapter two converge on `the-monastery-autofix-bot`.
- Round 8 left one prototype beat homeless: "the gate was sealed and guarded **for a reason**",
  which no longer attaches to the guardian's gate. Recorded in `the-cracked-gate`.
- Still outstanding: game styles for `green-skins` and `mystics` (both needed for chapter two);
  seven unnamed faction unique features; why the robot gate is guarded at all; and the Ancients'
  motive, which the story outline cannot be finished without.
- Round 2 rejected the interviewer's recommendation on Q7 (one world, per-faction slices) in
  favour of ten separate realities with traversal between them, and rejected the Q8
  recommendation of free order in favour of story-gated blocking.
- **Unresolved contradiction carried into round 3:** the retro README says the Ancients (humans)
  locked the factions apart; this round says traversal difficulty is a natural cycle. Also
  Templar vs Knight for the Celestials protagonist.
- The genre-per-faction structure is the central design bet and the central scope risk — ten
  distinct genre systems built solo.
- Open question raised for round 2: world topology, story ordering, the nature of the eleventh
  faction, and the vertical slice.
