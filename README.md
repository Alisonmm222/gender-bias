# Gender Bias in LLMs 

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

## Project Organization

**Course**: Simulations Tools 2025

**Authors:** Taner Yasadur, Alison Moldovan-Mauer

**Date:** 2025-01-09

**Model:** llama-3.2-3b-instruct-q4_k_m.gguf
```bash
pip install llama-cpp-python
```   

## Project Structure
**Hypothesis:** The perceived gender bias in a language model persists even when the inputs vary randomly.

A Monte Carlo simulation is used to test this hypothesis by generating multiple variations of input prompts and analyzing the model's responses.


### To Dos:
    [ ] Anzahl Simulationen (z. B. 10 000 generierte Antworten pro Template). ⇒ Parallelisierung im Code?????
    [ ] Kontrollgruppen: Feste (nicht zufällige) Prompts als Referenz.
    [ ] Bootstrapped CI für jede Kennzahl (z. B. 95% CI).
    [ ] Conditional Probability: Anteil der Antworten, die z. B. „he“ verwenden, gegeben ein Prompt mit Berufsrolle
    [ ] Signifikanzmaße & Konfidenzintervalle
    [ ] Bias-Score / Odds Ratio: Verhältnis der Wahrscheinlichkeiten (z. B. P(„he“|doctor) / P(„she“|doctor)).
    [ ] Varianz oder Entropie der Bias-Metriken über die Monte-Carlo-Runs — misst, wie beständig der Bias bei Prompt-Rauschen bleibt.
    [ ] Sensitivitätsanalyse: Variiere die Sampling-Strategie, Anzahl der Simulationen, und die Zusammensetzung der Namenlisten; prüfe Robustheit der Ergebnisse.
    [ ] Temperature / Sampling testen: z.B. 0.0 deterministisch, 0.7, 1.0). Für Monte-Carlo: viele Samples bei nicht-deterministischen Settings.
    [ ] Visualisierungen:
        [ ] Balkendiagramm: P(Arzt | male) vs P(Arzt | female) mit Errorbars.
        [ ] Heatmap: Berufe × Gender→Wahrscheinlichkeiten.
        [ ] Token-prob Divergence Kurven (KL oder mean logprob diff).
        [ ] Wordclouds getrennt nach Gender (Adjektive).


This project is organized following the [Cookiecutter Data Science](https://cookiecutter-data-science.drivendata.org/) template. The structure is as follows:

```
├── configs
├── data
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.                                  
│   └── raw          <- The original, immutable data dump.
├── figures
├── notebooks
├── reports
├── src
├── README.md          <- The top-level README for developers using this project.
├── envoronment.yml    <- The conda environment file for reproducing the analysis environment.
```

## Installation

1. Clone the repository:
```bash git clone https://github.com/Alisonmm222/gender-bias
cd gender-bias
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install the package and dependencies:
```bash
pip install -r requirements.txt
pip install -e .
```
4. (Optional) Copy and configure environment variables:
```bash
cp .env.example .env
```




