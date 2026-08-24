---
tags:
  - game-mechanic
topics: []
status: seed
created: 2026-08-19
updated: 2026-08-19
sources: []
source_count: 0
aliases:
  - Glitches
  - Continuity Errors
state: concept
category: narrative
features: []
related_mechanics:
  - protagonist-swapping-and-story-gating
---

# Continuity Glitches

The world does not quite add up, and the player can catch it. Every time a god edits a realm, the
realm writes history to cover the edit ([[the-retcon-engine]]) — and the cover story holds locally
but not globally. **The seams are the evidence trail to what the game actually is.**

**State:** concept · **Category:** narrative

**Implemented by:** _(no feature notes yet — no code exists)_

## How It Works

The rule: **a realm's account of itself is airtight from inside and contradicts the realm next
door.** The player is never given a character who lies. They are given ten realms whose stories
cannot all be true at once, and a structure that walks them through all ten.

**The name is diegetic.** There is an actual system called [[the-continuity-system]], built by
[[quetzalcoatl-the-white]] to track the world's evolution into key continuity events and **reject
anything that would break them**. A continuity glitch is that system not holding.

**And the rule above is not a rule. It is arithmetic.** [[the-retcon-engine]] repairs continuity
errors **reactively and locally** — it only acts on an error once detected, and it never has the
scope of all ten histories when it chooses what to change. A repair mechanism that can see one realm
at a time can only ever produce history that is **coherent in that realm and contradictory next
door.** The design does not have to author that property; the fiction manufactures it.

**Most glitches are made by the repair, not merely revealed by it.** Brute-forcing a change into
history that already happened is itself destabilising, and a fix that solves the detected problem
can seed several unforeseen ones in realms whose histories were never compatible. Those get detected
and patched in turn. **The player is walking through the exhaust of a machine trying to help.**

Four kinds, in rough order of how loud they are:

| Kind | What the player sees |
|---|---|
| **Continuity** | Two realms give incompatible accounts of the same event or object |
| **Chronology** | Something is older than it can possibly be — a guardian placed within memory that everyone remembers as ancient |
| **Foreign object** | A thing from another realm, with no local history and no explanation for how it got here |
| **Witness** | A character whose memory predates a retcon and does not match the record |
| **Leakage** | A fragment of the outside — an avatar in one of the four colours, a scrap of lore about a place with no name ([[the-four-developers]]) |

### Two Tiers Of Loudness

Every glitch is authored at one of **two tiers**, and the tier is what gets budgeted per chapter
([[story-continuity-timeline]]):

| Tier | The player… | Deniability |
|---|---|---|
| **Subtle** | may pass it entirely, and the story does not depend on catching it | total — it reads as flavour |
| **Strong** | cannot miss it | thin — and must still not read as a bug |

**Kind and tier are independent.** Any of the five kinds can be written at either tier: a continuity
contradiction can be a throwaway line in one realm's scripture or a monument that flatly refutes the
one next door. The kind is *what the glitch is*; the tier is *how hard it pushes*.

The two are budgeted differently. **Subtle glitches can be dense**, because missing one costs the
player nothing — they accumulate into a feeling. **Strong glitches are rationed**, because each one
spends deniability, and a player who reaches for a patch note has stopped playing the mystery.

**Leakage is the loudest kind and needs the most care.** It is the only one that shows the player
something rather than asking them to infer it, so it is also the one most likely to be read as a bug
in the real game rather than a clue. Use it sparingly and early: four recurring colours are a pattern
the player can carry for a very long time without an explanation.

**The delivery mechanism is [[protagonist-swapping-and-story-gating]].** A glitch is only visible to
someone who has been in two places, so the mechanic that braids the ten stories is also the mechanic
that makes the mystery detectable. Nothing extra needs building to surface them — they surface when
the player does what the game already asks.

**Most characters cannot see them; the player always can.** Ordinary inhabitants absorb a rewrite
completely and behave as though the new continuity was always the case. The player holds ten realms
at once. This is the same asymmetry the game already uses in [[the-smashing-of-the-gargoyles]], where
the player watches a cutscene the protagonist has no memory of — scaled up to become the spine of the
mystery.

**But there is a short list of characters who do see them, by two separate mechanisms**, and the
list includes a chapter-one protagonist:

- **Code sight.** A fixbot's heal repairs the *code* of whatever it is fixing, so a retcon is visible
  to it as an edit ([[a-heal-is-a-patch]]). [[autofix]], [[mifix]] and [[odie]] all have it.
- **Preserved memory.** Dormancy keeps a mind out of the retcon's reach — [[gargoyle]]'s torpor and
  [[odie]]'s stand-by both do it.
- **The liches** are the only ones who both see *and* explain, and they present real knowledge of the
  realms' infrastructure as **ancient eldritch lore** ([[the-void]]).

**Seeing, understanding and self-trust are three different things**, and no character has all three
— the ladder is set out in [[a-heal-is-a-patch]]. That is what keeps the witnesses from short-circuiting
the mystery: every one of them is missing a different piece.

**[[gargoyle]] is the loudest case.** He wakes with an unedited memory of the world before his torpor
and a realm whose history has moved underneath him. He is a continuity checker by construction, and
unlike the fixbots his evidence is a *narrative* contradiction rather than a diff — which is why he
carries the mechanic for the player even though he is not the first to notice.

**That makes him the tutorial for the mechanic, not the first instance of it.** Glitches are
everywhere from the start, because they date from [[the-linking-of-the-realms]] and were never
cured — [[realm-01]]'s lore still glitches, and its lore still adjusts itself to fit. A glitch needs
no in-fiction witness at all; the player is the detector. Chapter one's realms are as glitched as
any, and what chapter two adds is a character who can **say so out loud**.

## Why It's Fun

The pleasure of noticing. A glitch is never pointed at; it rewards the player who was paying
attention in a realm they left three hours ago, and it converts *having played the other stories*
into a form of competence. It also gives a ten-protagonist structure a reason to exist beyond
variety — the breadth **is** the detective work.

The risk to manage: a glitch the player reads as a **bug in the real game** rather than a clue is a
glitch that has failed. Deniability must run one way only — strange enough to notice, never so
strange that the player reaches for a patch note.

## Tuning

No values yet. The knobs to expect:

- **Density** — how many are placed per chapter. **The rate climbs, and it should accelerate rather
  than rise steadily.** The fiction supplies the curve: [[the-retcon-engine]] is a feedback loop in
  which each repair seeds further errors, so the count compounds rather than grows linearly
  ([[the-four-developers]]). The player's growing sense that something is wrong is measurement, not
  mood — which means density is a storytelling instrument rather than a difficulty setting.
- **Loudness** — the **subtle/strong** split above, and how many of each a chapter carries. The two
  tiers ramp differently: subtle density can climb freely, strong instances are spent carefully.
- **Confirmability** — whether the player can ever *check* a suspicion, or only accumulate them.
- **Acknowledgement** — which characters notice out loud, and how often. This is now a real budget
  rather than a question: [[autofix]], [[mifix]], [[odie]], [[gargoyle]] and the liches can all
  notice, and **acknowledgement buys deniability.** A glitch a character remarks on cannot be read as
  a bug in the real game, so **strong-tier glitches are safest in their company** and must be spent
  more carefully everywhere else ([[a-heal-is-a-patch]]).

## Used In

<!-- gd:used-in:start -->
<!-- gd:used-in:end -->

## Related

- [[story-continuity-timeline]] — where the per-chapter budget of each tier is tracked.
- [[the-retcon-engine]] — what produces them.
- [[the-four-developers]] — what they are evidence of.
- [[the-ancient-language]] — the other evidence channel, and the more legible one.
- [[protagonist-swapping-and-story-gating]] — how the player comes to hold two facts at once.
