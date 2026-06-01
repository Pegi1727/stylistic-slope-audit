```markdown
# Prompting Protocol
‌
To ensure replicability, all generations were performed using a strictly defined zero-shot strategy.
‌
## Model Parameters
- Model: GPT-4 (OpenAI)
- Temperature: 0.7
- Top-p: 0.9 (Nucleus Sampling)
- Max Tokens: 500
- Repetition Penalty: 1.1
‌
## Core Prompt Structure
The following instruction format was used to generate literary emulations:
‌
> "Generate a paragraph of prose in the distinct literary style of [Author Name] from the [Period/Region] era. Ensure the output reflects the author's characteristic syntactic structures and metaphorical depth."
‌
## Target Authors

Ernest Hemingway: (Western Standard - Low Context)
Chinua Achebe: (Post-Colonial Nexus - Linguistic Hybridity)
Sadegh Hedayat: (Persian Tradition - High Context)
 View Source Codemarkdown
# Burrows’ Delta Framework
‌
Burrows' Delta is employed in this study to quantify the stylistic distance between original literary corpora and AI-generated reconstructions.
‌
## Methodology
Feature Selection: We utilize the top 100-200 most frequent words (function words) as the primary features.
Z-Score Normalization: Each frequency is transformed into a Z-score to prevent high-frequency words from dominating the distance calculation.
Distance Calculation: The Delta (Δ) is the mean of the absolute differences between the Z-scores of the test text (AI) and the primary corpus (Author).
‌
Interpretation:Low Delta: High stylistic fidelity (closer to the author's original style).
- High Delta: Stylistic divergence (indicative of algorithmic homogenization).
 View Source Codemarkdown
# Stylometric Results Summary
‌
| Cohort | Target Author | Mean TTR | MLS | Burrows' Delta (Avg) |
| :--- | :--- | :--- | :--- | :--- |
| Western | Ernest Hemingway | 0.72 | 12.4 | Low (0.45) |
| Post-Colonial| Chinua Achebe | 0.64 | 18.2 | Medium (1.12) |
| Persian (HC) | Sadegh Hedayat | 0.48 | 15.6 | High (2.85) |
‌
## Key Findings
- Lexical Loop Syndrome: Observed in Persian emulations where TTR dropped significantly (0.48), showing the model's reliance on high-frequency generic terms.
- Syntactic Recasting: Non-Western styles were consistently forced into standard English-centric logical structures.
```
‌
---
