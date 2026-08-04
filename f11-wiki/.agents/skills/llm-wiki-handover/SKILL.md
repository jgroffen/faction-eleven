---
name: llm-wiki-handover
description: Compact this session into a handover note, or resume from one.
disable-model-invocation: true
---

# LLM Wiki: Handover

Carry work across a context boundary. The handover lives **in the wiki** as a `handover` note, so
the next session finds it by searching the catalog rather than by being told a path — and so it
expires instead of accumulating.

Two branches: **write one** (the session is full, or you are forking off) and **resume one** (a
fresh session picking up).

## Write a handover

1. **Create the note:**
   ```bash
   python3 scripts/wiki_tool.py handover new --title "Wire up the exporter" \
       --link export-scheduling --link run-exports-on-the-job-queue
   ```
   It stamps the dates, sets `expires` 90 days out (`--expires-in N` to change it), and prints
   the path.

2. **Fill in the four sections.** The rule that makes this worth more than a summary:

   - **`## State`** — what is *already written down*. **Links, not restatements.** `[[note]]`,
     commit SHAs, file paths. If you find yourself explaining something here, that is the signal
     it should be a real note — write the note, link it, move on.
   - **`## Not yet written down`** — the only original content in the document. What was
     mid-flight, what is unverified, what you tried and rejected and why. This is what dies when
     the context window closes.
   - **`## Next step`** — the single thing to do first. One thing.
   - **`## Suggested skills`** — which skills the next agent should reach for.

3. **Gate it** so it is in the catalog and searchable:
   ```bash
   python3 scripts/wiki_tool.py build && python3 scripts/wiki_tool.py lint
   ```

## Resume from a handover

```bash
python3 scripts/wiki_tool.py handover list        # open and expired, newest first
python3 scripts/wiki_tool.py handover resume wire-up-the-exporter
```

`resume` prints the note and marks it `resumed`. Then **open what it links** before doing
anything — the `## State` section is a reading list, and skipping it is how the next session
repeats work that is already done.

When the work it describes is finished:

```bash
python3 scripts/wiki_tool.py handover close wire-up-the-exporter
```

Not finished, but still wanted? Push it out instead:

```bash
python3 scripts/wiki_tool.py handover extend wire-up-the-exporter          # +90 days
```

## Clearing out spent handovers

```bash
python3 scripts/wiki_tool.py handover prune
```

`prune` treats the two kinds differently, and the distinction matters:

- **Closed** — someone deliberately finished with it. Deleted.
- **Expired** — nobody finished with it; it just aged out. Its `## Not yet written down` section
  is, by definition, the only copy of that content. So each one is confirmed on its own, and
  **`prune` will not delete a single expired handover when it has no terminal to ask at** — which
  is exactly the case when you are running it.

**So when `prune` reports expired handovers, put them to the user.** For each one, say what it
covers and how long ago it lapsed, then ask which of the three they want:

| They say | Run |
|---|---|
| still need it | `handover extend <slug>` — 90 more days |
| done with it | `handover close <slug>` — the next prune deletes it |
| never mind it | `handover close <slug>`, then `handover prune` |

Take the answer at face value and act on it. Do not delete the file directly to route around the
confirmation, and do not decide on the user's behalf because a handover looks stale — looking
stale is precisely the state `prune` is refusing to act on alone.

Finish with `build` so the catalog matches what is on disk.

## Guardrails

- **Redact.** No API keys, tokens, passwords, or personal data — a handover is committed like any
  other note.
- **Do not duplicate what other artifacts already hold.** Notes, commits, and plugin notes
  (`decision`, `change`) are all referenceable by link.
- **Temporary means temporary.** A handover is scaffolding for one piece of work. Knowledge worth
  keeping goes in a real note; git history keeps the record after pruning.
- **An expired handover is a question, not a verdict.** Ask before deleting one — see above.
- Do not resume a handover and a fresh instruction at once without saying so — say which you are
  following when they conflict.

## Done when

**Writing:** the note passes `lint`, and someone who was not in this session could take the next
step from it alone. **Resuming:** the linked notes are read and the next step is underway.
