---
tags:
  - game-mechanic
topics: []
status: seed
created: 2026-08-14
updated: 2026-08-14
sources:
  - Raw/Sources/interviews/faction-eleven-lore-and-design.md
source_count: 1
aliases:
  - Green Skins Game Style
  - Gargoyle Game Style
state: concept
category: exploration
features: []
related_mechanics:
  - exploration-core-loop
  - faction-genre-mechanics
  - ninja-rhythm-platforming
---

# Gargoyle — Stone Metroidvania

The [[green-skins]]' game style, **replacing** the prototype's bare "stealth platformer" label. It
runs on **the same platforming engine as [[ninja-rhythm-platforming]]**, with a different move set
and **no rhythm layer** — and it is structured as a **Metroid-style** game: a gated map opened by
acquiring abilities.

The [[gargoyle]] **starts with almost nothing.** His entire opening kit is *stealth while
stationary*. Everything else on the ladder below is earned.

**State:** concept · **Category:** exploration

**Implemented by:** _(no feature notes yet)_

## How It Works

**One substance, many verbs.** Every ability the Gargoyle has is a variation on being made of
**stone** — which is what makes the ladder read as one character growing rather than a list of
pickups. The author's set, given as incomplete and unordered:

| Ability | What it does |
|---------|--------------|
| **Stone-form** | Stealth **only while not moving**. The starting kit. |
| **Stone strength** | Move heavy obstacles. |
| **Glide** | Span otherwise impassable gaps; avoid obstacles. |
| **Stone-stealth** | Stealth at **slow speed** — the restriction loosens rather than lifts. |
| **Stone strength 2** | Move heavier obstacles, and **break** some. |
| **Stone-drop** | Stone-form **while jumping**: break weak ground from a height, and **knock out** opponents. |
| **Double jump** | He can flap **once**. |
| **Triple jump / quad jump** | Successively closer to true flight. |
| **Gargoyle flight** | Full flight. |
| **Gargoyle Legacy** | Final unlock — **sonic flight, super strength, super fortitude**. |

**He does not fight.** Settled by the author: the Gargoyle **wants to protect and save the
green-skins** — gargoyles see themselves as **protectors** — so there is no combat verb in the
kit at all. **Stone-drop knocks opponents out**, which is the closest he comes: he can *neutralise*,
never kill. This makes his Metroid a **pure traversal-and-stealth** Metroid, where a locked door is
opened by a movement ability rather than by the right weapon.

**Upgrades are found, not trained.** The Gargoyle unlocks abilities by finding **Gargoyle lore
fragments** in the world — so his progression is also how the player learns what a gargoyle *is*.
Growth and exposition are the same collectible.

**Failure costs progress, not life.** The Gargoyle's story does not involve dying in his own realm.
Being caught **resets the section** and forces him back to its start. Abilities once gained are
**permanent** — the player loses position, never capability.

**Why he is sneaking varies by section.** Sometimes it is subversion of the invasion; sometimes
being caught simply means he is **thrown out** of wherever he is. The stealth is not one uniform
fail-state but a per-section framing.

## The Ninja In Realm 09

Under [[realm-governs-game-style]], the [[ninja]] plays the **same Metroid structure** when he
crosses into [[realm-09]] in [[chapter-02]] — the rhythm layer stays home in [[realm-01]], and his
progression becomes ability-gated too.

But he acquires abilities **his own way**, keeping the Institute's model intact: he finds a
**challenge room**, [[mifix]] and the Ninja have a **dialogue**, and then he **learns the new skill
by practising it in the room**. So realm-09 holds two kinds of upgrade node — the Gargoyle's lore
fragments and the Ninja's challenge rooms — and they characterise the two protagonists in exactly
opposite terms: one **remembers** what his kind could do, the other **trains** until he can.

The challenge rooms are also where the Ninja's [[ninja-rhythm-platforming]] skill-based platforming
survives inside a Metroid: hard, self-contained, optional-feeling rooms in a map otherwise built for
exploration.

**[[mifix]] is the save/restore mechanic in realm-09.** The companion who lets the Ninja retry in
chapter one becomes, mechanically, the save point in chapter two — so the Ninja and the Gargoyle
share a map with **different failure models**: the Ninja restores from Mifix, the Gargoyle restarts
the section.

## Why It's Fun

Not stated by the author in those terms. What the design reaches for is legible: a character who
begins unable to do anything except **hold still**, and ends in **sonic flight** — the widest
power-curve of any faction, on a map that has been quietly showing you the places you could not
reach the whole way up.

## Tuning

No values yet. The knob that matters is **where flight lands** — see below.

## Scope And Pacing Risk

Two, both real:

- **Metroidvania is the most content-hungry genre on the roster.** A linear platformer ships level
  by level; an interconnected map is not playable until the loop closes. That fights
  [[chapter-based-release]] harder than any style chosen so far. The mitigation is already in the
  design: **two protagonists traverse the same map**, so realm-09 is built once and played twice.
- **Flight ends level design.** Double → triple → quad → full flight is four rungs on a single
  axis, and once the player can fly, gaps, walls and verticality stop gating anything. Metroid puts
  its equivalents last for this reason. **How much of the ladder belongs in chapter two is
  undecided** — flagged, not resolved.

## Used In

<!-- gd:used-in:start -->
<!-- gd:used-in:end -->

## Related

- [[exploration-core-loop]] — the shell; this is its platforming presentation.
- [[ninja-rhythm-platforming]] — the same engine, a different move set, no rhythm.
- [[realm-governs-game-style]] — the decision that makes this style apply to visitors too.
- [[faction-genre-mechanics]] — the per-faction genre layer this is an instance of.
