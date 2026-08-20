# paper/

LaTeX source for the manuscript, plus figures at the resolution the venue requires.

**Belongs here:** `.tex` source, `.bib` bibliography, figure files referenced by the
source, and the venue's own class/style files as obtained from the venue.

**Does not belong here:** style or class files written from memory or reconstructed by
hand. Venue templates are *fetched from the venue* and committed verbatim, with the
retrieval URL and date recorded in the commit message. A template that cannot be
fetched is recorded as an open action in `OUTSTANDING.md` and left absent — an
approximated template silently produces a non-compliant submission.

Also does not belong here: any number that is not traceable through `PROVENANCE.md` to
the script in `src/` that emitted it and the file in `results/` that captured it.

No venue is committed to yet. See `audit/VENUE.md`.
