---
tags:
  - "decision"
topics: []
status: seed
created: 2026-08-08
updated: 2026-08-08
sources:
  - "Raw/Sources/interviews/faction-eleven-lore-and-design.md"
source_count: 1
aliases: []
decision_status: proposed
decided: ""
components: []
feature: ""
supersedes: ""
superseded_by: ""
---

# Release Faction Eleven In Chapters

Ship the game as a series of **chapters that progress the overall story**, rather than as one
complete ten-faction release.

**Chapter one is [[robots]]-led**: [[autofix]]'s story carries the main plot progression, with
**[[ninja]] and [[templar]] present as what will feel like mini-games**.

**Status:** proposed — the author's words were "I'm thinking that the game will be released in
chapters", which is an intent, not a commitment.

**Based on:** [[project-scope-and-constraints]], [[faction-genre-mechanics]]

## Context

One developer, commercial intent, and a design that commits to ten distinct genre systems
([[faction-genre-mechanics]]). A single-release ten-faction game means no revenue and no player
feedback until all ten genres are finished — which for a solo developer is the failure mode that
kills projects of this shape.

The author reports the most concrete ideas for five factions: [[ninja]] ([[institute-of-eight]]),
[[autofix]] ([[robots]]), the Knight/[[templar]] ([[celestials]]), [[gargoyle]]
([[green-skins]]) and [[conjurer]] ([[mystics]]).

## Options Considered

- **Chapters** — release incrementally, each chapter advancing the overall story. Trade-off: buys
  early revenue, early feedback, and a schedule that survives one person; costs the ability to
  freely revise earlier factions once players hold them, and demands the story be authored so
  that a partial multiverse is satisfying.
- **Single full release** — not discussed by the author. Trade-off: preserves total design
  freedom until the end; risks years of unpaid, unvalidated work.

## Decision

Chapters. **Chapter one = [[robots]] (main plot) + [[institute-of-eight]] and [[celestials]] as
mini-games.** Not yet firm as a release model, but the chapter-one composition is settled.

This is [[realm-01]], [[realm-02]] and [[realm-03]] — a **contiguous arc of
[[the-wheel-of-realms]]**, three mutually neighbouring realms that are historically friendly
with each other. The first chapter is therefore not three arbitrary factions but a connected
neighbourhood, which is both fictionally coherent and the smallest slice that can demonstrate
traversal between near realms.

## Chapter One, As Specified

| Faction | Form | Ends with |
|---------|------|-----------|
| [[robots]] (lead) | full — [[robots-incremental-exploration]] | sealed gates they cannot open alone; remote comms restored, waking the shrine bot ([[the-shrine-bot-awakens]]) |
| [[institute-of-eight]] | genuinely reduced — one cycle of boss fight, defeat, training, plus lore and the shrine | the gate guardian undefeated, but the gate **cracked** ([[the-cracking-of-the-gate]]) |
| [[celestials]] | genuinely reduced — one very simple tower defence | [[the-fall-of-the-outpost]]; retreat to [[templar-monastery]] |

## Chapter Two, As Sketched

- The [[celestials]] at [[templar-monastery]]: tower defence with platforming exploration between
  levels, a second defeat by the war machine, and [[the-calling-of-ancient-allies]] — the first
  deliberate reconnection in the game.
- The [[mystics]]' realm becomes a **major setting**.
- The [[robots]]' restored comms pay off a second time, hearing [[the-monastery-autofix-bot]].
- The [[institute-of-eight]]: the shrine bot detects a *second* mini-fix signal, leading [[ninja]]
  out through [[the-ancient-ruin]]'s abandoned cracked gate ([[the-second-signal]]).
- The [[green-skins]] enter: [[ninja]] meets [[gargoyle]], who is **very ancient** and wants to stop
  his own faction's war on the Celestials. They team up to find the bot — **which [[templar]] has**.

**Chapter two converges on a single object.** Three protagonists move toward
[[the-monastery-autofix-bot]] — the Templar holding it, the Robots hearing it, the Ninja and the
Gargoyle hunting it — and none of them knows about the others. That is a far stronger chapter
shape than chapter one's, and it means chapter two is where the game's premise finally *pays*
rather than merely sets up.

**Scope warning:** chapter two now involves five factions ([[robots]], [[institute-of-eight]],
[[celestials]], [[mystics]], [[green-skins]]) against chapter one's three, and two of them
([[mystics]], [[green-skins]]) have **no settled game style at all**. See
[[faction-design-status]].

### Chapter one's causal chain

The three factions are not parallel demos. They form one chain:

> [[ninja]] fights the guardian and loses → [[the-cracked-gate]] → [[autofix]]'s restored remote
> comms reach through the crack → [[the-shrine-bot-awakens]].

Meanwhile [[templar]] loses [[the-outpost]] and retreats, setting up chapter two. Every faction
fails, and the failures are what connect them.

## Consequences

Recorded as open questions rather than settled facts, since the decision itself is provisional:

- **A chapter is several factions with one lead.** One faction carries plot progression; others
  appear in smaller form. This resolves the trap noted below.
- [[protagonist-swapping-and-story-gating]] **can ship in chapter one**, because there are three
  factions to swap between. Had chapter one been a single faction, the mechanic that defines the
  game would have had nothing to demonstrate.
- **"Mini-game" resolved for the Ninja (2026-08-08): genuinely reduced.** Chapter one gives
  [[ninja]] a single cycle of boss fight → defeat → training, plus lore-building and the mini-fix
  bot in the family shrine. Not a vertical slice of the full faction, and not a diegetic
  novelty — a small, complete version of the loop that grows later without retcon. The same
  question is still open for [[templar]].
- **The Institute's gate does not open in chapter one.** [[ninja]] cannot open it until every
  faction has been introduced, which makes it a late-game turning point. Chapter one therefore
  ends with the Ninja *not* winning — and protects [[gargoyle]] and [[realm-09]] for the chapter
  where the Green Skins are actually built.
- **Chapter one has a spine:** [[the-shrine-bot-awakens]]. An ability earned in [[autofix]]'s
  incremental skill tree wakes the mini-fix bot in the Ninja's shrine, connecting the chapter's
  lead faction to its first mini-game. This is also chapter one's demonstration of
  [[protagonist-swapping-and-story-gating]].
- **[[autofix]]'s story is the one that must carry the mystery**, since it leads. The robots'
  sealed gates — which they cannot open alone — are already the perfect first contact with
  [[faction-eleven-antagonist]]'s work.
- The [[faction-eleven-antagonist]] reveal is distributed across the ten stories. Chaptering means
  committing to how much of that mystery each chapter pays off, before the later chapters exist.
- Whether ten factions is a **story requirement or an ambition** was asked and not answered; the
  chapter model makes it possible to defer that question, which is a benefit and a risk.
