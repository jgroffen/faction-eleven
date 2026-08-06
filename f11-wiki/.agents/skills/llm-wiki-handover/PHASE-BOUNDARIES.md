# Phase boundaries

A **phase** is a chunk of work inside a session — the grilling, the ingest, the lint fixing. A
phase ends when you think *"ok, we're done with that"*. The **phase boundary** is the gap between
two of them, and it is the only place this decision belongs. Mid-phase there is nothing to decide:
continue, or split what is left into subagents.

## Step 0: land the knowledge first

Before choosing anything below, ask what in this session is **knowledge** rather than **state**.

Knowledge becomes **notes**, whichever option you then pick. A handover carrying an explanation
that should have been a `concept` note is the failure this wiki exists to prevent — the
explanation dies with the handover when it is pruned, where a note outlives every session. Write
the notes, run `build` and `lint`, and only then decide the boundary.

This is what makes the tree below cheaper here than anywhere else: once the knowledge is in the
catalog, the conversation that produced it is much closer to disposable.

## The five options

| Option | What it does |
|---|---|
| **Continue** | Stay in the session. No context switch at all. |
| **`/clear`** | Empty the context window and start from nothing. |
| **Handover note** | `handover new` — a committed, searchable note the next session finds. |
| **Subagent** | Send the task to its own context window and get a report back. |
| **`/compact`** | Compress this context and carry on with the summary. |

## The tree

Work top to bottom at the boundary. The first **yes** wins.

**1. Can you continue in this session?** Yes when the next phase needs this one as a **primary
source** — the conversation verbatim, not a summary of it — or when there is simply enough room
left for the next phase to fit. Grilling → writing the notes is the standard yes: the notes want
the answers as they were given. Continue costs nothing and loses nothing, so rule it out first.

**2. Is the context irrelevant to what comes next?** If everything here — the searching, the dead
ends, the resolved branches — is disposable, **`/clear`**. It is the cheapest move on the board.

In a wiki this is a stronger option than it looks, because Step 0 changes the answer. Elsewhere,
clearing a relevant context loses the *why* behind the work and no amount of re-reading gets it
back. Here, if the session's knowledge is already in notes, the *why* is on disk and the context
really is spent. Write the notes, then clear.

**3. Do you need a handover note?** Narrower than it feels. You need one when you are:

- swapping to a **new harness** (Claude → Codex),
- moving to a **new directory** or repo,
- handing the work to a **colleague**,
- forking a side task you found **mid-phase**,
- or stopping for long enough that **a future session will have to find this by searching** —
  the wiki-specific case, and the one a scratch file cannot serve. The note is in the catalog, so
  a session weeks from now discovers it from `handover list` or `search-catalog` without being
  told a path.

**4. Can the task be done AFK?** Scoped tightly enough to run with nobody steering it? Send it to
a **subagent** and leave this session untouched. **llm-wiki-research** is the standard case: it
reads primary sources and comes back with a cited source file.

**5. Otherwise, `/compact`.** Relevant context, same harness, same directory, and you need to stay
in the loop. Pass it an instruction (`/compact we're about to fix source-lint`) so the summary
keeps what the next phase needs.

`/compact` is the **default, not the first reach**. It sits last because the four questions above
it are all cheaper or more precise. Starting here produces a fresh session that is confidently
wrong about a decision the summary flattened.

## Primary and secondary sources

Every move except **Continue** replaces the session as it happened with a summary of it:

| Source | Information | Noise | Room to move |
|---|---|---|---|
| Primary (Continue) | Full | Lots | Little |
| Secondary (`/compact`, handover) | Lossy | Less | Lots |

This is why question 1 comes first, and why Step 0 matters: a **note** is the one artifact that
escapes this table entirely. It was compiled to be read later, so it loses nothing by the session
ending.

## These are judgement calls

None of the questions is objective, and the same boundary can go two ways on two days. The value
is in asking them **in order**, at the boundary rather than in the middle of the work.
