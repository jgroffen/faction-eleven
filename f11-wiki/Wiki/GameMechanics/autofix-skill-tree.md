---
tags:
  - game-mechanic
topics: []
status: seed
created: 2026-08-12
updated: 2026-08-12
sources:
  - Raw/Sources/interviews/faction-eleven-lore-and-design.md
source_count: 1
aliases:
  - The Skill Tree
  - Autofix Upgrades
state: concept
category: progression
features: []
related_mechanics:
  - robots-incremental-exploration
  - minibot-command
  - robot-repair-puzzle
---

# The Autofix Skill Tree

[[autofix]]'s progression: **one tree, five branches**, paid for with **Data Fragments** — collected
from repaired robots ([[robot-repair-puzzle]]), not scavenged.

**Unlocking a skill is research, not training.** Autofix does **not have the schematics**; they are
no longer neatly available anywhere. He is **rediscovering the robots' own history and technology**
by studying the data he recovers from the machines he mends. Every unlock is lost knowledge
recovered, so the skill tree is an **archaeology of the robots' peak**, not an invention of
something new.

**State:** concept · **Category:** progression

**Implemented by:** _(no feature notes yet)_

## The Five Branches

| Branch | What it covers |
|--------|---------------|
| **Scrapping** | scrap collection efficiency; converting scrap into different kinds of **construction materials** |
| **Upgrades** | movement, **comms**, armour, diagnostics, **scanning range** (for diagnostics), **max controllable minibots** |
| **Fabrication** | **modules** and **components** |
| **Repair** | what kinds of damage can be fixed |
| **Robotics** | building minibots — and, behind a lock, **building Robots: true reproduction** |

Robotics is the branch with the story in it. Building whole robots is what the creators destroyed
the autofix line to prevent ([[robots]]), so the deepest node of the tree is the forbidden act.

### ACCESS DENIED

The **autonomous robotics** skills are not merely expensive — they are **blocked out, marked
`ACCESS DENIED`**. The player can see them and cannot buy them, from the first hour.

Unblocking them is the work of **later chapters**, and [[odie]] holds **hints on what is needed**.

This is the single best piece of design in the faction. A visible, locked branch labelled with a
refusal tells the player three things at once: that something is being kept from them, that
somebody did the keeping, and that the answer is not in this realm. It plants
[[faction-eleven-antagonist]] as a *user-interface element* long before the story names them — and
it ties the [[robots]]' survival to the multiverse reopening, which is what gives them a stake in
the ending.

## The Resource Chain

Nothing is bought directly with what you pick up. Everything refines:

> **scrap** (various kinds) → **construction materials** (via Scrapping) → **modules** and
> **components** (via Fabrication) → **repairs** and **minibots**

**Modules** — built under Module Construction, itself an unlock:

- Memory Module · CPU Module · GPU · DPU · MPU · **Quantum Core**

**Components** — built under Component Construction: various **sensors** and **effectors**.

Modules and components do double duty: they are what damaged robots need to be repaired
([[robot-repair-puzzle]]), *and* what minibots are built from ([[minibot-command]]). So every
module is a choice between fixing someone and building something.

## The Comms Ladder

The **Upgrades** branch carries the ladder that governs everything minibots can do. Each tier
unlocks a whole behaviour, not a stat:

| Tier | Unlocks |
|------|---------|
| **Short Range Comms** | *required to control minibots at all*; better/easier scrap collection; minibots as **followers** — which widens the pool of robots that can be repaired, and so yields more skill points and lore |
| **Long Range Comms** | minibots as **tools** — sent where Autofix cannot go, and used to gate exploration |
| **Extremely Long Range Comms** | minibots as **automation** — assigned to collect scrap **automatically** |
| **Quantum Comms** | better control again — and, by accident, the signal that escapes [[realm-02]] ([[the-first-signal]]) |

Note what the ladder implies alongside the rediscovery framing: Autofix is not inventing
inter-realm comms, he is **recovering** a capability the robots once had. Whether Quantum Comms
reaches other realms *by accident* or because it was **built to** is not stated — and the second
reading would mean the first signal is not an accident at all.

This ladder is the spine of the whole faction: **range is the progression**. Each tier buys a
different *kind* of play — companions, then puzzle tools, then an idle economy — so the genre of
the Robots' game changes as the tree grows rather than merely accelerating.

## Why It's Fun

Not yet defined. What is structurally true: **Data Fragments come from
repairing robots**, not from grinding scrap, so the progression rewards the thing the character is
*for*. Autofix gets stronger by healing his people, and learns his own history by doing it.

## Tuning

No values yet. The critical relationship is **Data Fragments from repairs** against **materials
from scrap** — one is finite and story-bearing, the other renewable.

## Used In

<!-- gd:used-in:start -->
<!-- gd:used-in:end -->

## Related

- [[robots-incremental-exploration]] — the faction game style this tree drives.
- [[minibot-command]] — what the Robotics branch and the comms ladder produce.
- [[robot-repair-puzzle]] — where skill points come from.

## Open

- Whether **Quantum Core** relates to **Quantum Comms** — the naming implies the module is what the
  comms tier needs, but that is not stated.
- **What unblocks `ACCESS DENIED`**, beyond that [[odie]] has hints and later chapters do the work.
- Who wrote the block. A machine-readable refusal implies an author.
- Whether upgrades are ever mutually exclusive, or the tree is fully completable in one run.
