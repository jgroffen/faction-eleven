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

### Round 9 — 2026-08-11

**Interviewer's question: is there a discrepancy in the shrine bot "waking up" when the gate is
cracked, given the bot is also the reason the Ninja survives non-boss failures?**

> The bot doesn't wake up as it's always awake and the reason the ninja doesn't die except in boss
> fights. Instead the minifix bot is like a companion and mentor of the ninja, and has been online
> and maturing for generations of the ninja's family. When the gate is cracked the minifix bot
> receives the two signals - one from the Autofix bot in the robot's realm and another from the
> minifix bot in the Templar's Celestial realm, whose signal traverses from the open gate between
> the Green Skins and Celestial realm and the ruin that contains a gate from the Ninja's realm to
> the Green Skins realm.

### Round 10 — 2026-08-11

**Naming and motivating the shrine mini-fix bot, and resolving the signal-timing discrepancy.**

> Lets give the shrine minifix bot a name - Mifix. Mifix and the Ninja family line are motivated to
> defeat the Gate Boss as the family has a legacy to reunite the allied factions - Mifix believes he
> may be the only robot with autofix capabilities left and without autofix bots the robots slowly
> degrade ... but the details and Mifix's memory have become corrupted and reasons are shrouded in
> myth.
>
> Also, lets resolve the discrepency - There are two story beats that must occur before Mifix
> detects the signal from the Celestial Minifix bot. 1: The robot story line progresses to where the
> Autofix bot unlocks Quantum Comms (the skill that allows for remote comms to minifix bots) and 2:
> The templar must find and activate their signals. Only when both are done will Mifix hear the
> faint signal of the remote minifix bot. Additionally, Mifix won't hear the Autofix or Templat
> minifix bot at all unless there is a crack in the Boss Guarded Gate. The gate isn't cracked all
> along, it's cracked when the Ninja progresses to the Boss Battle with a new (to be determined)
> trained skill.

### Round 11 — 2026-08-11

**The mechanism behind the crack — why it gates reception of both signals.**

> All gates from the Robot Realm are fully sealed and Quantam Comms can't operate without an
> opening. The crack lets both minifix bots receive the signal from the Autofix bot. Mifix and the
> Ninja decide that seeking this faint signal is worth investigating as an alternative way to get to
> the Robot Realm.

### Round 12 — 2026-08-12

**Q32 — Minibot versus mini-fix bot: what's the difference?**

> Agreed. I'm thinking Minibots are like an upgraded currency. Player collects various kinds of
> scrap to repair robots. Robots once repaired unlock lore and progress (giving you a skill or
> training currency). Skills to unlock include module construction which leads to more unlockable
> skills like: Memory Module Construction, CPU Module Consturction, GPU, DPU, MPU, Quantum Core.
> Another branch of the skill tree is Component Construction that unlocks various sensor and
> effector components. The autofix bot will come across robots that need specific kinds of modules
> and components to repair them. The modules and components are also used to (once the skills are
> unlocked) build Minibots. First kind of minibot is general and can collect basic scrap parts.
> Later specialised minibots can later be unlocked via the skill tree. Ideas include: Shield-bot,
> Suppressor-bot, EMP-bot, all help disable robots that have gone mad or have become aggressive so
> the autofix bot can repair them. Unlocking the building of minifix bots is the culmination where
> the Robot realm can essentially start to self-repair, but all minibots only work in a short range
> of the Autofix bot. A different skill tree for the Autofix bot would include upgrades - like Short
> Range Comms required to control minibots, Long Range Comms, Extremely Long Range Comms, and
> finally Quantum Comms. The various minibots can be upgraded too.

**Q33 — What do minibots actually do?** (options: automation / tools / followers)

> Why not all three? Short Range Comms allows for easier / better scrap collection and unlocks c)
> which increases the pool of Robots that can be repaired (and acquiring more skill points and
> lore), Long Range Comms unlocks b) which could help gate progress by blocking exploration.
> Extremely Long Range Comms would unlock a) where the minibots can be assigned to collect scrap
> automatically.

**Q34 — One progression system or two?**

> See Q32 answer. I'm thinking for skill tree branches: Scrapping (scrap collection efficiency,
> converting scrap into different kinds of construction materials), Upgrades (movement, comms,
> armor, diagnostics, scanning range (for diagnostics), max controllable minibots), Fabrication
> (modules and components), Repair (what kinds of damage you can fix), and Robotics (building
> minibots, maybe eventually building Robots - true reproduction).

**Q35 — What is "fixing a deranged robot" as an activity?**

> It's a parts puzzle with varied outcomes. If a robot can't be repaired it can be scrapped. If it
> can be repaired it can provide skill points, lore, quests, unblock paths opening more exploration
> options. Some robots that can't be repaired yet will block progress. The autofix bot will know if
> a robot can be repaired or not, but may not know how until it's diagnostic skills are upgraded. If
> it can diagnose a malfunctioning or fully disabled robot it will know what parts are needed to
> perform the repair.

**Q36 — Does Autofix understand what he hears?**

> Autofix can control all the minibots he built. He can issue commands too. Minifix bots are
> special. Even the ones he built he can communicate with but they are far more autonomous like
> other robots - he can communicate but not control, though like most robots once fixed they are
> happy to work with the Autofix bot. Mifix and the distant Templar minifix bot are detectable (once
> the crack in the door event occurs, and the Templar minifix bot is activated), but they are too
> far away to communicate. I think a good reveal would be the Templar minifix bot has uncorrupted
> memory and when Mifix and the templar's minifix bot meet the minifix bot can reveal robot realm
> history that was lost. Need to consider what this minifix bot knows, maybe give it a name.

### Round 13 — 2026-08-12

**Q37 — "Minibots are like an upgraded currency" — stored labour, or spendable?**

> They are stored labour AND currency - you upgrade a minibot to make specialised minibots, doing so
> 'consumes' a minibot reducing the stored labour.

**Q38 — What breaks the range leash?** (recommendation: mini-fix bots are exempt, and that's the
point of them)

> agreed.

**Q39 — Does Autofix know what "Quantum" means?** (recommendation: he is recovering technology he
does not understand)

> Agreed sort of, the skill points represent rediscovery - the autofix bot doesn't have the
> schematics - the schematics aren't neatly available anymore. The autofix bot is discovering the
> robots history and technology by collecting data from repaired robots - lets rename skill points
> as 'Data fragments'. Unlocking a skill reflects the Autofix bot researching the data fragments and
> rediscovering lost knowledge from them.

**Q40 — Name the monastery bot, and decide what it knows.**

> great suggestions. The Templar minifix bot is known to the Celestials as the Relic of St Archivus.
> Once activated, the minifix bot knows his designation as MF-710D (MF-28941 in decimal). He
> remembers the Celestials nick-named him Odie before he was put in stand-by mode to preserve his
> memory module from long-term degradation. Minifix bots and autofix bots can't repair themselves.

**Q41 — Does the Robotics branch reach "true reproduction"?**

> Agreed. Lets block access to the autonomous robotics skills with an 'ACCESS DENIED' block-out.
> Later chapters would work towards unblocking this skill tree. Odie will have hints on what's needed
> to do this. Note that the Ninja, Mifix, and Garagoyle reaching the Templar is the culmination of a
> Chapter. I'm thinking the Mystics gameplay and the Mystics protagonist also reaching and supporting
> the Templar should also culminate at the end of the same chapter. Lets delve into the Mystics in a
> later session. I might need to re-arrange things, and make Chapter 2 focus on the Gargoyle
> gameplay, and move the Mystics gameplay and culmination of the Ninja, Mifix, Gargoyle, and Mystics
> protagonist reaching the Templar as the culmination of Chapter 3 instead.

### Round 14 — 2026-08-14

The author opened the round with the conclusions rather than answers, having asked for mechanic
ideas for the Gargoyle (originally imagined as stealth platforming, then as squad turn-based):

> Conclusion is Gargoyle is going to use the same platforming engine as the ninja, but with a
> different skill set (different platforming moves) and no rhythm mechanic. Lets change the Gargoyle
> game mode to Metroid style. When the Gargoyle is playing he has a minimal skill set to begin with,
> I'm thinking he can stealth without moving only. When the ninja moves into the Green Skin's realm
> he will have the same Metroid style progression through unlocking upgrades approach that
> represents growth for the ninja character as well.

**Q42 — The ability system, and the Gargoyle's move set.**

> Gargoyle mechanics, probably incomplete and in no particular order: Stone-form - no move stealth,
> stone strength - move heavy obstacles, glide - span otherwise impassable gaps and obstacle
> avoidance, Stone-stealth - slow-speed stealth, stone strength 2 - move heavier obstacles and break
> some obstacles, stone-drop - stone form while jumping that can be used to break through weak ground
> from great heights and knock out opponents, Double Jump - gargoyle can flap once, triple jump, quad
> jump - shows the gargoyle getting closer to full flight, Gargoyle flight, Gargoyle Legacy - final
> unlock that grants sonic flight - super strength - super fortitude.

**Q43 — Which structure governs realm-09, and does the rhythm layer travel?** (recommendation:
genre is a property of the realm; the rhythm stays home)

> Agree - Gargoyle unlocks upgrades by finding Gargoyle lore fragments - when in Realm 9 the Ninja
> 'upgrades' are instead training opportunities - The ninja finds a challenge room - Mifix and the
> Ninja have some dialog then 'learn' the new skill by practicing it in the room.

**Q44 — What does stationary stealth do, and what happens when he's seen?**

> It resets the section - The reason to stealth may vary per section but the Gargoyle is trying to
> subvert the invasion (we'll get into the lore and story in a separate grilling), some sections will
> simply be he is kicked out of whererever he is.

**Q45 — Does he fight?** (recommendation: no — his kit disables rather than destroys)

> No he doesn't fight - he wants to protect and save the Green skins and wants to stop the Green
> Skins faction from being manipulated and used. gargoyles see themselves as protectors.

**Q46 — Where do upgrades come from, and who teaches the Ninja?**

> Already covered by Q43 answer.

**Q47 — What happened to the party members?** (recommendation: make recruits *be* the upgrades)

> I think this idea isn't compatible with the Metroid style - I'll save it for a different faction.
> Gargoyle and Ninja will find each other at some point in chapter 2 but the gameplay in the Green
> Skins realm doesn't suit party or squad mechanics. We should record a decision that the realms
> mechanics apply when gameplay is in that realm - hence the ninja gameplay swaps to Metroid style in
> realm 9, the Gargoyle and ninja ultimately move on to celestial realm in chapter 3 and their
> gameplay will swap to Templar tower defence with heroes style.

**Q48 — Map shape and saves; is Mifix the save point?**

> Gargoyle is permanent progression every time he passes a section and collects upgrades - his story
> doesn't involve dying in Green Skins realm. Mifix is the save / restore mechanic in the Green Skins
> realm for the Ninja.

**Q49 — Cracking: what does failure cost the Gargoyle?** (recommendation: a crack costs an ability)

> Failure costs the gargoyle progression - he is forced back to the start of the section he is
> working through.

### Round 15 — 2026-08-16

The author opened a grilling on **Gargoyle lore** with the following statement of the high-level
material. Recorded here verbatim as the round's evidence; the questions put to it follow in round
16.

> high level is the Gargoyle story starts with a cutscene showing how the Gargoyles are magical
> constructs made by necromancers from the damned realm (realm 8) and shamans from realm 9.
> Gargoyles are dead orcs that are resurrected and golem-ified - they are imbued with magical power,
> but are autonomous and only follow instructions they are imbued with. This was done so that the
> gargoyles couldn't be used against another faction. The gargoyles imbued instructions are that
> they are realm guardians, they cannot act except in defence of a realm being invaded - they cannot
> work against their own faction.
>
> They were created to defend against attacks from the Celestials, mystics, and fey folk, who were
> constantly incurring into the Green skins, Damned, and werebeast realms.
>
> The cut scene shows the creation of the Gargoyles, that they are defenders only - they are
> dispatched to fight back the invastions and seal up the gateways from the enemy factions. They
> return and are instructed to rest until needed again.
>
> Gargoyles enter stone form and scene cuts to black to represent a time jump. Same scene fades in
> and it's apparent much time has passed. Then a hooded vampire woman in robes enteres with a
> Minotaur and a Giant. The woman orders 'do it!' and leaves. The minotaur and giant smash all the
> gargoyles' heads with hammers. The hammer breaks on the last gargoyle's head, only partially
> smashing his head. The minotaur and giant look at each other, shrug, and leave.
>
> Fade to black and fade in to the same scene - a bolt of power awakens the last gargoyle - and
> gameplay starts. The reason the gargoyles awoke is because the realm was unsealed so the green
> skins, damned, and werewolves can attack the celestials.
>
> Part of the gameplay is the gargoyle begins alone with knowing his backstory, and knowing he is
> missing much of his power. He doesn't know why he is awake but thinks he mustn't let anyone know
> he is active when he doesn't know what's going on. These gargoyles are loyal to the Green Skins,
> there are gargoyles in the werebeasts realm and the damned realm too that are loyal to those
> realms.

### Round 16 — 2026-08-16

Answers to the questions put to round 15's material.

**Q51 — Is he broken, or is he interpreting?**

> I like the angle that an antagonist he comes across in the green skins realm tries to convince him
> he is malfunctioning - lets make that happen with the vampire woman. The answer is the gargoyles
> could shape rock too - and they shaped the barriers on the inside of the realm gates - they are
> awoken when the barrier is broken. The implication is there was a plan to break the barrier to the
> celestials realm and so the gargoyles were destroyed before the plan was enacted so they wouldn't
> wake. The reason they wake is obvious - if their barrier is broken then the realm is under attack
> from an outsider. The gargoyle won't know why he has awakened but sees the destruction of his
> fellow gargoyles and concludes that the green skin realm is under threat somehow, so he starts
> trying to work out why. As the gargoyle story progresses he will discover that the celestial gate
> barrier was broken and the Green Skins generally think it's because the celestials started another
> incursion. Later he will uncover that the barrier was broken by a group secretly working to incite
> the green skins, werebeasts, and the damned to attack and invade the celestials. Lets call this
> secret group something ... lets say they call themselves the Gardians of Night.

**Q52 — When is this, and does he remember the world before?**

> The gargoyles were made and sealed the gate's to the celestial, fey folk, and mystics realms a long
> time ago, but yes the gargoyles do not know of the ancients, but are aware of the other realms.
> Lets soften the lack of awareness of other realms - most residents in most realms are not aware of
> other realms, or have little awareness of only a few realms or legends of people from other places.
> The Werebeasts, Damned, and Green Skins have better awareness than most as their realms were
> connected and friendly for a long time whereas most realms had little to do with each other except
> maybe their close allies, who became myth when the realms were sealed. The gargoyles themselves
> have no knowledge of what happened between them going into topor and coming out of it.

**Q53 — Who is the vampire woman, and why destroy her own side's safeguard?**

> They are all part of the Guardians of Night - who themselves are being manipulated by an ancient to
> start trouble with other factions. From the perspective fo the Guardians of Night the recent
> unsealing of some of the gates is proof that the Celestials, Fey Folk, and Mystics intend to invade
> their realms again. We haven't discussed them much yet, but the Mystics are under invation by the
> Damned mostly and some werebeasts too. This too has been instigated by the Guardians of Night. Her
> name is Val (short for Valynthia).

**Q54 — Why does an offensive war wake a defensive construct, and what is the bolt?**

> The bolt of power is magic the Gargoyles themselves imbued into the barriers they constructed -
> they are awoken from their topor when a barrier is broken. The gargoyle won't know what's happening
> but will slowly uncover the manipulation of the green-skins and see this manipulation as an act
> that counts as external forces attacking the green skin realm.

**Q55 — Are the other realms' gargoyles still standing?**

> The Damned gargoyles have also been smashed - in a similar plot where the Damned are leading an
> invastion into the Mystics realm now. There werebeasts haven't had their gargoyles smashed and
> their barriers are in place. This makes for a future plot line in a much later chapter where the
> Gargoyle will attempt to seek the other gargoyles for help, something he will have to be convinced
> to do by one of the other protagonists as he is mainly focused on the Green Skins and would see
> this as getting involved in other faction conflicts.

**Q56 — What does he not know?** (recommendation: he knows the factions, and has never heard of the
Ancients)

> Agreed. He doesn't know why he is damaged and the other gargoyles around him are destroyed, even
> though the player does as he was privy to the cut-scene.

**Q57 — What are the lore fragments?** (recommendation: pieces of his own smashed head)

> The lore fragments are pieces of other gargoyles that he can use to restore himself. When he
> awakens there are other smashed gargoyles in the same room. When he comes to he can barely move but
> finds some of his own fragments that restores him somewhat. As he is inspecting the other gargoyles
> he finds another fragment that grants him the first gargoyle power to stealth without moving. His
> head looks damaged still, and while gargoyle's are very rare they are scattered around the
> green-skin realm in important places. All have had their heads smashed, and some have fragments
> that the gargoyle can use to recover.

**Q58 — Are the other gargoyles still physically there?**

> agreed.

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
- Round 9 corrected a real contradiction: the shrine mini-fix bot was described as "woken" by the
  first signal while also being the reason the Ninja survives non-boss failures. It has been
  **awake for generations**; the quest was renamed `the-first-signal` and the bot promoted to a
  `character` note, `the-shrine-mini-fix-bot`, as the Ninja's companion and mentor.
- Round 9 also settled the second signal's **route** (realm-03 → open gate → realm-09 → cracked
  ruin gate → realm-01), which had been recorded as the interviewer's inference, and confirmed the
  monastery bot is a **mini-fix** bot.
- Round 10 named the shrine bot **Mifix** and gave him a motive: he believes he may be the last
  robot with autofix capability, and the Ninja's family line carries a **legacy to reunite the
  allied factions** — but his memory is corrupted and the reasons have decayed into myth.
- Round 10 resolved the timing discrepancy with a three-condition gate, named **Quantum Comms** as
  the Autofix skill-tree unlock, and established that the guarded gate is **not** cracked all along
  — it cracks when the Ninja returns to the boss battle with a newly trained skill (TBD).
- Round 10 also produced a `character` note for **the Gate Guardian**, settling three competing
  names for it (gate guardian / gate warden / Gate Boss).
- Round 11 closed the last open mechanism question. The crack is a **transmission** problem, not a
  reception one: realm-02 is sealed on every side, Quantum Comms cannot operate without an opening,
  and the crack is the only hole in that seal. Autofix's signal escapes through it and reaches
  **both** mini-fix bots, which is why the crack gates the second signal too.
- Round 11 also gave `the-second-signal` its motive: Mifix and the Ninja pursue the faint signal as
  an **alternative route to the Robot Realm**, the guarded gate being cracked but impassable until
  the Gate Guardian falls.
- Round 12 built out the Robots' systems into three notes: `autofix-skill-tree` (one tree, five
  branches, with a comms ladder that changes the genre as it grows), `minibot-command` and
  `robot-repair-puzzle`. Quantum Comms was reframed as a **local** ability; the cross-realm signal
  is an accident.
- Round 12 established that mini-fix bots are **autonomous** — Autofix can communicate with them but
  not control them — and that the distant bots are **detectable but not reachable**.
- Round 12 proposed a reveal: the Templar's mini-fix bot has **uncorrupted memory** and can restore
  the Robot Realm's lost history. It needs a name and its knowledge needs deciding.
- Round 13 renamed skill points to **Data Fragments** and reframed unlocks as **rediscovery** —
  Autofix has no schematics and is researching the robots' lost technology from data recovered from
  the machines he repairs.
- Round 13 named the monastery mini-fix bot **Odie** (designation MF-710D / MF-28941, known to the
  Celestials as the Relic of St Archivus) and promoted it from an `item` to a `character` note.
  Established that **mini-fix and autofix bots cannot repair themselves**, which is now its own lore
  note and explains Mifix's corruption, Odie's stand-by, and the faction's whole predicament.
- Round 13 added the **`ACCESS DENIED`** block on autonomous robotics, and **proposed a chapter
  restructure**: chapter two refocused on Gargoyle's gameplay, with the Mystics and the four-way
  convergence at the Templar moved to a new chapter three. Recorded as provisional.
- Round 14 settled the **green-skins' game style**: `gargoyle-stone-metroidvania` — the Ninja's
  platforming engine, a different move set, no rhythm layer, Metroid-structured, with a ten-rung
  ability ladder running from stationary-only stealth to sonic flight.
- Round 14 established that the **Gargoyle does not fight at all** — he is a protector — and that
  the green-skins are **being manipulated and used**, which is the first stated reason for the
  faction's expansion and the strongest lead yet on the antagonist. The lore behind it is
  **deliberately deferred** to a dedicated session; do not invent who is using them.
- Round 14 produced a structural rule with wide reach: **`realm-governs-game-style`** — a genre
  belongs to a realm, not a protagonist. The Ninja plays a Metroid in realm-09; both he and the
  Gargoyle play tower defence in realm-03 in chapter three. This turns ten one-shot genre systems
  into systems that get played repeatedly, and is the main mitigation for the project's central
  scope risk.
- Round 14 **rejected party/squad mechanics for the Gargoyle** — as unsuited to the realm, not as a
  bad idea. The author reserved them for a different faction.
- Round 14 also rejected the interviewer's Q49 recommendation (failure cracks him and costs an
  ability): failure costs **position**, not capability — back to the start of the section.
- Rounds 15–16 built out the **Gargoyle's lore** across six new notes. Gargoyles are dead orcs
  resurrected as stone constructs (`the-gargoyle-guardians`), made jointly by realm-08 necromancers
  and realm-09 shamans, autonomous so they could never be used offensively, and able to act only in
  defence of an invaded realm.
- Rounds 15–16 **resolved the sealing contradiction** the wiki had carried since round 1. There are
  **two layers**: the Ancients built and locked the *gates*; the gargoyles shaped *barriers* on the
  inside of them (`the-realm-barriers`), imbued with their own magic, so that breaking a barrier
  wakes them. The green-bloc realms sealed themselves in; the Ancients only had to keep them there.
- Rounds 15–16 introduced **the Guardians of Night** — a secret cross-realm group who smashed the
  gargoyles of realms 08 and 09, broke the Celestial barrier from the inside, and let three realms
  believe they were defending themselves. They think they are defending too. **They are being
  manipulated by an Ancient** — the eleventh faction's first action in the *present day*, and the
  game's first reachable antagonist. `val` (Valynthia), a vampire of the Damned, gave the order.
- Round 16 **softened the disconnection**: awareness of other realms is a spectrum, not a blackout,
  and the old allies of realms 07/08/09 remember each other better than most. Recorded in
  `the-long-disconnection`.
- Round 16 turned the "lore fragments" into `gargoyle-fragments` — **pieces of other gargoyles**,
  found at important places across realm-09, all with their heads smashed. Progression, exposition
  and grief are one object.
- Round 16 gave four "thin — leave" factions a **role derived from someone else's story** rather
  than invented: the werebeasts and the Damned as old defensive allies (the werebeasts' gargoyles
  survive, setting up a much later chapter), the Mystics as a second invasion front, and the Fey
  Folk as one of the three old invader realms. Their protagonists and game styles remain untouched.
- A **fourth source** was ingested 2026-08-16: `labs-faction-classes.md`, scraped from an older
  website the author built. It supplies the **complete 10x6 faction-class matrix** and confirmed
  three things the interview had left open — the minotaur and the giant are green-skins, `val` is a
  Vampire (the Damned's Commander class), and the gargoyles' makers (Necromancer, Shaman) are both
  their factions' **Medic** class. It also corroborated the green-skins' subjugation independently.
  One conflict surfaced and was **resolved the same day by the author: the Templar is the
  Celestials' Commander**, and the factions-retro readme's "Front Liner" is superseded. **Knight**
  turns out to be a *separate faction class* of the same faction — their Front Liner — which also
  explains the round-1 wobble where the author said "Knight" and the prototype said "Templar".
- Still outstanding: the game style for `mystics` (leads chapter three, scheduled for a dedicated
  session, now the only chapter lead without one); the green-skins' **culture and leadership**;
  why realm-07's gargoyles were spared; whether "an Ancient" means an individual;
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
