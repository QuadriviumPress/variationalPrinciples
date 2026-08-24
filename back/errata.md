---
title: "Errata"
short_title: "Errata"
label: errata
---

# Errata

This page tracks corrections made in this MyST edition relative to the
[LibreTexts source](https://phys.libretexts.org/Bookshelves/Classical_Mechanics/Variational_Principles_in_Classical_Mechanics_(Cline))
that was crawled and converted to Markdown (see `scripts/html_to_myst.py` and
`scripts/build_book.py`). Two kinds of defects are recorded separately below:
issues introduced purely by the HTML → Markdown conversion, and issues that
were already present in the underlying LibreTexts/PDF text and have been
corrected here for readability and correctness.

## Conversion defects (fixed)

These were artifacts of the automated HTML → MyST conversion, not the
underlying textbook content. The `_table()` method in `scripts/html_to_myst.py`
originally built table cells with `self._inline(td)`, which converts `<br>` to
a literal newline, and the page-level `normalize_inline_math()` pass converted
any `\[...\]` display math to a multi-line ` $$ ` block wherever it occurred —
including inside table cells. Markdown pipe tables require one physical line
per row, so any cell containing a `<br>` or block math broke the table into
malformed extra rows. `_table()` has since been rewritten to force inline math
and collapse multi-line cell content onto one physical line, rendering as a
pipe table when every cell fits on one line and as a `list-table` directive
(which tolerates richer cell content) otherwise, so this does not recur on the
next `npm run convert`.

- **`back/glossary.md`** — the entire glossary table (all 87 entries) was
  broken below the first entry that contained a formula. Eleven entries
  (*Abbreviated action*, *Canonical coordinates*, *Characteristic function*,
  *Euler's hydrodynamic equation*, *Euler-Lagrange equation*, *Fermat's
  principle*, *Newton's First-order integrals*, *Generalized energy theorem*,
  *Hamilton's stationary-action principle*, *Inertia tensor*, *Poisson
  brackets*) had their definitions collapsed onto a single line with inline
  math. The *Euler's equations for rigid-body rotation* and *Jacobian*
  entries used the `eqnarray`/`equation` LaTeX environments without `$`
  delimiters at all, so they rendered as raw text instead of math; both are
  now wrapped in `$...$` (`eqnarray` converted to KaTeX-compatible `aligned`).
  Also removed: a leftover, book-irrelevant LibreTexts *template* row
  ("Words (or words that have the same definition) ... Eg. 'Genetic,
  Hereditary, DNA'") that had been pulled in verbatim from the glossary
  plugin's boilerplate instructions and rendered as if it were the book's
  first glossary entry.
- **`chapters/ch-15-advanced-hamiltonian-mechanics.md`** — Table 15.1
  (Hamilton–Jacobi summary table): three cells that each contain two stacked
  equations were splitting the table; now renders as a `list-table` with
  each cell's equations collapsed onto one line.
- **`chapters/ch-19-mathematical-methods-for-classical-mechanics.md`** — four
  tables of curvilinear-coordinate formulas (polar, cylindrical, spherical,
  and the Frenet–Serret/arc-length table) had "Unit vectors" and "Time
  derivatives of unit vectors" cells with 2–3 stacked equations each, and one
  cell containing a 3×3 rotation-matrix equation spread across ~14 lines with
  blank-line padding; all now render as `list-table` directives with each
  cell's equations collapsed onto one line.
- **`chapters/ch-13-rigid-body-rotation.md`** — a garbled aligned equation
  block for the perturbed Euler equations (§13.22): `\$I_3 − I_1)` should
  read `(I_3 − I_1)`, and a stray `\\(` between the second and third lines
  should have been the `\\` row separator. Also fixed an adjacent `\(\lambda
  \mu$` (mismatched delimiter) to `$\lambda \mu$`.
- **Stray `\$` where a closing inline-math delimiter should have been a
  plain `$`** — found in four chapters, each breaking the math immediately
  after it: `chapters/ch-10-nonconservative-systems.md` ($m=m_0e^{\Gamma
  t}$), `chapters/ch-04-nonlinear-systems-and-chaos.md` ($n\to\infty$),
  `chapters/ch-11-conservative-two-body-central-forces.md` ($\mathbf{r}$),
  `chapters/ch-06-lagrangian-dynamics.md` ($F_{q_i}^{EXC}$).
- **Duplicated words** from the source text, corrected in 14 places across
  chapters 3, 5 (×2), 6, 7, 8, 11 (×2), 12 (×4, including a figure `alt` text
  that duplicated its caption), 13 (×2), 15, and 16 — e.g. "the the", "to to",
  "it it", "frame frame", "equation Equation".

## Broken cross-references

An audit of the original equation cross-reference macros found five citations
that did not resolve to a defined target, from LibreTexts end-of-chapter
"review" sections that restate results using the *original* PDF's equation
numbering without re-attaching a label to the restated equations. One was
fixed here directly: the citation to equation 7.37 (used in
`chapters/ch-09-hamiltons-action-principle.md` for "Jacobi's Generalized
Energy ... was defined in Equation 7.37") pointed at an equation in
`chapters/ch-07-symmetries-invariance-and-the-hamiltonian.md` that had lost
its label; the definition of $h(\mathbf{q},\dot{\mathbf{q}},t)$ in §7.7 is the
only equation in the book matching that description, so the label was
restored there.

The book's subsequent full renumbering pass (which replaced the old
cross-reference macros throughout with resolved MyST links) independently
reconstructed the three other citations this pass had left unresolved —
equation 13.103 (`chapters/ch-13-rigid-body-rotation.md`), equation 7.38
(`chapters/ch-07-symmetries-invariance-and-the-hamiltonian.md`), and equation
9.2 (`chapters/ch-09-hamiltons-action-principle.md`) all now link correctly.

One case remains unresolved:

- `chapters/ch-08-hamiltonian-mechanics.md` — "Equation (a)" (line ~475,
  alongside a working link to equation `c`) has no equation tagged `(a)`
  defined nearby in that worked example; the nearest similarly-tagged
  equation (`eq-8-a1`) belongs to a different worked example later in the
  chapter, so it isn't a safe fix. Left as plain text pending someone with
  the source PDF confirming the intended target.

## Original-text corrections (fixed, tracked here)

These appear to be errors in the underlying textbook content itself (not
introduced by the Markdown conversion), corrected in this edition:

- **`chapters/ch-19-mathematical-methods-for-classical-mechanics.md`**
  (spherical coordinates table) — the unit vector
  $\mathbf{\hat{r}}$ was given as
  $\hat{i}\sin\theta\cos\phi + \hat{j}\sin\theta\cos\phi + \hat{k}\cos\theta$,
  repeating $\cos\phi$ for both the $\hat{i}$ and $\hat{j}$ components. The
  standard spherical-to-Cartesian unit vector is
  $\hat{i}\sin\theta\cos\phi + \hat{j}\sin\theta\sin\phi + \hat{k}\cos\theta$
  (confirmed against the $\hat{\phi}$ and $\hat{\theta}$ unit vectors listed
  immediately below it in the same table, which are internally consistent
  with $\sin\phi$/$\cos\phi$ alternating correctly). Corrected the $\hat{j}$
  component to $\sin\theta\sin\phi$.

## Notes / not changed

- **`back/glossary.md`** contains two separate entries titled *Euler-Lagrange
  equation* (one with a formula, one with a one-line prose definition) and
  duplicate near-entries such as *Constraints scleronomic* / *Scleronomic
  constraints* and *Constraints rheonomic* / *Rheonomic constraint*. These
  are left as-is since removing either is a content/editorial judgment call
  beyond what this pass covers, not a mechanical error.
