---
name: gdd-quest
description: This skill should be used when the user asks to "design a quest", "add a mission", "write a quest line", "lay out a story beat", or "add a side quest" in a vault with the game-development plugin. It interviews the user, wires the quest to its giver/location/mechanics/rewards/prerequisites, creates a grounded quest note, and keeps the quest sequence spoiler-safe.
---

# Game Development: Design a quest

Turn a story idea into a `quest` note — wired to its giver, its place, the mechanics it leans on,
its rewards, and the quests that must come first — without spoiling, or being spoiled by, the
quests around it.

## Preconditions

- The vault has the plugin installed (`python3 scripts/wiki_tool.py plugins` lists
  `game-development`). If not, install it — see the repo's plugins/README.md.
- The world it references exists. A quest links to a `character` giver, a `location`,
  `game-mechanic`s, `item` rewards and prerequisite `quest`s — author missing pieces first
  (**gdd-worldbuild** for people/places/items, **gdd-mechanic** for systems).

## Steps

1. **Load the prompt template** from the vault's `_prompts/quest-design.md`.
2. **Ground it:** `list-notes --tag character` (giver), `--tag location`, `--tag game-mechanic`,
   `--tag item` (rewards), `--tag quest` (prerequisites). Create anything missing before linking.
3. **Interview** for the hook, the objectives (observable, in order), the place and giver, the
   mechanics it exercises or teaches, the reward, and the ordering/prerequisites.
4. **Create it:**
   ```bash
   python3 scripts/game_tool.py new-quest --title "Light the Braziers" --type main \
       --giver vess --location thornvale --mechanic ember-crafting --reward cinder-key \
       --prereq reach-thornvale --status design \
       --summary "Vess needs the braziers relit before nightfall."
   ```
   Fill `## Hook`, `## Objectives`, and `## Notes`. `## Rewards` / `## Prerequisites` track the
   linked items and quests.
5. **Run the spoiler check** (below) whenever you set a `--prereq`.

## Keep the sequence spoiler-safe

Quests are played in an order constrained by `prerequisites`. The invariant: **nothing in a quest
may reveal the outcome of a quest that lists it as a prerequisite; a quest may assume anything its
prerequisites established.** When you add a `--prereq`, read both quests and check the hook,
objectives, rewards and any character lines in both directions. Fix by rewording, resequencing
which is the prerequisite, or splitting the reveal. The tool records the dependency; keeping the
writing clean is the design work.

## Guardrails

- **Author before you link** — the tool rejects a giver, location, mechanic, reward or prereq that
  doesn't exist.
- A quest is content (one thing to do). The *system* behind a class of quests is a `game-mechanic` or a
  software-development `feature`, not a quest.
- Objectives must be observable ("read Vess's three letters", not "understand her motives").
- Move `--status` along as it's built (`blockout` → `scripted` → `shipped`) so `status` is honest.

## Done when

The gate passed, the quest is wired to real world notes, its objectives are checkable, and its
prerequisites don't create a spoiler.
