---
tags:
  - quest
topics: []
status: seed
created: 2026-08-08
updated: 2026-09-15
sources:
  - Raw/Sources/interviews/faction-eleven-lore-and-design.md
source_count: 1
aliases:
  - The Shrine Bot Awakens
quest_status: design
quest_type: main
chapter: chapter-01
giver: ""
location: realm-02
mechanics:
  - robots-incremental-exploration
  - protagonist-swapping-and-story-gating
rewards: []
prerequisites:
  - the-cracking-of-the-gate
---

# The First Signal

The story event that ties chapter one together, in three beats across two realms: [[ninja-kazuma]]'s defeat
**cracks** a gate, [[mifix]]'s long-unheard call gets through it and **wakes** the frozen [[autofix-alto]],
and Autofix **answers**.

**Status:** design · **Type:** main · **Chapter:** [[chapter-01]] · **Location:** [[realm-02]]

> **Nobody involved knows they are cooperating.** The Ninja makes an opening by losing. Mifix has been
> calling into silence for generations. Autofix is not conscious for the first half of his own
> chapter's central event.

## The Beat

### 1 — The crack

[[ninja-kazuma]] returns to [[the-gate-guardian]] with a newly trained skill, loses again, and the fight
**cracks the gate** to [[realm-02]] ([[the-cracking-of-the-gate]], [[the-cracked-gate]]). That crack
is the only hole in the Robot Realm's seal, which has been total: a sealed realm stops signals as well
as travellers ([[allied-faction-signals]]), so nothing has gone in or out in living memory.

### 2 — The wake

For generations the [[institute-of-eight]] have kept an ancestor spirit in a small toy car. It is
really a **mini-fix bot**, awake the whole time, training the family and **calling home** so that one
day it can get back there. Nothing has ever answered, because nothing could hear it.

Now something can. Mifix's call goes through the crack, and what it carries is his **activity log** —
the working record of generations spent repairing things in a realm he was never written for.

On the other end of it, in a ruined factory, [[autofix-alto]] has been **frozen**: caught in a paradox in
his logic loop, hit when he tried to fix a foreign object from another realm and could neither
classify it nor let it go. The log resolves the paradox, because it is the record of a machine doing
that exact thing and surviving it. It teaches him the rule he lacked:

> **You can fix things that aren't robots if you study them enough. If you don't know how to fix them
> yet, don't try.**

**Autofix wakes.** The machine that saves him is one he built himself, and neither of them knows it.

### 3 — The answer

Autofix's story plays out in [[realm-02]] and he unlocks **Quantum Comms**
([[robots-incremental-exploration]]) to better control the minibots he has learned to build — a local
upgrade with a local purpose. Through the same crack, his answer reaches **both** mini-fix bots:
[[mifix]] in [[realm-01]], and [[odie]] in [[realm-03]].

**They are detectable, not reachable.** The distance is too great to communicate — Mifix knows
something is there and nothing more. Contact is a fact, not a conversation, which is what makes it
worth crossing realms to chase.

## Ordering

The three beats are **causally ordered and cannot be reshuffled**: no crack, no wake; no wake, no
answer. That is a change from a chapter whose two conditions could be met in either order, and it
constrains chapter one's structure rather than merely describing it.

| # | Beat | Faction | Depends on |
|---|------|---------|------------|
| 1 | [[ninja-kazuma]] cracks the guarded gate in the boss battle | [[institute-of-eight]] | — |
| 2 | [[mifix]]'s call and activity log wake [[autofix-alto]] | [[robots]] + [[institute-of-eight]] | beat 1 |
| 3 | [[autofix-alto]] unlocks **Quantum Comms** and answers | [[robots]] | beat 2 |

## Why It Matters

This is the **first cross-realm contact in the game**, and it happens between [[realm-01]] and
[[realm-02]] — **neighbours on [[the-wheel-of-realms]], historically friendly**. The oldest
alliance in the setting is the first one to come back.

It is also the **first worked example of [[protagonist-swapping-and-story-gating]]**, and a
two-sided one: it needs a defeat suffered in the [[institute-of-eight]]'s story *and* an ability
earned in the [[robots]]'. Neither faction alone can produce it.

**The chapter's payoff is a rescue nobody performs.** The Ninja makes an opening by failing at
something else entirely. Mifix does not send the log deliberately — he sends what he always sends, and
this time it arrives. Autofix is unconscious throughout and wakes up fixed. Three parties solve a
problem none of them knew about, which is the game's thesis executed once, small, in its first hour
([[story-outline-requirement]]).

Note who does what: the Ninja makes the opening and does not know what he has done; the robots earn
the ability and cannot use it until someone else acts first.

## Open

- Who "gives" this quest is undefined — it is a story beat inside the Robots' own line rather than
  something an NPC hands over.
- **How much of [[realm-02]] is playable before the wake.** The beats are strictly ordered, so either
  the Robots' story opens after the Ninja's, or the pre-wake portion is played as something other than
  Autofix. Undecided, and it is the chapter's biggest structural question.
- **Which trained skill** lets the Ninja progress to the boss battle and crack the gate — to be
  determined ([[ninja-rhythm-platforming]]).
- Does [[autofix-alto]] know his answer was received? The stronger version is that the player knows and
  Autofix doesn't.
- Whether the player is shown the paradox and the freeze, or only its resolution.
