# Measuring Stylistic Asymmetry in Large Language Models: A Stylometric Cross-Tradition Audit

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20612701.svg)](https://doi.org/10.5281/zenodo.20612701)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![R 4.3+](https://img.shields.io/badge/R-4.3%2B-276DC3.svg)](https://www.r-project.org/)
[![Reproducibility: Verified](https://img.shields.io/badge/Reproducibility-Verified-success.svg)](#reproduction--replication-pipeline)

> **Official Replication & Artifact Repository for:**
> *Measuring Stylistic Asymmetry in Large Language Models: A Stylometric Comparison of Generated Prose Across Literary Traditions*
> **Author:** Pegah Merrikhi
> **Permanent DOI:** [10.5281/zenodo.20612701](https://doi.org/10.5281/zenodo.20612701)

---

## 🖼️ Visual Overview & Empirical Gallery

<table>
  <tr>
    <td width="33%" align="center">
      <b>Graphic Abstract</b><br>
      <img src="figures/graphic abstract.png" width="100%"/>
    </td>
    <td width="33%" align="center">
      <b>Methodology Pipeline</b><br>
      <img src="figures/figure_methodology_design.png" width="100%"/>
    </td>
    <td width="33%" align="center">
      <b>Stylometric Divergence & MLS</b><br>
      <img src="figures/figure_1_divergence_and_mls.png" width="100%"/>
    </td>
  </tr>
  <tr>
    <td width="50%" align="center">
      <b>Stylometric Radar (Human vs. GPT-4o)</b><br>
      <img src="figures/figure_2_stylometric_radar.png" width="70%"/>
    </td>
    <td width="50%" align="center">
      <b>Expert Human Evaluation</b><br>
      <img src="figures/figure_3_human_evaluation.png" width="70%"/>
    </td>
  </tr>
</table>

---

## 📌 Executive Summary & Abstract

LLMs demonstrate remarkable fluency; however, their ability to faithfully reproduce literary styles across diverse traditions remains uneven. This repository contains the complete empirical dataset, stylometric extraction pipelines, and evaluation benchmarks for auditing **stylistic asymmetry** in GPT-4o.

We reveal a pronounced **"stylistic slope"**:
1. **Western Minimalist Prose:** near-native stylistic fidelity.
2. **Postcolonial Anglophone Prose:** moderate flattening.
3. **Persian Modernist Prose:** substantial degradation (Hapax collapse -26.79%; Plausibility 2.00/5).

---

## 📊 Comprehensive Results Tables

### Table 1: Computational Stylometric Benchmarks (Mean ± SD)

| Literary Tradition | Corpus | Burrows' Δ | MATTR | MLS | Hapax (%) |
|:---|:---|:---:|:---:|:---:|:---:|
| Western Minimalist | GPT-4o | 0.428 | 0.740 | 12.57 | 46.94 |
| Postcolonial | GPT-4o | 1.167 | 0.663 | 15.88 | 41.07 |
| Persian Modernist | GPT-4o | 2.689 | 0.580 | 14.57 | 32.14 |

### Table 2: Expert Human Evaluation (1–5 Likert)

| Literary Tradition | Plausibility | Coherence | Cultural Situatedness | Voice Authenticity |
|:---|:---:|:---:|:---:|:---:|
| Western Minimalist | 4.60 | 5.00 | 4.40 | 4.60 |
| Postcolonial Anglophone | 3.00 | 4.00 | 2.60 | 2.80 |
| Persian Modernist | 2.00 | 4.00 | 1.60 | 2.20 |

---

## 🏁 Key Conclusions
- **The Coherence Trap:** While the model generates syntactically coherent prose (Mean Coherence: 4.0/5.0), this masks a "stylistic collapse" in *Voice Authenticity* (2.2) and *Cultural Situatedness* (1.6) in non-Western traditions.
- **Asymmetric Representation:** The model loses its "idiosyncratic fingerprint" as it moves from canonical Western contexts to non-Western corpora.

---

## 📖 Citation

**APA 7th Format:**
> Merrikhi, P. (2025). *Replication Package for "Measuring Stylistic Asymmetry in Large Language Models"* (Version 1.0.0) [Data set & Software]. Zenodo. https://doi.org/10.5281/zenodo.20612701

**BibTeX:**
```bibtex
@misc{merrikhi2025stylistic,
  author = {Merrikhi, Pegah},
  title = {Replication Package for "Measuring Stylistic Asymmetry in Large Language Models"},
  year = {2025},
  publisher = {Zenodo},
  doi = {10.5281/zenodo.20612701},
  url = {https://doi.org/10.5281/zenodo.20612701}
}
