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

### Round 17 — 2026-08-18

**The author opened by presenting the eleventh faction and the primary antagonist story in full,
unprompted.**

> The Eleventh Faction are not very well known - any lore about them includes that they are ancient
> so they are often just called 'The Ancients'.
>
> What they really are are a pantheon of gods in the style of the Aztec gods. The main four gods are
> the Tezcatlipocas:
>
> - Tezcatlipoca, creator god, lord of darkness, lord of the night, god of battles, and the lord of
>   the North. Tezcatlipoca is also known as the "Smoking Mirror". Tezcatlipoca is the old
>   arch-nemesis of Quetzalcoatl. (Black Tezcatlipoca)
> - Quetzalcoatl, god of the life, the light and wisdom, lord of the winds and the day, and the lord
>   of the West. Quetzalcoatl is the old arch-nemesis of Tezcatlipoca. (White Tezcatlipoca)
> - Xipe-Totec, god of agriculture, fertility, seasons, metalsmiths, and disease, and the lord of the
>   East. (Red Tezcatlipoca)
> - Huitzilopochtli, god of war, human sacrifice, bloodletting, and the lord of the South. (Blue
>   Tezcatlipoca)
>
> These four gods are also known simply as The Black, The White, The Red, and The Blue.
>
> The Black creates reality, let's it run it's course until it causes it's own destruction. He then
> re-creates reality from the destruction, making changes to the creation so each iteration improves
> on the last. The Blue supports the Black, and is focused on forced evolution through conflict, but
> resents the loss of progress that occurs through total destruction.
>
> The White tries to subvert the Black by attempting to bring order to reality, pushing back against
> the chaos and entropy. The Red supports the White and is focused on growth and the spread of life
> over non-life, but resents the lack of change and stagnation of life that The White pushes for.
>
> In this iteration of reality takes the form of ten different realms. These realms were not
> connected for thousands of years. This reality was more stable than previous realities, and the
> cycle of creation and destruction was stalled. The Black decides to intervene, forming pathways
> from each realm to every other realm. This rapidly moved reality towards total destruction due to
> the conflicts that arose between the factions.
>
> The Green Skins and Werebeasts started many of the cross-faction conflicts. The Damned would
> leverage the chaos to steal dead bodies to take back to their realm for reanimation, and the
> Vampires would build their ranks by turning inhabitants of other factions.
>
> Over time the Fey Folk, Mystics, and Celestials formed an alliance and started pushing back. The
> Green Skins and Werebeasts especially were not co-ordinated in their incursions - they were more
> raiding and pillaging than fighting a war. This turned the tide greatly. The Vampires of The Damned
> proposed working with the Green skins to create the Gargoyles to push back the enemies and seal the
> gates from their side.
>
> Inspired by the success of the Gargoyles, The White and the Red decide that the Inhabitants of
> Reality themselves are pushing for survival and deserve stability. They convince the Blue that the
> inhabitants deserve their existence as the realms were originally created - disconnected from each
> other - which will stay the destruction of reality while the factions will continue to evolve
> through internal conflict within each realm.
>
> The power of the three combined is what causes the gates to seal. The conflicts did cause great
> change and entropy, so instead of pushing back against the other three The Black decides to let
> reality run it's course with the realms closed from each other for a thousand years.
>
> Initially the realms flourish, but over time some realms begin to suffer. The robot realm falls to
> entropy and loss of life as the Robots lose the ability to fix themselves, The fey folk avoid all
> change and stagnate, The mystics lose motivation to innovate and progress. The Damned can't
> pro-create as they relied on the dead of other factions to grow their ranks, so they slowly lose
> numbers. The Werebeasts and Green Skins never progress due to too much in-fighting.
>
> The Red becomes unhappy with the status-quo and acts to intervene in two ways: encourage and imbue
> the Ninja and a Vampire to breach the gate to their allies (the Robots and the Aliens for the
> Institute of Eight, and The Green Skins and Werewolves for The Damned).
>
> The White becomes aware of The Red's intervention too late to stop The Damned, but is able to
> create Gate Guardians in the Ninja's realm to guard the Alien and Celestial gates.
>
> The Blue, seeing the intervention of The Red and The White, decides to intervene as well. He renews
> his alliance to The Black and influence the creation of the Guardians of Night - a secret alliance
> of Green Skins, Werebeasts, and The Damned who are motivated to reignite the old conflict with the
> Mystics, Celestials, and Fey Folk. This leads to the destruction of almost all the Gargoyles and
> the Gargoyle-created barriers between the Green Skins and the Celestials, and the Werebeasts and
> the Mystics.
>
> The Guardians of Night then blame the destruction on the Celestials and Mystics, and manipulate
> their allies to invade the Celestials and Mystics realms. The Damned are afraid of the Fey Folk and
> so keep that barrier sealed.

**The interviewer put nine questions**, on: humans vs gods; which god is "an Ancient"; what the Gate
Guardian holds; whether the Red's imbuement costs the "crack made by losing" beat; which barriers
broke; the Lovecraftian void gods; the timeline of the three interventions; whether the pantheon
extends past four; and whether this answers the Ancients' motive.

### Round 18 — 2026-08-18

**The author's answer, opening with the reveal the whole design turns on.**

> The eleventh faction in-game lore is they are four gods. Which god is 'right' is intentionally
> ambiguous. Is 'The Black' right and reality should be destroyed and recreated, ultimately leading
> to better realities? Is 'The White' right and have the inhabitants of the realms earned their
> continued existence if they can avoid mutual self destruction?
>
> The real mystery is the four gods are actually four software developers building computer games.
> faction-eleven is actually a collection of computer games developed by an indie game development
> company. One of the developers 'The Black' decided to connect all the games together but this
> causes crazy side effects so the other three devs decide to shut down the links between the games.
> The games seem to go back to normal but over time all the games start having problems so 'The Red'
> decides to sneak in a code change encouraging some of the game protagonists to unblock access to
> compatible games (in-game this means their allied realms). He adds code to the Ninja and a Vampire
> Val that allows them to unseal realm gates. 'The White' dev gets a notification that computer
> characters are showing up in the wrong games - does some diagnostics and discovers the Damned gates
> to the Werebeasts and Green Skins realms are now unsealed. He checks the change history to uncover
> what 'The Red' did and decides to add his own code change to add 'bosses' to guard the ninja's
> allies gates. This causes the ninja game code to retcon the lore around the gate boss. 'The Blue'
> realises what's been going on and decides to join in the fun too and develops his 'Secret Society
> System' - which leads to the 'Red Power Imbued' vampire forming the Guardians of Night.

Answers to the round-17 questions:

- **Q2 (which god is "an Ancient"):** "Agree" — The Blue.
- **Q3 (the Gate Guardian / timeline):** "Agree - the institute punishment lore is the game trying to
  incorporate the code changes into the game system and lore."
- **Q4 (the Ninja's imbuement vs the crack):** "The boss is guarding the gate but the Ninja has been
  'imbued with red power' ... he failes the battle multiple times but keeps trying. In one of these
  battles he attacks the boss with the red power. It doesn't hurt the boss but it does crack the gate
  - it's only a crack because the Ninja wasn't attacking the gate directly."
- **Q5 (which barriers broke):** "Agree" — the wiki's arc-mirror stands; the Werebeasts' barrier
  facing the Fey Folk is the intact one, spared because the Damned fear the Fey Folk.
- **Q6 (the Lovecraftian void gods):** "'The Black' software dev is inadvertantly behind this. He has
  been playing with AI and added liches to The Damned game that are driven by AI. This gives the
  liches the ability to bypass game rules, and they hacked their way out of their game, into the
  network (the void) and have been stealing alien game content for use in their own game. They have
  been hiding their tracks so none of the devs know it's going on."
- **Q7 (timeline):** "Good catch - I answered in Q3 but I feel it's a little weak so needs to be
  handled carefully. I think this will be represented as glitchy in-game - it's a way that the devs
  interfering in the game breaks game lore and continuity. I like your suggested solution to adjust
  timing here, and the lore of time for the devs / gods doesn't need to align with the games timeline
  is confirmed."
- **Q8 (does the pantheon stop at four):** "Agreed, There are other gods because there are other
  employees and other humans, but the four are the ones that matter."
- **Q9 (is this the motive):** "Agree - and that answer works very well with the Black dev's
  motivation."

**The interviewer put eight further questions**, on: the retcon engine and its failures; the Ancient
Language as machine-readable data; what lives in the void; whether characters are sentient; whether
the dev layer is ever seen directly; lead-dev assignment and "compatible" meaning shared engine; what
destruction means in studio terms; and whether anything sits above the four.

### Round 19 — 2026-08-18

> I basically agree with all your answers. The Black wants to rebuild and move on but The White loves
> the games they created and wants to keep the games as they are. The Blue and Red want to make
> improvements but disagree on what improvements to make. I agree for now with some dev's being more
> invested in some realms but I'd couch it as they were the lead dev on those games, and all devs
> have worked on all games.

**The interviewer put seven questions**, on: what the Red and Blue are arguing about; lead-dev
assignment and design signatures; whether the White knows he broke his own principle; where the two
reveals land against chaptered release; whether the player chooses which dev is right; the four
factions with no decline written; and whether there is a diegetic player.

### Round 20 — 2026-08-19

- **Q1 (Red vs Blue):** "Agree" — Red is content and connection, Blue is systems and pressure.
- **Q2 (lead-dev assignment and design signatures):** "Agree."
- **Q3 (does the White know he broke his own principle):**

> It's not just white's changes that breaks things. When black connected the games together it lead
> to over half the games developing issues, some of which have continued to be broken like the Robots
> game. White is trying to add protections to the game to stop other code from other games getting
> into the games he cares about and breaking them further. We have already agreed that glitches and
> continuity errors that the player can notice are hints to the true nature of the game, so more will
> be added. Agree that no change causes the games to atrophy too - they need patching and new
> content. Agree that White's position that the characters and games deserve to keep existing he's
> just going about it the wrong way is sympathetic to the player and an emotional hit worth keeping.

- **Q4 (where the reveals land):**

> Agree - the game morphs from characters in indivitual games trying to progress in their individual
> games into the characters in the game uncovering the motivations of the gods and realising they
> need to unite all factions and achieve a lasting balance to prove to the gods that they deserve to
> exist. They should come to realise that no single god is completely right and none are completely
> wrong. Proving this to the gods in the game lore will also change the minds of the devs - leading
> the devs to agree on a new path forward that leads the company to success. The characters in the
> game need to both align with the real goal of the gods (make good games, make their company
> succeed) with the gameplay in the game. I'm thinking there will be 8-10 chapters. I was thinking
> one chapter per faction and then a final chapter but now I believe multiple faction story arcs will
> progress in individual chapters, and protagonists will participate in each other's games earlier
> than I originally planned.

- **Q5 (does the player choose which dev is right):** *The interviewer's recommendation — a player
  choice the game refuses to grade — was rejected.*

> How the main plot plays out is on rails - it's more a story the player plays through - the
> protagonists in the game should always come to the conclusion outlined in Q4.

- **Q6 (the four factions with no decline written):** *The interviewer's four proposals were largely
  rejected.*

> Not every game needs a decline from the games being networked together. The pirates game benefited
> from the networking but went back to normal after, though the economy was skewed from trade goods
> of other realms that can no longer be supplied. The other three games (aliens, celestials, institute
> of eight) were all mostly fine after the links between realms were closed. There were some glitches
> still in the lore of the Institute of Eight but the lore keeps adjusting automatiaclly to fit. The
> aliens game is now suffering due to the liches interference but this is a recent development.

- **Q7 (is there a diegetic player):** "Agree" — no. The four are the top of the ladder.

## Notes For The Compiler — Rounds 17–20

- **The eleventh faction is now settled at three layers**: the ten factions remember nothing; the
  discoverable in-game truth is four gods; the real truth is four software developers at a struggling
  indie studio, and the ten realms are ten games.
- **The wiki's oldest claim was right for the wrong reason.** `faction-eleven-antagonist` said "the
  Ancients are humans... the thing behind it all is us". That survives intact at the bottom layer.
- **Two blocking gaps in `story-outline-requirement` are now closed**: the Ancients' motive, and the
  shape of the ending.
- **Rejected this session, do not re-propose**: a mortal servant caste for the gods; a player-facing
  choice of which god is right (the plot is on rails); a diegetic player above the four; declines for
  the Celestials, Aliens and Institute caused by the sealing; the Pirates' decline as a closed 4X
  economy (they benefited from the linking and merely lost their trade goods after).
- **Still open**: the studio's off-screen commercial pressure in specifics; what a glitch concretely
  looks like in each settled genre; whether the Ninja ever learns what he is; and the chapter
  restructure to 8–10 chapters with multiple faction arcs running per chapter.

### Round 21 — 2026-08-19

**The author revised the Red and the Blue's motivations, unprompted.**

> I have an update on The Red and The Blue - want them to have better motivations as devs that can be
> reflected in their representation as gods in the game. The Red and Blue represent a different common
> developer problem - The Red wants everything perfect before she does anything - she likes making
> big, elegant but complicated systems. They suffer from 'polishing the rock' and never shipping soon
> enough because they are a perfectionist that also scope creep. The Blue is the opposite, not testing
> enough and making big sweeping changes with little thought or care on the impact and potential
> side-effects. The Red gets more done but at the cost of quality. Neither are terrible developers,
> but that is where they fall on the quality vs velocity spectrum. They are both best when they can
> work together. The Red and The Blue are regular devs, while The Black and The White are senior
> developers. The Red is female while the other three are male. The Red and The Blue are younger, in
> their late 20's while the Black is in his late 30's and the White is in his late 40's. Their colours
> are represented in their avatars used in their game dev, but also their avatars in the game and the
> snippets of lore and 'real world' leaking in to the game that the characters in the game can come
> across.

**Interviewer's note on one ambiguity, flagged to the author and compiled on the coherent reading:**
the sentence "The Red gets more done but at the cost of quality" describes the **Blue** everywhere
else in the paragraph — the Red is the perfectionist who does not ship, the Blue is the one making
sweeping untested changes. Compiled as *the Blue gets more done at the cost of quality.*

## Notes For The Compiler — Round 21

- **This supersedes the round-19/20 axis for the Red and the Blue.** "Content and connection versus
  systems and pressure" is replaced by **quality versus velocity**, which is a real and common
  developer failure pair rather than a design-philosophy disagreement.
- **Seniority is new and load-bearing.** The Black and the White are senior developers; the Red and
  the Blue are regular devs. This is why the two younger ones **sneak changes in rather than
  proposing them** — they do not have the standing to argue. The theology's "the Red supports the
  White, the Blue supports the Black" is office politics.
- **The Red is female; the other three are male.** Existing notes referred to the Red as male and
  are corrected.
- **Ages:** Red and Blue late 20s, Black late 30s, White late 40s.
- **"They are both best when they can work together"** is the mechanism of the ending: the resolution
  is not one god winning but the four resolving into a team that functions.
- **Avatars are a third evidence channel**, alongside the Ancient Language and continuity glitches:
  each dev's colour appears in their avatar at work, in their avatar inside the games, and in
  snippets of lore and real-world material leaking in that the characters can find.

### Round 22 — 2026-08-22

**The author corrected the nature of the pressure on the studio**, revising the round-19 answer that
had accepted off-screen commercial pressure.

> The pressure on the company is more that the games are becoming unstable and the developers are
> fighting about the solution to the point where they may break up the company. The devs are friends
> and developed the games and put the company together themselves. Tension over the problems with the
> games, disagreements on how to solve technical problems, and what's best for the company. I don't
> want 'real world' business issues being part of the story - focus is the devs as a friend group
> dealing with their challenges, and the player progressing the story helps the devs sort out their
> problems.

## Notes For The Compiler — Round 22

- **This supersedes round 19's Q8 answer.** "Commercial pressure, off-screen and never personified"
  is withdrawn. There are no publishers, funding cliffs, deadlines or business problems anywhere in
  the story.
- **There is now genuinely nothing above the four.** They founded the company themselves and built
  the games themselves. The ladder does not merely stop at four — there is no rung above them to
  stop at.
- **The four are friends**, not colleagues. The stakes are the friendship and the thing they made
  together, not the business.
- **New fact: the games are becoming unstable**, and worsening. The pressure is technical, and the
  fight is about how to fix it. This is a stronger stake than atrophy, which was the previous
  account.
- **The threat is the group breaking up.** Everything the player does that moves the story helps the
  four sort their problems out.
- Compiler inference, flagged as such: worsening instability is the in-fiction reason the rate of
  continuity glitches should climb across the chapters.

### Round 23 — 2026-08-22

**The author refined the four's relationship**, correcting the interviewer's extrapolation that the
Black and the White's enmity was a friendship that had already soured.

> They are all friends that met through work or study. Their approaches to their work differs and
> once the stakes go up (the games they care about are becoming unstable, the company they built
> could go under, their friend group could break up) the pressure goes up. The solution is comprimise
> and collaboration - leverage their differences to balance their approaches and solve their problems.
> They succeed together or the company and their friendships will fall apart.

## Notes For The Compiler — Round 23

- **Corrects round 22's compiled inference.** The Black and the White's enmity is **not** a
  historical falling-out. They are all still friends. The differences in approach were always there
  and were never a problem; **rising stakes turned difference into conflict.** Present-tense pressure
  on a live friendship, not the aftermath of one.
- **How they met:** through work or study.
- **Three stakes, escalating, all internal:** the games they care about are destabilising; the company
  they built could go under; the friend group could break up. The company failing is a *consequence*
  of the other two, not an outside business problem — consistent with round 22.
- **The solution is compromise and collaboration:** leverage their differences to balance their
  approaches. **Their differences are the solution, not the problem.**
- **It is all-or-nothing:** they succeed together, or they lose both the company and the friendships.
- Compiler note: this makes the two layers of the story say the same thing. In the fiction, ten
  factions must unite and hold a balance, and no single god is wholly right. Underneath, four friends
  must compromise and use what each is good at. The protagonists' solution *is* the developers'
  solution — which is the convergence round 20 asked for, now structurally exact rather than
  thematic.

### Round 24 — 2026-08-22

**The author set out how the revelation is staged, and corrected the Black's and the White's
motives.**

> The player sees the game through the eyes of the characters in the game. Characters in the game
> interpret the devs actions and interactions through the game as the actions of gods. The
> revelations come slow - first it looks like two gods fighting and two other gods switching
> alliances. The slow revelation of this is devs working against each other and arguing over problems.
> The motivation of all gods appear simple and malevolant or protective at first, but it's slowly
> revealed that there is more nuance. The Black didn't actually link all the games without consent out
> of spite - he succeeded in arguing for the change because the games had become stagnant and
> connecting them was a way to liven up gameplay. When things became unstable The White argued
> successfully for the links between games to be closed as a way to stabilise the games. Things
> persisted that way for a while but over time the impact of the instability and stagnation issues
> both increase and the devs are all arguing about it (reflected in the game as the gods are fighting)
> until the Red sneaks a small change into the code base (granting the Red Power to the Ninja and
> Liv), which is the catalyst to the Blue making his changes.

**Interviewer's note on a name, flagged to the author:** "Liv" does not appear elsewhere in the
material. The Red-imbued vampire is established as **Val** (Valynthia) from round 18 onward, and the
description matches exactly. Compiled as Val pending confirmation.

## Notes For The Compiler — Round 24

- **Corrects the compiled account of the Black's and White's authority.** Neither acted unilaterally.
  **The Black argued for linking the games and won**, because the games had gone stagnant and
  connecting them was a way to liven up gameplay. **The White argued for closing the links and won**,
  as a way to stabilise them. Two legitimate, agreed decisions — not seniority overriding anyone.
- **The Red's sneaked change is therefore the first illegitimate act in the whole history**, and the
  **catalyst** for the Blue's. The process worked until it didn't; her commit is where it broke.
- **Both problems compound.** After the sealing, instability *and* stagnation both keep getting worse
  over time. The sealing did not fix the instability, it only stopped it spreading.
- **The devs arguing about it is what the realms see as the gods fighting.** The correspondence is
  direct and is the mechanism of the whole mystery.
- **Perception model:** the player sees everything through the eyes of characters inside the games,
  who interpret dev actions and interactions as divine acts. There is no outside view.
- **The revelation is staged and slow, on two ladders at once:**
  - *Identity* — two gods fighting and two switching sides → four gods in a four-way argument → four
    developers working against each other.
  - *Motive* — simple, malevolent or protective → nuanced, and every one of them trying to help.

### Round 25 — 2026-08-22

**Name confirmed.**

> Confirm that Liv is Val - I got the name wrong.

The round-24 "Liv" was a slip. The Red-imbued vampire is **[[val]]** (Valynthia), as compiled. No
compiled note ever carried the wrong name.
