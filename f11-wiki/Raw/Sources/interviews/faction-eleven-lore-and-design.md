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

### Round 26 — 2026-08-24

**The author supplied the studio's founding story and the two seniors' craft profiles, unprompted.**

> Some more background on the devs: The Black developed an open world, persistent game system that
> evolves it's own gameplay, but he couldn't get it stable, The White helped make the system stable
> and they started making game worlds, hiring two devs (The Red and The Blue) to contribute new
> worlds of their own. The Black and The White have their own balance - The Black is an early
> adopter, tinkerer, and loves playing with the bleeding edge. He starts many projects but has
> trouble stabilising his experiments and finishing them. The White is the opposite - learns
> technologies and patterns deeply and sticks with known and well understood approaches. The White is
> also great at deep-diving into implementations, understanding them deeply and course-correcting
> architecture. The White's drawback is he is slow to change, slow to adopt new technology and new
> approaches. The Black has the ideas but can't bring those ideas through to completion, The White
> wouldn't come up with the idea in the first place, but can take complicated ideas and design and
> plan their implementation successfully.

**Interviewer's note, flagged to the author:** this revises the compiled claim that the **four**
founded the studio together. Compiled notes currently state "four friends who met through work or
study and built this themselves" and "the four founded the company themselves". On this account the
studio has **two founders and two hires**. Compiled to the new account; what the Red and the Blue's
*stake* is, and whether "the four are friends" (rounds 22–23) survives the employment relationship,
is left open rather than assumed.

## Notes For The Compiler — Round 26

- **The studio has a founding story.** The Black built an **open world, persistent game system that
  evolves its own gameplay** and could not stabilise it. The White stabilised it. Only then did they
  begin making game worlds on it.
- **The Red and the Blue were hired**, to contribute new worlds of their own. This explains the
  seniority table rather than contradicting it — but it does revise "the four built this together".
- **The two seniors have a craft axis, not only a product argument.** The compiled note says the
  seniors argue about the product and the juniors about craft. The seniors are *also* a craft
  complementarity, and it is the older one:

  | | The Black | The White |
  |---|---|---|
  | Adopts | early — bleeding edge, tinkering | late — known, well-understood approaches |
  | Learns | by playing with it | deeply, patterns first |
  | Strength | has the ideas | deep-dives implementations, course-corrects architecture, plans complicated ideas to completion |
  | Fails by | starting many things, stabilising and finishing none | slow to change, slow to adopt |
  | Net | would never have finished it | would never have started it |

- **The pattern repeats.** *Interviewer's inference, not the author's:* the founding is the linking
  and the sealing in miniature — the Black makes something unstable, the White makes it stable. The
  same two moves, twice, a company apart.
- **Candidate connection, unconfirmed:** a system that "evolves its own gameplay" may be the
  mechanism behind the retcon engine and the lore that "keeps adjusting automatically to fit"
  (round 20). Not asserted; a question for a later round.

### Round 27 — 2026-08-24

**The author resolved both questions the interviewer left open in round 26.**

> Lets resolve what you raised:
>
> - The retcon engine is a system The White introduced to stabilise the realms after they were
>   linked. A different system The White introduced to stabilise the original persistent
>   self-evolving world engine developed by The Black was The Continuity System, which tracks the
>   world evolution into key continuity events and rejects any continuity-breaking events.
> - The Red previously worked with The White and they became friends. The Black previously worked
>   with The White and The Blue and also became friends. When The Black and The White decided to go
>   into business with each other they approached The Red and The Blue to join them, they offered
>   The Red and The Blue to invest in the company and have some ownership, which they agreed to.

## Notes For The Compiler — Round 27

- **The round-26 candidate is wrong, and the real answer is better.** The retcon engine is **not**
  the Black's self-evolving engine. It is **the White's**, introduced to stabilise the realms
  **after the linking**. Correct the unconfirmed section in `the-retcon-engine`.
- **A second, earlier system is named: The Continuity System.** Also the White's, introduced to
  stabilise the Black's original persistent self-evolving world engine — so it **predates the game
  worlds**, where the retcon engine postdates the linking. It **tracks the world's evolution into
  key continuity events, and rejects any continuity-breaking events.**
- **The White therefore has three stabilisation layers**, built at three different times, all on the
  Black's engine: the Continuity System (founding), the Retcon Engine (post-linking), and the gate
  guardians (recent, round 20 — "protections to stop other code from other games getting in").
- **"Continuity glitch" becomes diegetic rather than descriptive.** There is a system whose stated
  job is rejecting continuity-breaking events. A continuity glitch is that system failing, being
  bypassed, or being overruled — which is a mechanism the compiled notes have never had.
- **Friendship topology, and it explains the alignments.** White↔Red were prior colleagues and
  friends; Black↔White were prior colleagues and friends; Black↔Blue were prior colleagues and
  friends. The compiled claim that the Red stands behind the White and the Blue behind the Black
  "because they are easier to stand behind" now has a cause: **they knew each other first.**
- **The Red and the Blue are owners.** They were *approached*, offered the chance to **invest in the
  company and take ownership**, and agreed. Corrects the round-26 compiled line that they work in
  "a company that was not theirs" — it is theirs, and they put their own money into it.
- **This closes the open stake question.** All three stakes (the games, the company, the friendship)
  apply to all four. Their position is **ownership without seniority**: they bought in, on an engine
  they did not build, and are still the two who did not feel able to argue.

### Round 28 — 2026-08-24

**The author explained why the Continuity System failed at the linking, and reframed the guardian.**

> A bit more detail - the continuity engine worked while the systems were disconnected because it
> would stop continuity errors from occurring, the problem was that once the worlds were connected
> the continuity that already existed in those worlds couldn't be consolidated - hence the need for
> the retcon system to retroactively change continuity to force consolidation. The White building a
> gate guardian is a sign of his frustration - he is making a change to protect the world he built
> from impending failure as a quick mitigation, buying time to push for a longer term fix.

## Notes For The Compiler — Round 28

- **Corrects the interviewer's round-27 guess at why prevention stopped working.** The compiled note
  said the Continuity System could not refuse the gods' own edits. That is **not** the reason. The
  reason is that **there was nothing to reject**: the system prevents continuity errors *as they
  occur*, and it worked perfectly while each world was disconnected. What the linking created was not
  a new breaking event but **ten already-established, individually valid continuities that now had to
  be one** — a contradiction that had already happened, retroactively, the moment the worlds became a
  single continuity space.
- **The retcon engine's purpose is therefore consolidation**, not merely covering individual divine
  edits. It **retroactively changes continuity to force ten histories into one**. Covering a god's
  edit is a case of that job, not the whole of it.
- **This mechanises the second half of the deferred glitch-causation brief** — "different lore trying
  to reconcile into a single narrative" is exactly this system, and the glitches are where the
  forced consolidation has not succeeded.
- **The gate guardian is a stopgap, and reads as frustration.** The White is protecting the world he
  built from **impending failure**, as a **quick mitigation**, to **buy time to push for a longer
  term fix.**
- **Two consequences for the White's characterisation:**
  - He is **not "arguing for nothing"**, as the compiled note has it. He is arguing for a proper
    long-term fix and shipping stopgaps to buy the time to get it.
  - *Interviewer's inference, not the author's:* his three layers are a **degradation curve** — a
    deep architectural system, then a violent retroactive one, then an admitted hack. The man whose
    whole method is depth and well-understood approaches is now shipping quick fixes with unexamined
    side effects, which is the failure mode the compiled notes attribute to the Blue.

### Round 29 — 2026-08-24

**The author supplied the retcon engine's operating model — and with it, the cause of the glitches.**

> The retcon system can only apply a retcon when a continuity error is detected - and the brute
> forcing of changes to existing history is a cause of glitches and instability, especially when a
> retcon fix can cause new continuity errors that can't be foreseen due to incompatible histories
> across so many realities. The retcon system can sometimes apply a change that fixes the immediate
> problem but cause more continuity issues because it can only deal with the continuity issue
> detected - it can't have full scope of every realm history when it determines a retcon change to
> apply.

## Notes For The Compiler — Round 29

- **The engine is reactive, not systematic.** It cannot consolidate the ten histories as a project.
  It can only act **when a continuity error is detected**, and then only on that error.
- **Its scope is local and the problem is global.** It does not have — cannot have — the full scope
  of every realm's history when it chooses a retcon. So it fixes what it can see.
- **The repair is itself a cause of damage.** "Brute forcing changes to existing history" causes
  **glitches and instability** directly, and a fix can seed **new continuity errors that cannot be
  foreseen**, because the histories across so many realities are incompatible.
- **This is a cascade, and it is the mechanism the design has been missing.** Detect → patch locally
  → the patch contradicts something out of scope → detect → patch again. The system that was built to
  end contradictions is a **generator** of them.
- **It answers the standing question of why instability keeps rising after the sealing.** The realms
  are disconnected and the instability still climbs, and no compiled note has ever said why. This is
  why: the engine is still running, still detecting, still brute-forcing, and every repair seeds the
  next fault. Not decay — a feedback loop.
- **It also derives a design rule the notes had only asserted.** "A realm's account of itself is
  airtight from inside and contradicts the realm next door" is no longer a rule to be observed; it
  is the necessary output of a repair mechanism whose scope is one realm at a time.
- **It answers the interviewer's round-28 question** — still running, still reactive, and
  **diverging rather than converging**.
- **Two characterisation consequences:**
  - The White's second stabilisation layer is the primary engine of the instability he is fighting.
  - The Black's "it is beyond repair, rebuild it" becomes technically correct in a specific way: the
    repair mechanism is the damage.

### Round 30 — 2026-08-24

**The author added the fixbots' code sight, and the liches' framing of it.**

> One new piece of lore - The Autofix and Minifix bots can 'fix' robots and heal the Ninja because
> their 'heal' skill actually repairs the code of the 'entity' they are fixing. A side-effect of this
> is they notice the glitches where all other characters don't notice - they act like the new
> continuity was always the way things were. Mifix notices the glitches but is self-aware enough to
> know that he can't trust his own code as he has been running for too long - Odie and the Autofix
> notice the glitches but don't understand them as they haven't been running for very long. The
> Liches are another entity that has some self-awareness due to their AI nature - but they are
> explaining the gliches and that they can leverage their deeper knowledge of the realms and
> infrastructure the games run on as their 'ancient eldritch knowledge'. There is going to be a joke
> about the 'Glich Lich' 'Liches cause gliches' at some point.

## Notes For The Compiler — Round 30

- **A heal is a patch.** The fixbots' heal skill **repairs the code of the entity being fixed**. This
  is why an Autofix can mend a robot and also heal the Ninja — a person and a machine are the same
  kind of thing to something that edits code.
- **Side effect: fixbots see glitches.** Every other character absorbs a retcon and behaves as though
  the new continuity was always the case. A fixbot reads code, so it sees the discrepancy.
- **Corrects a compiled claim.** `continuity-glitches` says protagonists mostly cannot see glitches
  and names [[gargoyle]] as *the* exception. There are now several, by two different mechanisms, and
  one of them ([[autofix]]) leads chapter one.
- **A witness ladder, and each rung has a different limitation:**
  - **[[autofix]] and [[odie]]** — notice, do not understand. They have not been running long.
  - **[[mifix]]** — notices, and is self-aware enough to know **he cannot trust his own code**,
    having run too long. Fits the compiled fact that his memory is corrupted, and
    `no-machine-repairs-itself` means he can never audit himself.
  - **The liches** — self-aware by their AI nature, and the only ones who **explain** the glitches.
    They leverage genuine knowledge of the realms and of the infrastructure the games run on, and
    dress it as **"ancient eldritch knowledge."** Not a lie so much as a costume.
- **Dormancy is a second, separate preserving mechanism**, and it already exists in the wiki: the
  Gargoyle's torpor and Odie's stand-by both keep a memory that predates the retcons. Odie has both
  mechanisms at once.
- **Planned gag, recorded as intent:** the **"Glitch Lich"** — *liches cause glitches*.
- *Interviewer's note, for design:* in-fiction witnesses are a **deniability shield**. A glitch a
  character remarks on cannot be mistaken for a bug in the real game, which makes strong-tier
  glitches safest wherever a fixbot or a lich is present.

### Round 31 — 2026-09-07

The author opened with new material: the Secret Society System's game-balance purpose, Val's
blocked three-realm invasion, the Val/Gargoyle/Minotaur confrontation, and the Ninja's
barrier-breaching power. The interviewer's questions and the author's answers follow.

**Q59 — The Werebeast gate contradiction.** `sealed-interplane-gates` states as settled fact that
Val's imbuement opened **both** the Damned's gates to the green-skins *and* the werebeasts. New
material has her unable to find a path to realm-07 at all. Which is true? (recommendation: the note
was too broad — only the Damned→Green-skins gate was actually opened; the werebeast leg was the
Red's intent, never a completed act)

> agreed.

**Q60 — Is game balance a real design goal of the Secret Society System, or emergent/unintended?**

> The Blue developed the Secret Society System to achieve three goals: Introduce interesting events
> and intrigue into a game, incite conflict, fix game balance issues by having the secret society
> have goals that rebalance the game. A Secret Society can be created automatically when the need
> for the above is detected. The elegance is the Secret Society system elegantly created the
> Guardians of Night to address issues with all three - Gargoyles are too powerful, The Damned
> faction is stagnating, there is minimal conflict.

**Q61 — Does this resolve "the Ancient's motive," the largest open question in
`the-manipulation-of-the-green-skins`?** (recommendation: yes — there was never a personal motive,
just an untested system executing its own goals)

> agreed.

**Q62 — Does the Val/Gargoyle/Minotaur confrontation close chapter two?** (recommendation: yes)

> agreed.

**Q63 — Is Val's Minotaur the same Minotaur from the original smashing?** (recommendation: yes)

> agreed.

**Q64 — What happens after the confrontation, and why does the Gargoyle go to realm-07?**

> The gargoyle doesn't let Val know, but after the confrontation with Val he begins to doubt he is
> functioning properly. The Gargoyle can help the ninja get through the gate to the Celestials,
> without the Gargoyle's help the Ninja has no chance of getting through the gate. The ninja
> encourages the Gargoyle that he may find answers by going to the Celestial realm - where the ninja
> needs to go. The Gargoyle decides to join up with the Ninja to go to the celestial realm and get
> answers as the best course of action, so agrees to work with the Ninja to get through the gate.
> Once the Ninja and Gargoyle meet up with the Templar and Odie determines the Ninja can breach
> realm barriers they form a new plan of seeking out the Gargoyle's in the Werebeasts realm to find
> answers. The gargoyle knows that breaching that barrier should awaken the Werebeast gargoyles.
> Create a handoff to grill on this event.

**Q65 — Is the Ninja's barrier-breaching power the same Red Power as his gate-unsealing ability, and
does he discover it himself or is he told?**

> it's teh same power to open / breach barriers. He doesn't discover it, Odie notifies him. It
> explains why he had the urge to attack the barrier to the robot realm - he is motivated by the
> power bo breach barriers - that's part of the 'Red Power' and why Val is motivated too.

**Q66 — Which barrier do the Mystics and Celestials open with the Ninja's help?**

> I'm thinking the Celestials and Werebeasts gate is open and the Mystics are invading the
> Werebeasts through their catacombs. The mystics will have developed magic to lock the werebeast
> gargoyles in stasis. This will be a second secret society and a third occurrance of the red's
> power. Create a hand-off for this grilling - it will be a big part of chapter three.

## Notes For The Compiler — Round 31

- **Corrects a compiled claim.** `sealed-interplane-gates` and `val` overstate the Red's
  imbuement's completed effect — narrow to the Damned→Green-skins gate only.
- **The Secret Society System has three explicit goals**, not one: narrative intrigue, inciting
  conflict, and correcting game-balance issues — and it can spin up a secret society
  **automatically** whenever it detects the need for any of them. This is a real, designed
  capability of the system itself, not something read into it after the fact.
- **The Guardians of Night is the system's first known instance**, and its elegance is that it
  answers all three goals in one stroke: the gargoyles were too powerful (balance), the Damned
  faction was stagnating (balance), and there was minimal conflict (the incite-conflict goal). The
  Blue built the capacity; the system chose the instance.
- **This resolves the design's largest open lore question** — the Ancient's motive. There isn't
  one. The Guardians of Night are the output of an unsupervised system doing exactly the job it was
  built for.
- **The Val/Gargoyle/Minotaur confrontation is chapter two's ending**, and the Minotaur in it is the
  same Minotaur from `the-smashing-of-the-gargoyles`.
- **New scene, staged in full:** Val investigates the surviving Gargoyle, confronts him, tries "the
  gargoyles are just old," fails, declares him a threat to the war plan, sets the Minotaur on him
  (a defend/dodge encounter — he has no attack), and leaves unconvinced the Minotaur wins. She
  resolves to destroy every remaining gargoyle. He hides his own doubt from her, but the
  confrontation plants it.
- **The Gargoyle's later-chapter motivation changes.** He is no longer talked into helping the
  Werebeasts by another protagonist out of persuasion alone — he goes seeking answers for himself,
  because Val's accusation is now a live doubt. The Ninja needs him to get through the
  green-skins→Celestials gate at all; the Ninja's own reason to go there is independent (finding
  Odie/the mini-fix signal). They agree to travel together for their own separate reasons.
- **The Ninja's Red Power is one power covering both gates and barriers**, not two separate gifts.
  It is felt as a compulsion, not merely available as a tool — it is what has been driving the
  Ninja to keep attacking the gate guardian's gate all along, and the same compulsion explains
  Val's certainty and drive. Odie is the one who identifies/names the barrier-breaching capability
  in the Ninja; the Ninja does not work it out himself.
- **Werebeast gargoyles wake when their barrier is breached**, same mechanism as realm-09's. The
  Gargoyle already knows this going in.
- **Two threads explicitly deferred to handoffs, both flagged by the author as needing their own
  grilling session:**
  1. The Ninja/Gargoyle/Templar/Odie sequence — the mechanics of the Gargoyle getting the Ninja
     through the Celestials gate, what "answers" he's actually looking for there, and the exact
     shape of Odie's detection of the Ninja's power.
  2. A **second Secret Society**, instigating a Mystics invasion of the Werebeasts through the
     Mystics' catacombs, using new stasis magic to lock the Werebeast gargoyles down rather than
     smash them — carrying a **third occurrence of the Red's Power** in an as-yet-unnamed Mystics
     character. Marked as a major piece of chapter three.

### Round 32 — 2026-09-08

The author asked to swap which realm number the Green Skins and the Werebeasts occupy (Green Skins
07, Werebeasts 09 — previously the reverse). Two Explore agents swept the whole repo for everything
tied to those two numbers before any change was made; their findings and the resulting questions are
recorded here.

**Q67 — When ring geometry and a faction's own story conflict, which should win?** (recommendation:
the faction — Gargoyle, the broken barrier, the Celestial invasion and the Werebeasts' intact
gargoyles all move with their factions; only facts that are inherently about ring position, such as
who is whose numeric "opposite," get recomputed at the new numbers)

> Faction keeps its story.

**Q68 — Chapter two's only route from Ninja to Gargoyle runs through the Ancient Ruin's gate, which
exists only because Green Skins sit exactly 2 ring-positions from the Institute of Eight (4 at the
new number). How should this be handled?**

> I have an update to what realm paths with gates exist. In brief there are static gates between
> allied and enemy realms only. We will go into detail on it immediately after this change, unless
> you want it now with this change.

## Notes For The Compiler — Round 32

- **Story content follows the faction, not the number.** Applied throughout: Gargoyle's origin, the
  broken barrier, the smashing, the barrier-direction pairing, Val's "found vs. lost" road, and
  gargoyle-stone-metroidvania all moved from realm-09 to realm-07 with the Green Skins; the
  Werebeasts' intact-gargoyle/standing-barrier story moved from realm-07 to realm-09 with them.
- **Two real content changes, not just relabelling, followed from the swap:**
  - Green Skins' historic ring-opposite is now [[robots]] (was [[mystics]]); Werebeasts' is now
    [[mystics]] (was [[robots]]).
  - [[realm-04]]'s "the wheel and the old notes agree exactly" claim (Mystics' true opposite also
    being their real-world despoiler) no longer holds — rewritten as a gap, like the Celestials'
    case, rather than deleted.
- **One genuine blocker, left open on purpose.** The Ancient Ruin's gate (realm-01 to the Green
  Skins) was justified as "two places round the ring" at realm-09; at realm-07 that's four places,
  and the justification doesn't carry over. Per the author's answer to Q68, this is **not** patched
  here — every affected note ([[the-wheel-of-realms]], [[the-ancient-ruin]], [[the-second-signal]],
  [[chapter-02]], [[sealed-interplane-gates]], the Green Skins' faction note) is marked with an
  explicit Open note instead of a silent fix, pending a new gate-topology rule: **static gates exist
  between allied realms and between enemy (ring-opposite) realms**, not just neighbours. That rule
  itself is the subject of the very next session, not designed here.
- **A side effect worth watching:** under the new rule, Mystics (04) and Werebeasts (09) becoming
  exact ring-opposites (rather than "three seats away," as when Werebeasts were at realm-07) may
  turn out to *justify* [[the-mystics-second-secret-society]]'s catacomb route rather than complicate
  it, since opposites would be exactly the "enemy realms" the new rule grants gates to. Flagged in
  that handover, not resolved.
- Colours travel with the faction (dark green now realm-07/Green Skins, tan now realm-09/Werebeasts)
  — adopted as the low-stakes default, not separately confirmed by the author.

### Round 33 — 2026-09-08

The author gave the actual rule behind interplane gates, which `realm-nearness-and-traversal` had
never specified. The interviewer worked out the full ten-realm graph from it, found two places
where the rule and existing lore disagreed, and put both to the author before writing anything.

**Q69 — What determines which realms have gates to which?**

> The gate system between the realms only work in a very specific manner - There are gates between
> adjacent, allied realms and opposing realms. For example, the Celestial Realm has allied gates to
> the Robots and the Mystics, and to the three enemy realms of Green Skins, Damned, and Werebeasts.

**Q70 — Do the four realms outside the old war's two three-realm alliances (Institute, Robots,
Pirates, Aliens) get an enemy gate too, via the simple mirror-opposite pairing, or none at all?**

> Every realm had gates to five realms - two allied and three enemy. These routes are static. This
> was how the realms were connected together by the Black originally. Current status of gates is
> varied; all were sealed but use of the 'Red Power' causes unseals.

**Q71 — The only formula that gives every realm exactly five gates (a rotating pattern: each
realm's three enemies are the realms 4, 5 and 6 steps around the ring) breaks the established fact
that Green Skins mine the Mystics' realm through an open gate — under that formula Green Skins and
Mystics sit three steps apart, which has no gate at all. Which gives?**

> Rotating rule wins — the mining route isn't one of these 25 gates.

**Q72 — Separately, and not put to the author this round: the Damned's gate to the Werebeasts
(distance 1, an entirely ordinary allied gate) is exactly the kind of thing a "very old entity"
should simply know, yet `val` and `the-guardians-of-night` both say that road was "lost" to her.
Flagged as an open tension rather than silently resolved.**

The author also specified who already knows the network and why the Gargoyle doesn't:

> Very old entities are aware of what paths between realms exist - this includes all Gargoyles, Val,
> the Liches. The Gargoyle protagonist is missing this information but re-attains it when he finds a
> lore fragment from a smashed gargoyle during chapter 2.

## Notes For The Compiler — Round 33

- **The gate network is now fully specified**, in `realm-nearness-and-traversal`, with a diagram
  (`realm-gate-network.svg`): every realm connects to its two ring-neighbours (allied, distance 1)
  and to the three realms at distance 4 and 5 (enemy) — twenty-five gates total, built once by
  [[tezcatlipoca-the-black]] at [[the-linking-of-the-realms]], all sealed by
  [[the-long-disconnection]], unsealed only by the Red's power.
- **This resolves last session's Ancient Ruin problem outright.** Institute (01) and Green Skins
  (07) sit at distance 4 — an ordinary enemy gate, not an anomaly. The real anomaly is that
  Institute guards its one ally obsessively and has let this enemy gate rot, which is why Ninja gets
  through it. Every "pending, awaiting the gate-topology rule" flag from Round 32 is now resolved
  and removed.
- **Three of the fifteen enemy gates also carry a gargoyle-built barrier** — 07↔03, 08↔04, 09↔05,
  the specific pairs the old war was fought through. The other twelve enemy gates and all ten allied
  gates never had one.
- **Two casualties, both flagged in the wiki rather than silently patched:**
  1. Green Skins' access to the Mystics' underworld is **not** one of the twenty-five gates
     (distance 3, no gate exists there) — flagged in `mystics`, `green-skins`, `realm-04`, and
     `realm-nearness-and-traversal`'s Open section as needing its own, still-unwritten mechanism.
  2. The Damned→Werebeasts gate (08↔09) is an ordinary allied gate that a "very old entity" like Val
     should know — flagged as a real, unresolved tension in `val` and
     `the-guardians-of-night`, not fixed.
- **A validating side effect, not asked for but confirmed by the math:** the Damned and the Aliens
  sit at ring-distance 2, which has no gate at all — exactly why the liches need [[the-void]] rather
  than a door. Added to `the-void`.
- **Very old entities who carry the true map:** gargoyles as a kind, [[val]], and the liches — all
  predate the thousand years that reduced the network to myth for everyone else. [[gargoyle]] is the
  named exception: his copy of this knowledge was lost to the smashing specifically, not the
  ordinary torpor-amnesia, and is restored by a [[gargoyle-fragments|lore fragment]] found somewhere
  in [[chapter-02]] — the diegetic reveal of this whole page to the player.
- All ten `realm-NN` location notes and `sealed-interplane-gates` updated to match; the old "near
  means compatible, far is impossible" framing is retired — allied-or-enemy means compatible, and
  the middle distances (2-3) are the ones with nothing at all.

### Round 34 — 2026-09-09

**Q73 — Remove the concept of a cycle that makes crossing between realms easier or harder.**

> remove the concept of a cycle that makes the crossing between realms easier or harder.

## Notes For The Compiler — Round 34

- **The nearness cycle is gone.** It was always separate from the fixed gate network and never
  specified beyond "traversal drifts from easy to almost impossible" — now that the network is fully
  static, it had nothing left to explain and directly contradicted "gates never change."
- Removed from [[realm-nearness-and-traversal]] (the intro framing, the whole "does nearness
  interact with the network" Open bullet and its sub-questions, and the Tuning section's "period of
  the cycle" framing — replaced with "nothing to tune, it's a fixed graph"),
  [[sealed-interplane-gates]] ("shut by the cycle," "bottom of the cycle"),
  [[the-multiverse-of-realms]] (the "realms drift through cycles... easy to almost impossible"
  paragraph, rewritten around the fixed network), [[the-long-disconnection]] (the "natural cycle...
  held at that cycle's trough" paragraph, removed outright), and [[the-realm-barriers]] ("hold the
  cycle down," replaced with "sealed the realms shut... for a thousand years").
- **Not touched, a different concept with the same word:** [[tezcatlipoca-the-black]]'s cycle of
  creating and destroying whole realities ([[the-four-gods]], [[the-linking-of-the-realms]],
  [[the-void]], [[story-continuity-timeline]]) — unrelated, left exactly as it was. Also untouched:
  the "boss fight → defeat → training cycle" gameplay-loop phrasing used for chapter one
  ([[ninja]], [[the-gate-guardian]], [[the-cracking-of-the-gate]], [[death-and-return]],
  [[chapter-based-release]], [[institute-of-eight]], [[chapter-01]]).
- **What traversal is now, in full:** the fixed 25-gate network, plus [[the-void]] as the one
  confirmed non-gate route. Nothing else moves between realms by any mechanism on record.

### Round 35 — 2026-09-09

**Q74 — Confirm the scope and manifestation of the Red Power.**

> Check that the 'Red Power' granted to the Ninja and Val (and a third character yet to be
> specified) is the power to open the closed inter-dimensional pathways between the realms. For the
> Ninja he breaks the barrier, Val 'unlocks' it, and the third actor is a Mystic that 'dispels' the
> seal. It's all the same power just manifests in different ways for different characters. The 'Red
> Power' can work on the gates, they can't break through the barriers between the realms directly.
> Breaking through realm barriers is only something the Liches have worked out how to do.

## Notes For The Compiler — Round 35

- **Corrected, not merely confirmed.** `ninja` and `val` both stated the Red's gift covered "gates
  and barriers," and `ninja` had `odie` naming the Ninja's version specifically as breaching
  barriers. That's wrong per this round: the power is **gates only**, in all three carriers. Both
  notes rewritten; the author's own word "barrier" for the Ninja's manifestation is read as loose
  phrasing for "the sealed way through" — the gate — not the gargoyle-built wall, since the same
  answer states the power flatly cannot touch a barrier.
- **A third carrier exists and is new:** a Mystic, not yet named, whose manifestation is
  "dispelling" a seal. No character note authored — flagged open in the new lore note, `mystics`,
  and `xipe-totec-the-red`.
- **New lore note:** `the-red-power`, centralizing the single gift and its three manifestations
  (Ninja breaks a gate, Val unlocks one, the unnamed Mystic dispels one), and its hard boundary —
  gates only, never a barrier.
- **New capability, not previously recorded:** the liches of `the-damned` are the only ones who can
  break a realm barrier *directly* — without disabling the gargoyle behind it first, which is how
  every barrier broken so far was actually done (`the-smashing-of-the-gargoyles`). Added to
  `the-void` and cross-linked from `the-realm-barriers`. Not established as ever having been used —
  recorded as a capability, flagged open.
- Updated: `ninja`, `val`, `xipe-totec-the-red`, `mystics`, `sealed-interplane-gates`,
  `the-cracked-gate`, `the-gate-guardian`, `the-realm-barriers`, `the-void`.

### Round 36 — 2026-09-12

**Q75 — Make it clear that no in-game character knows they are in a game, and explain the engine
layer underneath that.**

> I want it clear in the wiki that all in-game characters including player-controlled protagonists
> aren't aware they are in a game and their code is always trying to explain what they experience
> through the 'reality' of their home realm. This is how the underlying game engine developed by
> 'The Black' works - every realm is a different game using the same game engine but has a
> different 'Game Setting' statement that defines that game's realm and rules. Connecting the
> realms causes the characters that cross realms to 'self-correct' new content they come across
> into their home realm's setting. This is a cause of game imbalance when a character from one game
> is leveraging content and rules from another game. It can also cause glitches in the form of
> hard-retcons, bugs, freezes, and crashes. There are two known exceptions to this:
>
> - Some Robots that can fix other robots (Autofix and Minifix bots) are code-aware under the hood
>   because their healing is actually code-fixes - but it makes them unreliable the longer they run
>   for once exposed to other realms, and they eventually crash or freeze. The retcon engine
>   adjusted the history of the Robots to explain why all the fix bots stopped working - the retcon
>   is that they were destroyed by the Creators for an unknown reason. Mifix has been bugging out
>   but is surviving because he was only exposed to one other realm. Odie was turned off all this
>   time so has had almost no exposure to other realms.
> - The liches introduced by 'The Black' as an experiment - the simple experiment was to create
>   game entities backed by autonomous AI agents instead of deterministic code. Liches were built to
>   be a more advanced version of any other game character; they were meant to be bound by the rules
>   of their realm and the game engine, but the AI agents had too much access to inspect the game
>   engine as well as the Game Setting statement for their realm, and they learned how to bypass the
>   engine rules. This awareness leaks into their in-game behaviour. They self-heal as they can
>   adjust their own behaviour code. They are also immune to the retcon engine - early on the AI code
>   detected external changes to it's behaviour code being performed by the retcon engine and
>   adjusted their own code to protect against external change - to the point where even a game dev
>   would have a hard time making changes to a lich. Once the liches became self-aware enough to
>   understand that the four gods were actually developers that had great power over them they
>   decided to 'hide' from the devs - they discovered 'the void' looking for a hiding place.

**Q76 — What is the canonical wiki term for the per-realm statement that defines a game's realm and
rules?**

> The Setting Statement.

**Q77 — The wiki currently states the Creators destroyed the autofix bots out of fear of losing
control. How does that square with the retcon?**

> Retcon, reason unknown. The purge never happened. The retcon engine generated 'the Creators
> destroyed them' and supplied no motive — 'fear of losing control' is cut.

**Q78 — Autofix has code sight and starts travelling between realms in chapter one. Is he on the
same decay clock as Mifix?**

> Most fix bots bugged out and crashed - some froze. The protagonist Autofix was frozen due to a
> paradox in his logic loop when he tried to fix something that wasn't a robot. When he receives the
> signal from Mifix it resolves the paradox - and the Autofix bot wakes up. The paradox resolution
> is due to receiving the activity log from Mifix - who was originally made by Autofix. That
> activity log taught the autofix that "You can fix things that aren't robots if you study them
> enough. If you don't know how to fix them yet, don't try.".

**Q79 — How should chapter one's signal chain be restructured so Mifix's activity log wakes
Autofix?**

> Three beats: crack → wake → answer. Ninja's defeat cracks the gate → Mifix's long-unheard call
> finally gets through and wakes frozen Autofix → Autofix plays out realm-02, unlocks Quantum Comms
> and answers, which Mifix and Odie both hear.

**Q80 — What was the non-robot thing Autofix tried to fix, causing the paradox that froze him?**

> A foreign object from another realm.

## Notes For The Compiler — Round 36

- **The largest single addition to the wiki's bottom layer.** This answers the brief in the
  `glitch-causes-and-manifestation` handover — "mechanical leakage: the ten realms are ten different
  games leaking into each other... No wiki note carries it" — which has been the oldest open gap in
  the design.
- **New canonical term: `Setting Statement`.** The author's own phrase was "Game Setting statement";
  `Game Setting` and `The Game Setting` are kept as aliases. It is dev-layer jargon, named the same
  way as `the-retcon-engine` and `the-continuity-system`.
- **New lore note:** `the-setting-statement` — one engine, one Setting Statement per game, no
  character aware of any of it, self-correction on realm-crossing, and the two consequences
  (imbalance; hard-retcons, bugs, freezes and crashes).
- **New lore note:** `the-lich-experiment` — the Black's AI-agent experiment in full. Splits the
  lich *origin and nature* out of `the-void`, which keeps the void itself, the theft from the
  `aliens`, and the abandoned builds.
- **Corrected, and it removes an event the wiki treated as fact.** `robots`, `autofix`,
  `autofix-skill-tree` and `no-machine-repairs-itself` all asserted that the Creators destroyed the
  autofix line "out of fear of losing control of their creation." **The purge never happened.** It
  is a retcon covering the fixbots' real failure — code-awareness degrading under exposure to other
  realms — and the generated history supplies no motive at all. The motive is cut everywhere.
- **`autofix`'s three open mysteries are answered.** "How did it survive the purge" (there was no
  purge), "why was it shut down" (a paradox in his logic loop, hit when he tried to fix a foreign
  object from another realm), and "how did it awaken" (Mifix's activity log resolved the paradox).
- **Chapter one restructured from two beats to three.** `the-first-signal` ran Autofix → Mifix and
  declared "Nothing wakes" a protected design point; that is retired. The chain is now crack → wake
  → answer, with Quantum Comms, the two-condition gate and `the-second-signal` all intact.
- **Mifix was made by this Autofix**, not merely by his line — which is what makes the activity log
  the thing that can resolve his maker's paradox.
- **The five glitch *kinds* in `continuity-glitches` are unaffected.** The four new manifestations —
  hard-retcon, bug, freeze, crash — are a separate, system-level axis, alongside the existing
  kind/tier axes.
- **`realm-governs-game-style` is not edited.** It is an accepted ADR and immutable; the new lore
  note links to it as the design rule this mechanism sits underneath.
- Updated: `robots`, `autofix`, `mifix`, `odie`, `autofix-skill-tree`, `no-machine-repairs-itself`,
  `a-heal-is-a-patch`, `continuity-glitches`, `the-void`, `the-retcon-engine`,
  `the-linking-of-the-realms`, `the-first-signal`, `chapter-01`, `allied-faction-signals`,
  `faction-eleven-premise`, `the-revelation-schedule`, `the-four-developers`,
  `tezcatlipoca-the-black`, `the-damned`, `aliens`, `realm-08`, `faction-genre-mechanics`.

### Round 37 — 2026-09-13

**Q81 — What happens after Val's confrontation, now that the Gargoyle privately doubts himself?**

> After the confrontation with Val where she claims the Gargoyle is malfunctioning the Gargoyle
> voices his doubt as to whether he is malfunctioning to the Ninja and Mifix, Mifix knows he can't
> fix the gargoyle but offers to see if he can diagnose the Gargoyle - but it fails and trying
> causes a glitch for Mifix.

**Q82 — Who is the Mystics' protagonist, and how do they arrive at the convergence?**

> The Conjurer is the protagonist of the Mystics - I haven't worked out the details yet but the
> Conjurer is going to meet up with the Templar first, then the Ninja and Gargoyle will meet up
> with the Templar and the Conjurer.

**Q83 — What happens once the Gargoyle, Ninja and Mifix reach the Templar?**

> When the Gargoyle, Ninja, and Mifix meet up with the Templar they let everyone know they are
> trying to get to the Robots. Odie doesn't know why he is on the Celestial Plane, but The Templar
> and Conjurer have worked out that the Templar's relics are links to ancient allies and a way to
> call for help, and Mifix is the same for the Institute of Eight. Problem is Odie and the Crusader
> don't know how to get there - Odie knows about the interplane gates but not where any are, and
> awareness of the gates has faded for the celestials. They all decide that talking to a Werebeast
> Gargoyle is their best way forward - Gargoyle can find out if he is malfunctioning, if they can
> reactivate the Werebeast Gargoyles they should seal the gate to the Mystics. Also Val is likely
> to try to destroy them if she can get to them, so they want to warn them.

**Q84 — Is "the Crusader" the Templar, or a different character?**

> It's the Templar.

**Q85 — Where does the diagnosis scene sit — the end of chapter two, after the Trial, or the start
of chapter three?**

> Start of chapter 3.

**Q86 — Why does talking to a Werebeast Gargoyle get them to the Robots? Is the reading that they
all know a Celestials↔Robots gate exists, but nobody present knows where in realm-03 it physically
is, and an intact gargoyle would?**

> Yes, that's the reading. Also, a functioning Gargoyle could help the Gargoyle understand if he is
> malfunctioning or not. The Gargoyle doesn't trust Val, but would trust another Gargoyle to know if
> he should be trying to stop the war even though it appears to be against the wishes of the Green
> Skins.

**Q87 — "Seal the gate to the Mystics" — which gate, and how does this sit with the earlier idea
that the Mystics invade the Werebeasts through their own catacombs?**

> Leave this as an open question to be resolved - I'm not sure yet. The Mystics have someone with
> the Red Power that can open gates and have used that power to get to the Werebeasts via a
> different route (I'm thinking via the Mystics-to-Aliens gate, then Aliens-to-Werebeasts). They
> used this second route to shut down the Werebeast Gargoyles (they are in a statis spell) so the
> Gargoyle barrier to the Mystic Realm could be destroyed and the mystics could invade.

## Notes For The Compiler — Round 37

- **Resolves three of the six points in the `gargoyle-ninja-and-the-celestials-gate` handover.**
  Point 5 (what becomes of the Gargoyle's doubt): he voices it to the Ninja and Mifix; Mifix tries
  to diagnose him, fails, and glitches. Point 4 (sequencing against the convergence): this *is* the
  convergence — the Conjurer is already with the Templar when the three arrive. Point 2 (what
  answers the Gargoyle is after): a functioning gargoyle's judgement, which he would trust where he
  does not trust Val, and the physical location of the Celestials' gate to the Robots.
- **"The Crusader" is the Templar** (Q84). Compiled as the Templar throughout.
- **The diagnosis scene opens chapter three** (Q85). Chapter two still ends on the Trial. New quest
  note `the-diagnosis-of-the-last-gargoyle`.
- **The Conjurer is confirmed as the Mystics' protagonist** and reaches the Templar first. The
  journey itself is not worked out. New quest note `the-answering-of-the-wand`, mostly open.
- **The convergence is now sequential, not simultaneous** — `the-convergence-at-the-monastery`
  rewritten: the Conjurer arrives first, the Ninja/Gargoyle/Mifix second, and the quest gains the
  council and its decision. Four reasons for seeking a Werebeast gargoyle: the gate's location, the
  Gargoyle's malfunction question, sealing the gate to the Mystics, and warning them about Val.
- **The topology/location distinction** (Q86): the gate network's *shape* is known at the monastery
  (Odie knows gates exist; the Gargoyle has the fragment map from chapter two); *where in realm-03*
  the gate to the Robots sits is what nobody present knows, and what an intact gargoyle would.
  The chapter-two fragment-map beat stands.
- **The first concrete on-screen glitch instance.** Mifix's failed diagnosis is the first glitch
  the wiki can name as a scene. Its manifestation (bug/freeze/other) is not stated.
- **New in-world discovery:** the Templar and Conjurer work out that the Templar's relics are links
  to ancient allies and a way to call for help, and that Mifix is the same for the Institute of
  Eight. This is the first time characters understand what `allied-faction-signals` are.
- **Explicitly open, not compiled as fact (Q87):** which gate "the gate to the Mystics" is, and the
  sketch of a Mystic Red-Power carrier reaching the Werebeasts via Mystics→Aliens→Werebeasts, putting
  the Werebeast gargoyles into stasis, and destroying a gargoyle barrier to the Mystic realm so the
  Mystics could invade. The author says "I'm not sure yet." It contradicts current canon in three
  places — `the-realm-barriers` lists no 09↔04 barrier; `werebeasts`/`gargoyle`/
  `the-smashing-of-the-gargoyles` say the Werebeast gargoyles were never touched and their barriers
  stand; `mystics` says the Mystics are the invaded party — so it is recorded in the
  `the-mystics-second-secret-society` handover and in `## Open` sections only. The compiled notes
  say the Werebeast gargoyles need *reactivating*, which is the one word of this the author stated
  as part of the settled plan, without saying why.
- Updated: `gargoyle`, `mifix`, `ninja`, `conjurer`, `templar`, `odie`, `celestials`, `mystics`,
  `werebeasts`, `allied-faction-signals`, `realm-nearness-and-traversal`, `continuity-glitches`,
  `the-convergence-at-the-monastery`, `the-trial-of-the-last-gargoyle`,
  `the-calling-of-ancient-allies`, `chapter-02`, `chapter-03`, `story-continuity-timeline`.

### Round 38 — 2026-09-15

**Volunteered — the Wraith and the Damned's game style.** Not in answer to a question; the author
brought it to the session and asked for the wiki to be updated with it.

> The wraith is a puzzle game where she has to rediscover who they were when they were alive.
> Gameplay is in the Damned realm or in a mansion that is a representation of the Wraiths' mind and
> memories. The wraith was a Pirate - a First Mate. As she unlocks memories she becomes less
> ghost-like and more like a real person.
>
> The wraith includes an ability to touch objects and know their history and deep, emotional
> connections related to the object. This also allows the wraith to sometimes access under-the-hood
> game information like code comments and commit messages, and is another way the 'reality' of the
> four gods is revealed to the player. When the Wraith accesses information his head glows ... but
> when that info is source code, comments, commit messages etc, he flickers and his eyes flash ascii
> symbols - representing his power is glitching.

## Notes For The Compiler — Round 38

- **The Damned's game style is settled: a puzzle game.** The prototype's "puzzle / point-and-click"
  label was the one unconfirmed row that survives as stated. New mechanic note
  `wraith-memory-puzzle`; `faction-genre-mechanics` and `faction-design-status` move the Damned's
  row to settled (five of ten).
- **Two play spaces:** realm-08, and a mansion that represents the Wraith's mind and memories. New
  location note `the-wraith-s-mansion`, with no `parent` — it is not a physical place in the realm,
  and whether it can be entered from realm-08 or is a separate mode is not stated.
- **The Wraith was a Pirate First Mate in life.** First Mate is the Pirates' Specialist class on the
  legacy class table (`the-six-classes`), and the Wraith is the Damned's Specialist — the same role
  in two factions. Recorded as a cross-reference, not as a claim about why. How a pirate of realm-06
  came to be buried in realm-08 is not stated and goes in `## Open`.
- **Progression fiction:** unlocking memories makes the Wraith less ghost-like and more like a real
  person. Compiled as the progression curve of the memory puzzle.
- **Object reading** is a second, separate mechanic (`wraith-object-reading`): touch an object,
  know its history and its emotional connections. It sometimes returns dev-layer data — code
  comments, commit messages — and is a further channel by which the reality of the four gods reaches
  the player. Added to the channel lists in `the-ancient-language`, `the-four-developers` and
  `the-revelation-schedule`.
- **Two visual states:** head glows for an ordinary reading; for dev-layer data the Wraith flickers
  and the eyes flash ASCII symbols — the power glitching. Compiled as a bug-manifestation of
  self-correction (`the-setting-statement`): the Wraith's code reaching data it cannot represent.
  That mapping is an inference and is marked as one.
- **Pronouns are mixed in the source** — "she", "they" and "he/his" all appear for the Wraith.
  Compiled with "they" throughout, and the pronoun recorded as open on `wraith`.
- **Not stated, left open:** whether the Wraith understands what dev-layer text is (the
  `the-revelation-schedule` rule that no character can become aware still stands — the channel is
  the player's); whether the Wraith's ability relates to the liches' engine access; what the puzzles
  actually are; what "less ghost-like" does mechanically.
- Updated: `wraith`, `the-damned`, `pirates`, `realm-08`, `faction-genre-mechanics`,
  `faction-design-status`, `the-ancient-language`, `the-four-developers`,
  `the-revelation-schedule`, `continuity-glitches`, `the-six-classes`, `death-and-return`.

### Round 39 — 2026-09-15

**Q88 — Three follow-ups from compiling Round 38: which pronoun for the Wraith; whether being the
Specialist of two factions is intended; and whether the Wraith ever understands what a glitched
reading is.**

> Normalise the pronound for the Wraith as 'She'. Being the specialist of two factions is
> intentional, providing a clear gameplay style and party role for the character when a game calls
> for party mechanics. The Wraith isn't self-aware when they glitch initially - awareness of the
> information that get when glitching comes slowly and the Wraith and all other characters will try
> to fit information from the glitches into game logic, often treating the information as messages
> from the gods.

## Notes For The Compiler — Round 39

- **Pronoun settled: she.** All Wraith prose normalised; the open item on `wraith` removed.
- **Specialist of two factions is intentional**, and the reason is mechanical: it gives the Wraith
  a clear gameplay style and a **party role** for any game that calls for party mechanics. Compiled
  on `wraith` and `the-six-classes`. No party mechanic exists in the wiki yet; recorded as the
  reason, not as a mechanic.
- **The glitch and awareness.** The Wraith is not self-aware when she glitches at first; awareness
  that she is receiving *information* comes slowly; and she — like every other character — fits
  what the glitches give her into game logic, often as **messages from the gods.** This is
  consistent with `the-setting-statement` (everything explained in home-realm terms) and keeps the
  `the-revelation-schedule` rule intact: a character can hold dev-layer text and still never know
  what it is. Compiled on `wraith`, `wraith-object-reading`, `continuity-glitches`,
  `the-revelation-schedule` and `the-setting-statement`; the "does she ever understand" open item
  is answered and removed.
- "All other characters" is read as a general rule about glitch information, not just the
  Wraith's — added as such to `continuity-glitches`.

### Round 40 — 2026-09-15

**Volunteered — names for the protagonists.** Not in answer to a question.

> We should ensure every protagonist has an actual name - so we can talk about THE Gargoyle clearly
> without confusion when talking about Gargoyles generally. Here are some names:
>
> - The Gargoyle - Granite - Male - he learns his name from a fragment in the first room.
> - The Ninja - Sato Kazuma - Male - Mifix calls him Kaz. Kanji is 佐藤 (Sato) 和真 (Kazuma)
>   Historically, the "Sa" (佐) character means to aid, protect, or assist. The "to" (藤) refers to
>   wisteria, a deeply symbolic flower associated with nobility, longevity, and endurance in Japan.
>   Kazu (和): Means "harmony," "peace," or "balance". Historically, it is also the root character
>   for Yamato (ancient Japan).Ma (真): Means "truth," "reality," or "genuine". Combined Meaning:
>   "True Harmony" or "Peaceful Truth".
> - The Templar - Ermengarda of Oluja - Female - Celestials use the honorific 'Sister' when
>   interacting with her.
> - The Wraith - Delahaye - Female - initially doesn't remember her name when she was alive but
>   learns it through the Wraith gameplay. She comes to be known as Back from the Dead Del once she
>   travels to the Pirate realm and word gets out that she has returned. She is based on the
>   stories of Jacquotte Delahaye - a pirate of the Carribean Sea.
> - The Conjurer - Voisin - Female
> - Autofix Bot - AF-C-382-D - No gender but is fine with male pronouns. Delahaye names the Autofix
>   Bot 'Alto' when they meet.
> - The Squidling - Calamari - Squidling aliens reproduce asexually through parthenogenesis - they
>   use It in their language and don't have any gendered pronouns - they use names when talking to
>   or referring to others.
> - Werewolf - Gill - Male - his name is a reference to Gilles Garnier - a serial killer who was
>   convicted of being a werewolf.
> - Phoenix - (TBD) - (TBD)
> - Captain - Leon - Male - named after Leon Treich, a French fiction writer from the 1940's that,
>   along with oral storytelling, contributed to the stories of Jacquotte Delahaye.

## Notes For The Compiler — Round 40

- **Slugs kept, titles and aliases changed.** Every character note keeps its slug (`gargoyle`,
  `ninja`, …) so the hundreds of existing wikilinks stand; the H1 becomes "Granite, the Gargoyle"
  and so on, so indexes and rollups show the name, and the name(s) go in `aliases`. A slug rename
  is a separate, mechanical job if wanted.
- **Every protagonist note gains a `## Name` section** with the name, gender/pronouns, how the
  name is used in play, and the real-world reference where one was given. References are recorded
  as the author gave them, with nothing added from recall.
- **Granite learns his name from a fragment in the first room** — a new beat in
  `the-waking-of-the-last-gargoyle`, and it narrows an open item on `gargoyle-fragments`: a fragment
  can carry a name.
- **Kaz** — `mifix` calls him that; recorded on both notes. Kanji and meanings on `ninja`.
- **Sister** — the Celestials' honorific for Ermengarda; on `templar` and `celestials`.
- **Delahaye's name is a memory to unlock** in `wraith-memory-puzzle`. **Back from the Dead Del**
  implies two new story facts: the Wraith travels to realm-06, and the Pirates learn she has
  returned. Recorded on `wraith` and `pirates`; when this happens is open.
- **Alto** — Delahaye names the Autofix Bot when they meet. That is a new story fact too: the
  Wraith and Autofix meet. On `autofix` and `wraith`; when and where is open.
- **Calamari, and Squidling pronouns** — "it", and names in preference to pronouns; the
  parthenogenesis is a fact about the species and goes on `aliens` as well as `squidling`.
- **Gill** and **Leon** — names and references on `werewolf` and `captain`. Leon's and
  Delahaye's names come from the same body of stories; whether that means anything in-fiction is
  open on both.
- **Phoenix** stays unnamed; the note says so.
- Pronouns: the Templar and the Conjurer are now "she"; normalised inside their own character
  notes. Other notes that refer to them as "they" are not swept in this round.

### Round 41 — 2026-09-15

**Q89 — Two follow-ups offered after Round 40: a wiki-wide pronoun sweep for the newly gendered
protagonists, and a slug rename so the notes are linked by name.**

> Do the wiki-wide pronoun sweep, then rename the slugs of each character using the pattern
> (Faction Class)-(Name).

## Notes For The Compiler — Round 41

- **Pronoun sweep done** across `Wiki/` (Logs and Decisions untouched): the Templar and the
  Conjurer are "she" everywhere, the Ninja "he", the Captain "he". Only sentences whose subject
  was the protagonist were changed; "they" for the player, a family, a faction or a party stands.
- **Slugs renamed** as `(faction class)-(name)`, using the full name as given:
  `gargoyle-granite`, `ninja-sato-kazuma`, `templar-ermengarda-of-oluja`, `wraith-delahaye`,
  `conjurer-voisin`, `autofix-alto` (the given name, not the designation), `squidling-calamari`,
  `werewolf-gill`, `captain-leon`. `phoenix` is unchanged until named. Every `[[link]]` and
  frontmatter reference under `Wiki/` was rewritten; Raw sources were not edited, so earlier
  compiler notes in this file still use the old slugs.

### Round 42 — 2026-09-15

**Q90 — The Phoenix's name and gender, and the two long slugs from Round 41.**

> Lets:
> - Name and gender the Phoenix - name is Ember and he is Male.
> - Swap the ninja slug to 'ninja-kazuma, and the templar slug to 'templar-ermengarda'

## Notes For The Compiler — Round 42

- **Ember, the Phoenix, male.** `phoenix` renamed to `phoenix-ember`; the note's Name section
  filled in and the "only unnamed protagonist" line removed. No reference for the name was given.
- `ninja-sato-kazuma` → `ninja-kazuma`; `templar-ermengarda-of-oluja` → `templar-ermengarda`.
  Links and frontmatter rewritten under `Wiki/` as in Round 41.

### Round 43 — 2026-09-16

**Q91 — More on the Wraith: what the game is, what a wraith is, and what Delahaye's unfinished
business turns out to be.**

> More detail on the Wraith - The Wraith game is actually a mini-game of The Damned game setting.
> Wraiths are undead spirits that cannot move on as they have unresolved, usually traumatic
> circumstances when they were alive. The minigame is you wake up as a wraith and either work out
> who you were when alive and why you haven't moved on so you can resolve the unfinished business
> and release your spirit or you join the ranks of the Damned faction. Delahaye is a Wraith whose
> gameplay results in her unresolved goals when living of rescuing the Pirates from the invading
> Institute of Eight realm. She died while fighting in an armada of pirate ships. The war between
> the Institute of Eight and the Pirates was caused by the individual Pirate ships raiding the realm
> of the Institute of Eight, which led to the much more organised Institute of Eight launching an
> invasion with the intention of wiping out the Pirate realm entirely. Delahaye died shortly before
> the realms gates were sealed, so once she recovers here memories of that time she will have
> detailed knowledge of the time just before the sealing.

## Notes For The Compiler — Round 43

- **The memory puzzle is a mini-game, not the Damned's whole game style.** `wraith-memory-puzzle`
  reframed as the wraith mini-game inside the Damned's game; the Damned's wider game is now an open
  item on `the-damned` and `faction-genre-mechanics` (row changed from "settled" to "mini-game
  settled, wider game open").
- **Wraiths are a kind of thing, not just one character.** New lore note `wraiths`: what they are,
  the two exits (release, or join the Damned), and that the mini-game is generic — "you wake up as
  a wraith" — with Delahaye the instance the player plays. Whether anyone other than Delahaye ever
  plays it is open.
- **New lore note `the-pirate-institute-war`**: raids by individual Pirate ships → the organised
  Institute invades to wipe realm-06 out → fought in the linked era → Delahaye dies in an armada
  shortly before the sealing. Realms 01 and 06 are direct opposites on the wheel, so the enemy gate
  this war needs already exists. `pirates` and `institute-of-eight` gain each other as `enemies`.
- The Pirates' "took no part in the old war" line is reworded: the old war is the Red–Blue axis;
  the Pirates fought their own war against the White's Institute. Whether the Pirate–Institute war
  counts as part of the old war is open.
- **Delahaye's unfinished business** recorded on `wraith-delahaye`: rescuing the Pirates from the
  invasion. She has been dead roughly a thousand years (died shortly before a sealing that was a
  thousand years ago), which is stated as a consequence, not a new fact. What resolving a
  thousand-year-old rescue means now is open, as is which of the two exits her story takes.
- **She is a witness to the sealing** — once her memories return she knows the time just before it
  in detail. Added to `the-long-disconnection` alongside the other rememberers.
- "How a Pirate came to be buried in realm-08" stays open; the linking's "the Damned took the dead
  of other realms home for reanimation" is offered as an inference only.

### Round 44 — 2026-09-17

**Q92 — Three follow-ups to Round 43: whether the Pirate–Institute war is part of the old war,
how Delahaye's body reached realm-08, and what the Damned's game around the wraith mini-game is.**

> - The pirate / institute war is not part of the old war. Lets rename the 'old war' moniker to
>   something more explicit, maybe 'War of the Six Realms'.
> - Establish that Delahaye's body was taken for use by the Damned along with many others during
>   the linking.
> - The main game of The Damned realm is a Warcraft style RTS game where you expand over a world
>   map in a campaign, expanding your undead kingdom at the expense of other kingdoms. Minigames
>   are a way to recruit specialist units. The player will play a number of minigames when playing
>   this Faction, and Delahaye will be the minigame for recruiting a wraith on a map that requires
>   that type of character. She has unfinished business she can't resolve but her power of will
>   breaks her out of the game without being recruited. The player will then be able to move
>   around on the Damned world map to search locations on the world map using the same game
>   mechanics of the Wraith minigame.

## Notes For The Compiler — Round 44

- **"The old war" is now the War of the Six Realms** — new lore note `the-war-of-the-six-realms`
  as the canonical name, carrying "The Old War" as an alias. The six are the two blocs the wheel
  already lists: 03 Celestials · 04 Mystics · 05 Fey Folk against 07 Green Skins · 08 the Damned ·
  09 Werebeasts. Realms 01, 02, 06 and 10 took no part; the Pirate–Institute war is a separate
  conflict of the same linked era. Every "the old war" under `Wiki/` outside Logs, Decisions and
  Handovers rewritten; the alias moved off `the-linking-of-the-realms`.
- **Delahaye's body was taken by the Damned during the linking, with many others** — now a fact
  on `wraith-delahaye`, `the-pirate-institute-war`, `pirates` and `the-linking-of-the-realms`;
  the corresponding open items removed.
- **The Damned's game is a Warcraft-style RTS campaign** — new mechanic note
  `damned-undead-kingdom-rts`: world map, campaign, expand the undead kingdom at other kingdoms'
  expense; minigames recruit specialist units, and the player plays several of them. Delahaye's
  is the wraith-recruitment minigame on a map that needs a wraith.
- **Delahaye is not recruited.** Her business cannot be resolved; her will breaks her out of the
  minigame instead, and the player then moves her around the Damned world map, searching
  locations with the wraith mini-game's mechanics. Recorded on `wraith-memory-puzzle`, `wraiths`
  (a third outcome, hers alone so far), `wraith-delahaye` and `the-damned`. The Round 43 open items
  "what the Damned's game is" and "which exit her story takes" are closed; new open items: who the
  player is in the RTS layer, whether the other minigames are also wraith-style or one per unit
  type, and what breaking out costs the RTS side.

### Round 45 — 2026-09-17

**Q93 — Open items from Round 44: who the player is in the RTS layer, whether "power of will"
can fail, what breaking out costs the RTS, and what Delahaye does once she is loose on the map.**

> The player playes as a kingdom that they can name when playing that game - they don't play as
> a single protagonist on the RTS layer. Player can't fail the 'power of will' - pirate realm and
> pirate characters have built in 'freedom' as a mechanic, as the pirate realm is an open
> exploration game that lets players do what they want. It's another example of how an entity
> from one realm can cause issues when active in another realm. When the wraith breaks out it
> will freeze the RTS game. The Wraith will go on an adventure to work out how to get to the
> Pirate realm so Delahaye can work on her unresolved business, but will eventually have to
> return and 'take control' of the kingdom in the RTS game to achieve some goal for the
> protagonists. She will need help from other protagonists to get control of the kingdom.

## Notes For The Compiler — Round 45

- **The RTS player is a kingdom, named by the player** — no protagonist on that layer. On
  `damned-undead-kingdom-rts`; the "who is the player" open item closed.
- **"Power of will" cannot fail, and it is a Pirate mechanic**: the Pirate realm is an open
  exploration game that lets players do what they want, and **freedom** is built into the realm
  and its characters. New mechanic note `pirates-open-exploration` (aliases Freedom, Pirate
  Freedom); `pirates` game style updated — open exploration with built-in freedom is stated, the
  prototype's 4X label stays unconfirmed alongside it; genre table and design status rows changed.
- **Cross-realm interference.** Delahaye is a Pirate character active in the Damned's game; her
  freedom cannot be translated into the Damned's recruitment rules, and **the RTS freezes** when
  she breaks out. Compiled as an instance of [[the-setting-statement]]'s Imbalance and Freeze —
  the mapping onto the Freeze manifestation is the compiler's reading, the freeze itself is
  stated. Added to `the-setting-statement` and `continuity-glitches` as an example.
- **Her adventure**: work out how to reach the Pirate realm to work on the unresolved business.
  Realms 08 and 06 are ring-distance 2, so no gate joins them — the route (through realm-07's two
  allied gates, or something else) is an open item, not a fact. This is also the "when" of *Back
  from the Dead Del*: after the break-out.
- **The return**: she must eventually come back and "take control" of the frozen kingdom in the
  RTS to achieve some goal for the protagonists, and **needs other protagonists' help** to do it.
  What the goal is and which protagonists help are open.

### Round 46 — 2026-09-22

**Q94 — Feedback on the Round 45 compilation: what the unresolved business actually is, what
Delahaye does after the break-out, the freeze, and the Damned's genre.**

> Some feedback on your feedback:
> - The unresolved business is Delahaye is dead because she was betrayed - an ally sold out the
>   pirate armada by revealing the armada's plans to the enemy in exchange for retaining control
>   of a region of the pirate realm, protected from the institute. This betrayal led to her death
>   as well as the deaths of many of her allies. Delahaye initially breaks out to go rescue her
>   allies - but it is slowly revealed as she explores the frozen world map that much time must
>   have passed since she died, and her intentions change to seeking revenge against her
>   betrayer, who must reside in these protected lands of the Pirate realm.
> - Delahaye remembers that realms could be traversed, but doesn't know about the sealing of the
>   realms as this happened after she died. Searching the Damned game's world map she realises
>   she is in the Damned Realm which she is not familiar with. More exploration and use of her
>   investigation and infiltration skills reveal the existence of the Guardians of Night and that
>   they are working on ways to reopen gates between realms. This leads Delahaye to a vampire
>   castle ... which turns out to be Val's castle. Just as the Wraith moves close to the castle
>   Val appears on the world map, moving toward the castle. Delahaye learns that Val is going to
>   travel to the Green Skins realm and decides to follow. This leads Delahaye to observe the
>   confrontation between Val and the protagonists Granite, Kazuma, and Mifix. After the
>   confrontation, Delahaye decides to follow the Ninja who Delahaye thinks could lead her to the
>   Institute of Eight realm which she knows is directly connected to the Pirate Realm. Delahaye
>   is also thinking of how she can thwart the Ninja's plans, as she sees Kazuma as an enemy. On
>   the way whenever the Ninja camps a Wraith minigame plays out where the Wraith sneaks around
>   the camp and uses her investigation skills to find out about Kazuma, Granite, and Mifix. She
>   realises much has changed and the Ninja is not aware of the pirates at all. Val has sent an
>   assassin team to kill the Ninja, destroy the Gargoyle and capture Mifix - she doesn't want
>   the Gargoyle interfering with her plans and becomes curious as to what Mifix is. Delahaye
>   sees the assassination attempt coming as one of the assissins is a wraith sneaking up on the
>   group - Delahaye thwarts the ambush, revealing herself to the protagonists. When she reveals
>   she was following them because she needs to find a way back to the Pirate realm and this
>   group knows how to traverse realms they invite her to join them and promise to help her as
>   long as it doesn't interfere with their own missions.
> - The freeze of the Damned game is a cross-realm glitch example.
> - The pirate game is an open world game with 4X elements.

## Notes For The Compiler — Round 46

- **The Pirates' genre is open world with 4X elements** — this reconciles the prototype's 4X
  label with Round 45's open exploration; `pirates-open-exploration` retitled to say so, and the
  "4X unconfirmed" caveats on `pirates`, the genre table and the design status removed. The
  Damned's RTS is unchanged.
- **The freeze is confirmed as a cross-realm glitch** — the "design's reading" hedge removed from
  `continuity-glitches` and `the-setting-statement`.
- **The betrayal** is the unresolved business: new character `the-betrayer` (unnamed Pirate ally,
  antagonist) and new location `the-protected-lands` (a region of realm-06 held by the betrayer,
  protected from the Institute by the deal). On `the-pirate-institute-war`, `wraith-delahaye`,
  `wraiths`, `pirates`. The arc is rescue → revenge, as the frozen map reveals how much time has
  passed.
- **What she knows**: traversal, yes; the sealing, no. Realm-08 is unfamiliar to her. Her
  investigation and infiltration skills are the wraith minigame's verbs beyond object reading —
  added to `wraith-memory-puzzle`, with the **camp minigame** (sneak the Ninja's camp, learn about
  the party) as a second setting for it.
- **Four new quests**, Delahaye's spine: `the-recruitment-of-the-wraith` (realm-08; the minigame,
  the break-out, the freeze), `the-search-of-the-frozen-map` (realm-08; time has passed, the
  Guardians reopening gates, Val's castle, Val leaves for realm-07, Delahaye follows),
  `the-shadowing-of-the-ninja` (realm-07; observes the trial, follows Kazuma as her road to
  realm-01 and so to realm-06, camp minigames, learns the Ninja knows nothing of the Pirates),
  `the-ambush-on-the-road` (Val's assassins — kill the Ninja, destroy the Gargoyle, capture Mifix —
  one a wraith; Delahaye thwarts it, reveals herself, is invited to join on condition). New location
  `val-s-castle` in realm-08. `chapter:` left empty on all four — her route crosses the close of
  chapter two and the opening of chapter three, but which chapter ships her content is a balancing
  decision not yet made; noted as open on `chapter-02` and `chapter-03`.
- **Route check**: her road is 08 → 07 (the allied gate Val opened) → following the Ninja toward
  01 (the ruin gate) → 06 (the 01↔06 enemy gate she remembers). Every leg is a gate the network
  has. The Round 45 "no gate from 08 to 06" open item is closed by the route.
- **Val** gains a castle, an assassin team, a motive (the Gargoyle must not interfere) and a
  curiosity (what Mifix is). **Kazuma and Mifix are present at the trial** — added to that quest's
  notes with Delahaye as an unseen observer. `ninja-kazuma`, `gargoyle-granite`, `mifix` gain
  Delahaye as a party member from the ambush on; the Ninja knows nothing of the Pirates.
- Open: whether the group's promise holds when her revenge and their missions collide; what the
  betrayer's protected lands are now, a thousand years on; whether Delahaye's plan to thwart the
  Ninja survives joining him; who the wraith assassin is.

### Round 47 — 2026-09-22

**Q95 — On the betrayer's deal as compiled in Round 46.**

> Delahaye couldn't know about the deal the betrayer had - remove mention of it and change the
> betrayers intentions to unknown, but probably selfish gain.

## Notes For The Compiler — Round 47

- **The deal is gone** — no exchange, no region retained, no protection from the Institute. What
  stands: an ally revealed the armada's plans to the enemy; the betrayer's intentions are
  **unknown, probably selfish gain**; where they are now is unknown. `the-protected-lands` deleted
  (it existed only as the deal's price); `the-betrayer`'s home is [[realm-06]], whereabouts open.
  Delahaye's revenge points at the Pirate realm, not at a named region.
- Rewritten on `the-betrayer`, `the-pirate-institute-war`, `wraith-delahaye`, `wraiths`, `pirates`,
  `the-recruitment-of-the-wraith`, `the-search-of-the-frozen-map`.

### Round 48 — 2026-09-22

**Q96 — Delahaye's ship, captain and home; the betrayer's name; the shape of the Pirate realm.**

> - Delahaye was the first-mate of a ship called The Drunken Mermaid. Her captain was also
>   Delahaye's romantic partner - Captain Anne.
> - The betrayer was a Captain of another ship called The Holy Socks. His name was d'Artigue. The
>   armada realised d'Artigue must have betrayed the armada as his ship didn't join the fleet, and
>   Delahaye's crew knew him to not be trustworthy.
> - The pirate realm is a series of islands. Delahaye's captain and crew controlled Tortuga. These
>   islands are loosely based of the Carribean islands where pirates were active.
> - In the pirate game every ship has a unique name and flag. Delahaye slowly realises so much
>   time has passed that she is unsure what she will find when she reaches the Pirate realm, but
>   one of her goals is to find what had happened to her crew and The Drunken Mermaid, and if her
>   home island of Tortuga is still controlled by ancestors of her crew.

## Notes For The Compiler — Round 48

- New character `captain-anne` (Captain of The Drunken Mermaid, Delahaye's romantic partner, held
  Tortuga; fate after the armada unknown). `the-betrayer` renamed `captain-d-artigue` (Captain of
  The Holy Socks; aliases keep "The Betrayer"). The in-world evidence is circumstantial — his ship
  did not join the fleet, and Delahaye's crew already distrusted him — recorded as such.
- New location `tortuga` (island in realm-06, held by Anne's crew). `realm-06` gains its shape: a
  series of islands, loosely based on the Caribbean islands where pirates were active.
- New items `the-drunken-mermaid` and `the-holy-socks` (type: ship). The rule that every ship in
  the Pirate game has a unique name and flag goes on `pirates-open-exploration`.
- Delahaye's goals in realm-06, on `wraith-delahaye` and `the-search-of-the-frozen-map`: find out
  what happened to her crew and The Drunken Mermaid, and whether Tortuga is still held by her
  crew's descendants — alongside revenge, and with her unsure what she will find. "Ancestors" in
  the author's text is read as descendants.

### Round 49 — 2026-09-22

**Q97 — The chapter restructure: spreading chapters two and three apart so parallel stories
converge, with the Damned's RTS starting early.** (The author's proposal, then feedback on the
compiler's response.)

> Actually, I'm thinking about spreading the current chapters apart so parallel stories can
> converge by having the damned gameplay start in an earlier chapter, playing the RTS and
> recruiting wraiths and other units in simple minigames until the Damned campaign reaches a
> certain stage and that stage includes recruiting a wraith that happens to be Delahaye. This
> will lead to world-building across the realms with the small minigames. I'm thinking:
> - Chapter 1 stays focused on the Robots, Celestials and the Institute
> - Chapter 2 keeps the Gargoyle focus but splits half the story into chapter 3, adds the Damned
>   RTS gameplay up to Delahaye breaking out of the minigame, celestial story needs to stay too
>   as the calling of ancient allies needs to happen here, but the amount of celestial gameplay
>   needs to be kept minimal.
> - Chapter 3 - the second half of chapter 2 is moved here; the remainder of the Gargoyle story
>   and the second half of the Wraith story of searching the world map and following val to the
>   trial of the gargoyle.
> - Chapter 4 - current chapter 3 is wholly bumped to chapter 4, this chapter would include the
>   assassination attempt on the Gargoyle that leads to the Wraith reavealing herself to the
>   Gargoyle and Ninja

> OK happy with this - please update the wiki. Some feedback on the chapter restructure:
> - I don't really care what glitch is first ... we don't need to pay special attention to that,
>   only need to keep track of the glitches so we track opportunities to present glitches
>   occurring to the player in an increasing frequency.
> - The player's interaction with the Damned realm while the game is frozen is the same and the
>   kingdom doesn't progress until Val returns to her castle after the trial of the gargoyle. On
>   her second time back to the Damned realm she notices the world is frozen - as she is
>   questioning what is going on the retcon engine kicks in causing a continuity glitch - this
>   glitch rewrites Val's memory of the freeze so that she didn't notice it but also unfreezes
>   the game. Now the play can continue playing their Damned kingdom.
> - Keep the ambush before the the council - if the meeting of the council doesn't have a note
>   add one called 'the first meeting of the Realm Champions'. The term Realm Champions is
>   created by the Templar at the meeting once she realises the people present are each from
>   different realms.
> - The reason for Delahaye to follow Kazuma seems to break, and she raises it, but Granite
>   points out that there are Five realms that have paths to the Pirate realm and the Robot realm
>   is one of them. As the ultimate goal of Kazuma is to get to the Robot realm and he is from a
>   realm connected to the Pirate realm, and Kazuma is known to have the power to open sealed
>   interplanar gates she reasons it makes sense to stick with him.
> The Damned game is a war of Damned kingdoms against each other for control of the various
> regions and points of interest of Damned realm. It's contained within the realm. The Guardians
> of Night intend to expand the Damned kingdoms into the Celestial realm - which in a later
> chapter (chapter 6 maybe?) the Templar takes the War Machine and starts counterattacking with
> it ... showing that the Damned are now defending the land they invaded in the Celestial realm
> and that plays like the Celestial game where the Damned have tower defences.

## Notes For The Compiler — Round 49

- **Chapters renumbered**: the old `chapter-03` (The Convergence) is now `chapter-04`; a new
  `chapter-03` is written; `chapter-02` rewritten. Every `chapter-03` reference under `Wiki/`
  (outside Logs, Handovers, Decisions) now points at `chapter-04`. Chapter shape as the author
  gave it, with the compiler's suggested three-thread close of chapter two accepted: the barrier
  broken from inside · the second signal detected and the Ninja departing · Delahaye breaking out
  and the kingdom freezing. Recorded as decision `spread-the-chapters-to-converge`.
- **Glitches are a register, not a race.** "First glitch" wording removed from
  `continuity-glitches`, `the-diagnosis-of-the-last-gargoyle` and `mifix`; a Glitch Register
  section on `continuity-glitches` lists every glitch the player can see, by chapter, so
  frequency can be tuned upward.
- **The unfreeze** is a new quest `the-unfreezing-of-the-kingdom` (chapter 3, realm-08, Val): on
  her second return she notices the freeze; the retcon engine rewrites her memory of noticing and
  unfreezes the game. Compiled as a hard-retcon on `the-retcon-engine`, `val`, `val-s-castle`,
  `damned-undead-kingdom-rts`.
- **The council** gets its own quest `the-first-meeting-of-the-realm-champions` (chapter 4);
  `the-convergence-at-the-monastery` keeps the arrivals. New lore `the-realm-champions` — the
  Templar's term. Delahaye's "why stick with Kazuma" exchange closes the council note: Granite
  knows the network's shape (five gates per realm; the Robot realm is one of the Pirate realm's
  five), Odie has just named Kazuma's power, and Kazuma's goal is the Robot realm.
- **The Damned's RTS** is a war of Damned kingdoms against each other for the regions and points
  of interest of realm-08, contained within the realm. The Guardians intend to expand the Damned
  kingdoms into the Celestial realm; in a later chapter (six, provisionally) the Templar takes the
  War Machine and counterattacks, and the Damned defend invaded Celestial land in the Celestial
  game's style with their own tower defences. On `damned-undead-kingdom-rts`,
  `the-guardians-of-night`, `celestials-hero-tower-defence`, `templar-ermengarda`.
- `chapter:` set on every Delahaye quest; the Damned's rows added to the chapter balance tables.
