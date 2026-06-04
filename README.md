# ASM - Advanced Statistical Methods (FMDS2526132)

This repository contains **practicals** implemented in **Python** for *Advanced Statistical Methods*. Each practical focuses on a specific statistical topic and demonstrates the required calculations and/or plots.

---

## Repository Contents

| File | Practical | Topic |
|---|---:|---|
| `Practical-1.py` | 01 | Binomial distribution |
| `PRACTICAL2.py` | 02 | Normal distribution |
| `PRACTICAL3.py` | 03 | Plotting binomial distribution |
| `PRACTICAL4.py` | 04 | Plotting normal distribution |
| `PRACTICAL5.py` | 05 | PDF, CDF (discrete/continuous visualization) |
| `PRACTICAL6.py` | 06 | t-test, normal test (example), F-test |
| `PRACTICAL7.py` | 07 | One-way ANOVA |
| `PRACTICAL8.py` | 08 | Non-parametric tests (Sign test) |
| `PRACTICAL9.py` | 09 | Kruskal–Wallis test |
| `PRACTICAL10.py` | 10 | Wilcoxon signed-rank/sign test |
| `PRACTICAL11.py` | 11 | Time series analysis & forecasting |

> Note: The exact code may include console prompts (`input()`) and graphical output (`matplotlib`).

---

## Setup Instructions

### 1) Install Python
Make sure Python is installed.

### 2) Install required packages
Run the following:

```bash
pip install numpy matplotlib pandas scipy
```

---

## How to Run

Open a terminal in the repository folder and run one of the following:

```bash
python Practical-1.py
python PRACTICAL2.py
python PRACTICAL3.py
...
python PRACTICAL11.py
```

Some scripts may ask for inputs (e.g., `N`, `P`, `r`, or `future year`). Others generate plots.

---

## Practical-wise Overview

### Practical 01 — Binomial Distribution
- Computes:
  - Binomial probability using:
    - \(P(r)=nCr\cdot p^r \cdot q^{n-r}\)
  - Mean and standard deviation
- Uses a custom `nCr()` and `BD()` implementation.

### Practical 02 — Normal Distribution
- Creates a range of values.
- Computes probability density (normal curve) using parameters (mean, sd).
- Computes a Z-score / Standard Normal Distribution term.

### Practical 03 — Binomial Distribution Plotting
- Computes probabilities for \(r=0\) to \(n\).
- Visualizes results using:
  - line plot
  - bar plot

### Practical 04 — Normal Distribution Plotting
- Plots the normal curve (probability density).
- Generates random samples from \(\mathcal{N}(mean, sd)\).
- Plots a histogram to show the distribution.

### Practical 05 — PDF, CDF Visualization
- Generates random data.
- Builds a histogram-based probability distribution.
- Computes:
  - PDF approximation
  - CDF (cumulative sum)
- Plots PDF and CDF together.

### Practical 06 — t-test / F-test
- Student t-test style computation:
  - Calculates sample mean
  - Sample standard deviation
  - t statistic and decision vs tabulated value
- F-test computation:
  - Compares sample variances and calculates F
  - Computes degrees of freedom

### Practical 07 — One-way ANOVA
- Computes:
  - Variance between groups (MSC)
  - Variance within groups (MSE)
  - F-statistic = MSC / MSE

### Practical 08 — Non-parametric Sign Test
- Uses a median hypothesis test.
- Subtracts the hypothesized median from each observation.
- Counts positive and negative signs (ignores zeros).
- Computes T = min(T+, T-).

### Practical 09 — Kruskal–Wallis Test
- Uses `scipy.stats.kruskal` over multiple groups.
- Compares p-value with alpha (0.05) and prints decision.

### Practical 10 — Wilcoxon Signed Rank / Sign Test
- Subtracts median from each data point.
- Removes zeros.
- Converts differences to absolute values.
- Ranks them and computes T+ and T-.
- Chooses T = min(T+, T-).

### Practical 11 — Time Series Analysis & Forecasting
- Rolling window sums (window sizes 3 and 5).
- Least squares forecasting:
  - Uses assumed mean A
  - Computes coefficients (a, b)
  - Generates fitted values and predicts future production for a user-entered year.

---



