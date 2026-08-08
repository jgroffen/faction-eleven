---
Title: "factions-retro prototype README"
Author: "Jim Groffen"
Reference: "factions-retro prototype repository, `README.md` at HEAD 3300b48 — a sibling project on the author's machine, supplied 2026-08-08"
ContentType:
  - "markdown"
  - "design-notes"
Created: 2026-08-08
Processed: true
tags:
  - "source"
---

# factions-retro prototype README

> Raw source material. Preserve the original context here. Do not rewrite this into a finished Wiki note — compile it into notes under `Wiki/` instead.

> **Provenance and status.** These are the author's *old* notes from an earlier prototype
> (`factions-retro`, a Commodore-format assembly project with sprite/character-set art). The
> author supplied them on 2026-08-08 as "your starting point on information for the factions",
> with the explicit caveat: **"we will need to go through each to determine what has changed."**
> Treat every claim here as legacy design pending confirmation, not as current canon.

## Content

## factions-retro (original document)

| Faction            | Protagonist | Role          | Game Type                |
| -----------------: | :---------: | :------------ | :----------------------- |
| Robots             | Autofix     | Medic         | Civ / Defender .. Crown  |
| Institute of Eight | Ninja       | Infiltrator   | Rogue-like / Isaac       |
| Celestials         | Templar     | Front Liner   | Tower Defence / FTL      |
| Mystics            | Conjurer    | Specialist    | Iso explorer / Diablo    |
| Fey Folk           | Phoenix     | Heavy Weapons | Bullet-hell / 1941       |
| Pirates            | Captain     | Commander     | 4X                       |
| Werebeasts         | Werewolf    | Front Liner   | RPG                      |
| The Damned         | Wraith      | Specialist    | Puzzle / point-and-click |
| Green Skins        | Gargoyle    | Infiltrator   | Stealth platformer       |
| Aliens             | Squidling   | Medic         | Choplifter / Metroid     |

Using pixelapp.com to draw sprites (24wx21h)

# Game Concept

Each faction has a unique feature, important to the final game mode when protagonists join up.

Features are unlocked through gameplay and also unlock progress, like Metroid.

## Game Navigation

Selecting a faction zooms into a world map for that faction if appropriate.

| Level | Map         |
| ----- | ----------- |
| 1     | Faction     |
| 2     | World       |
| 3     | Region      |
| 4     | Fast-travel |
| 5     | Location    |
| 6     | Encounter   |

## Start Screen

Pick any faction to play as the protagonist of that faction.

Cog to select a 'reality' and reset realities - save slots.

Returning to the select screen is only possible based on how that game works. Some require waypoints / camping. Others may be any time.

Faction map / start screen could be interesting ... z-axis=world maps and are circular. Would make for some interesting speedrun routing.

The faction selection screen could present progress for a faction, or progress in merging storylines as faction members join up.

## Reputation

Each protagonist has reputation with their faction. As other factions are
discovered, shorter reputation bars with those factions will appear. Reputation
can unlock game progress.

As you progress you will meet up with protagonists from other factions.
Reputation bars can merge as storylines merge. Representing this on The start
screen will be interesting.

# Story

There is a hidden faction referred to as the ancients, which are humans. They have locked the factions from each other.

There is a braille-like language that the ancients use. Should be fun to make the custom character set.

# Factions

## Robots

|                    |     |
| -----------------: | :-- |
| **Protagonist**    | Autofix |
| **Role**           | Medic |
| **Game Type**      | Civ / Defender of the Crown |
| **Currency**       | Parts |
| **Death Mechanic** | Restore-bot left outside of locations |

<table>
  <tr>
    <th>Game Description</th>
  </tr>
  <tr>
    <td>
      <p>Swap between location exploration and region control views.</p>
      <p>Starts with location exploration, search and recover / repair robots
      to build army, and destroy antagonistic robots. Some robots won't join
      but will give info or materials.</p>
      <p>Location exploration can discover adjacent locations. After clearing
      a location a world map opens that has locations of interest discovered
      and regions.</p>
      <p>This screen shows the player and allies as a unit, and the player can
      expand to more units. These can be used to control regions and expand
      into other regions.</p>
      <p>Ultimate goal is to control all regions and unite the robots. Moving
      the plot forward involves discovering the sealed interplane gates and
      finding rumors as to who created them, why they are sealed, and how to
      unseal them. In short, the robots can't unseal them on their own.</p>
    </td>
  </tr>
  <tr>
    <th>Story</th>
  </tr>
  <tr>
    <td>
      <p>The robots are old and defunct - they do not know how to fix
      themselves. Fearful of losing control of their creation, the creators
      destroyed the autofix bots once it was discovered autofix bots had the
      ability to not only repair damaged robots but create new robots from
      spare parts.</p>
      <p>The creators are long gone now, and the remaining robots slowly fell
      to disrepair and despair. While some bots found new purpose, others do
      not have the neural netowrk depth to develop a purpose and have shut down
      or gone insane.</p>
      <p>The robots with new purpose have developed varied goals, some
      constructive and some destructive.</p>
      <p>Decades later you awake alone in a ruined factory - a late-model
      Autofix - the only known functioning model with a full compliment of raw
      materials and plans for mini-fix bots.</p>
      <p>You alone represent a future for robots! But there are mysteries ...
      how did you survive the autofix purge? Why were you shut down and how did
      you awaken?</p>
    </td>
  </tr>
</table>

## Institute of Eight

|                    |     |
| -----------------: | :-- |
| **Protagonist**    | Ninja |
| **Role**           | Infiltrator |
| **Game Type**      | Rogue-like / Isaac with audio game queues |
| **Currency**       | Tablets |
| **Death Mechanic** | Cut-scene where their kid grows up, gets trained, and replaces them |

<table>
  <tr>
    <th>Game Description</th>
  </tr>
  <tr>
    <td>
      <p>A cycle of boss fight / defeat, and training to overcome the next
      boss phase / evolution.</p>
    </td>
  </tr>
  <tr>
    <th>Story</th>
  </tr>
  <tr>
    <td>
      <p>Starts with the player headed to the final boss fight very unprepared.
      The player is defeated because they don't have the skills required to
      progress in the fight.</p>
      <p>After their defeat the player is returned to their home where more of
      their back story is revealed. Their family are considered traitors and as
      punishment must endlessly fight the gate guardian.</p>
      <p>The family has a secret - an ancestor spririt housed in a small toy
      car. This toy is actually a mini-fix bot that has allied itself with the
      player to train the player's family to one day defeat the gate guardian
      so the mini-fix can get home.</p>
      <p>The gate guardian is protecting the gate to the Green-skins faction.
      This is when the player realises the gate was sealed and guarded for a
      reason. Player must then fight against waves of green-skins.</p>
      <p>Once the action settles down the player helps fortify the gate, but
      then goes through to work out what is on the other side.</p>
      <p>The player and mini-fix bot travel into the next faction and will
      meet the Gargoyle.</p>
    </td>
  </tr>
</table>

## Celestials

|                    |     |
| -----------------: | :-- |
| **Protagonist**    | Templar |
| **Role**           | Front Liner |
| **Game Type**      | Tower Defence / FTL |
| **Currency**       | Relics |
| **Death Mechanic** | TBD |

<table>
  <tr>
    <th>Game Description</th>
  </tr>
  <tr>
    <td>
      <p>Tower Defence where the player controls a castle that the player must
      upgrade between waves of enemies.</p>
      <p>Green-skins have war machines that attack. Eventually the Templar will
      take a war machine, start upgrading it and using it in defence, then take
      to the enemy.</p>
      <p>The templar and later allies from other factions act as hero units
      that have special powers to help in TD. Hero units level up and can get
      loot.</p>
    </td>
  </tr>
  <tr>
    <th>Story</th>
  </tr>
  <tr>
    <td>
      <p>This faction is under attack from both the Green-skins and Werebeast
      factions.</p>
      <p>This plane has gates that are open to both green-skins and werebeast
      faction planes.</p>
      <p>The green-skins attack relentlessly with many small units and
      occasional war machines.</p>
      <p>Werebeast faction attacks less frequently with fewer, very buff units.
      </p>
    </td>
  </tr>
</table>

## Mystics

|                    |     |
| -----------------: | :-- |
| **Protagonist**    | Conjurer |
| **Role**           | Specialist |
| **Game Type**      | Iso explorer / Diablo |
| **Currency**       | Scrolls |
| **Death Mechanic** | Use Homonculi |

<table>
  <tr>
    <th>Game Description</th>
  </tr>
  <tr>
    <td>
      <p>Simple progression of getting gear from dungeons, taking it to home
      cottage refine / enhance etc. Cottage has homonculi that retrieve gear
      and body, and revive you.</p>
    </td>
  </tr>
  <tr>
    <th>Story</th>
  </tr>
  <tr>
    <td>
      <p>Magicians live in towers / castles / cottages in the world.</p>
      <p>Above-world is friendly, and there are dungeons and an underworld.</p>
      <p>Deep in the underworld is an open gate to the green-skins faction
      that is how the dungeons keep repopulating.</p>
      <p>The green-skins have been mining the magic-rich plane.</p>
      <p><i>Could be Gargoyle and Conjurer meet up in this story.</i></p>
    </td>
  </tr>
</table>

## Fey Folk

|                    |     |
| -----------------: | :-- |
| **Protagonist**    | Phoenix |
| **Role**           | Heavy Weapons|
| **Game Type**      | 1941 / Bullet-hell |
| **Currency**       | Crystals |
| **Death Mechanic** | Reborn from ashes |

<table>
  <tr>
    <th>Game Description</th>
  </tr>
  <tr>
    <td>
      <p>TBD</p>
    </td>
  </tr>
  <tr>
    <th>Story</th>
  </tr>
  <tr>
    <td>
      <p>TBD</p>
    </td>
  </tr>
</table>

## Pirates

|                    |     |
| -----------------: | :-- |
| **Protagonist**    | Captain |
| **Role**           | Commander |
| **Game Type**      | 4X |
| **Currency**       | Booty |
| **Death Mechanic** | Pay the ferryman, losing booty |

<table>
  <tr>
    <th>Game Description</th>
  </tr>
  <tr>
    <td>
      <p>TBD</p>
    </td>
  </tr>
  <tr>
    <th>Story</th>
  </tr>
  <tr>
    <td>
      <p>TBD</p>
    </td>
  </tr>
</table>

## Werebeasts

|                    |     |
| -----------------: | :-- |
| **Protagonist**    | Werewolf |
| **Role**           | Front Liner |
| **Game Type**      | RPG |
| **Currency**       | Teeth |
| **Death Mechanic** | Revert to a puppy / baby for a bit |

<table>
  <tr>
    <th>Game Description</th>
  </tr>
  <tr>
    <td>
      <p>TBD</p>
    </td>
  </tr>
  <tr>
    <th>Story</th>
  </tr>
  <tr>
    <td>
      <p>TBD</p>
    </td>
  </tr>
</table>

## The Damned

|                    |     |
| -----------------: | :-- |
| **Protagonist**    | Wraith |
| **Role**           | Specialist |
| **Game Type**      | Puzzle / Point-and-click |
| **Currency**       | Return to grave / single spawn point |
| **Death Mechanic** | TBD |

<table>
  <tr>
    <th>Game Description</th>
  </tr>
  <tr>
    <td>
      <p>TBD</p>
    </td>
  </tr>
  <tr>
    <th>Story</th>
  </tr>
  <tr>
    <td>
      <p>TBD</p>
    </td>
  </tr>
</table>

## Green Skins

|                    |     |
| -----------------: | :-- |
| **Protagonist**    | Gargoyle |
| **Role**           | Infiltrator |
| **Game Type**      | Stealth Platformer |
| **Currency**       | Gold |
| **Death Mechanic** | TBD |

<table>
  <tr>
    <th>Game Description</th>
  </tr>
  <tr>
    <td>
      <p>TBD</p>
    </td>
  </tr>
  <tr>
    <th>Story</th>
  </tr>
  <tr>
    <td>
      <p>TBD</p>
    </td>
  </tr>
</table>

## Aliens

|                    |     |
| -----------------: | :-- |
| **Protagonist**    | Squidling |
| **Role**           | Medic |
| **Game Type**      | Choplifter / Terraria without mining |
| **Currency**       | DNA |
| **Death Mechanic** | Beamed up and restored? |

<table>
  <tr>
    <th>Game Description</th>
  </tr>
  <tr>
    <td>
      </p>Fly around above-ground clearing the area of enemies; The Damned
      faction. Once clear, go underground and clear enemies / rescue
      survivors.</p>
      <p>Build reputation with each other alien species by rescuing them
      and performing other tasks for them.</p>
    </td>
  </tr>
  <tr>
    <th>Story</th>
  </tr>
  <tr>
    <td>
      <p>Rescuing various aliens from the Damned faction that is attacking
      them.</p>
      <p>The damned have high-level liches that are opening gates to the alien
      worlds. The Damned have ancient lovecraftian gods that dwell in a void
      which connects alien space to the Damned plane.</p>
    </td>
  </tr>
</table>

## Notes for Compilation

- Confirms a roster of exactly ten playable factions, each with one named protagonist, a role, a
  game type, a currency and a death mechanic.
- **Contradiction with the 2026-08-08 interview:** this document names the Celestials protagonist
  **Templar**; the author referred to a **Knight** from the Celestials.
- **Contradiction / open question:** this document says the hidden faction is "the ancients, which
  are humans", who "locked the factions from each other". The interview describes the eleventh
  faction as the antagonist, and separately describes reality traversal as governed by natural
  cycles. Whether the Ancients *are* the eleventh faction, and whether the disconnection is
  caused or natural, is unresolved.
- Terminology drift: this document says **plane**; the interview says **reality**.
- Several game types here (4X, Civ, iso explorer, bullet-hell) do not obviously sit inside the
  interview's "platforming and top-down" common style.
- Fey Folk, Pirates, Werebeasts, The Damned and Green Skins have TBD descriptions and stories.
