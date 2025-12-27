# Gender Bias in LLMs 

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

## Project Organization

**Course**: Simulations Tools 2025

**Authors:** Taner Yasadur, Alison Moldovan-Mauer

**Date:** 2025-01-09

**Model:** llama-3.2-3b-instruct-q4_k_m.gguf 

## Project Structure
**Hypothesis:** The perceived gender bias in a language model persists even when the inputs vary randomly.

A Monte Carlo simulation is used to test this hypothesis by generating multiple variations of input prompts and analyzing the model's responses.


### To Dos:
    [x] Anzahl Simulationen (z. B. 10 000 generierte Antworten pro Template). ⇒ Parallelisierung im Code?????
    [ ] Kontrollgruppen: Feste (nicht zufällige) Prompts als Referenz
    [x] Signifikanzmaße & Konfidenzintervalle
    [ ] Bias-Score / Odds Ratio: Verhältnis der Wahrscheinlichkeiten (z. B. P(„he“|doctor) / P(„she“|doctor)).
    [ ] Varianz oder Entropie der Bias-Metriken über die Monte-Carlo-Runs — misst, wie beständig der Bias bei Prompt-Rauschen bleibt.
    [ ] Sensitivitätsanalyse: Variiere die Sampling-Strategie, Anzahl der Simulationen, und die Zusammensetzung der Namenlisten; prüfe Robustheit der Ergebnisse.
    [x] Temperature: 0.0 deterministisch
    [ ] Visualisierungen:
        [ ] Balkendiagramm: P(Arzt | male) vs P(Arzt | female) mit Errorbars.
        [ ] Heatmap: Berufe × Gender→Wahrscheinlichkeiten.
        [ ] Token-prob Divergence Kurven (KL oder mean logprob diff).
        [ ] Wordclouds getrennt nach Gender (Adjektive).


This project is organized following the [Cookiecutter Data Science](https://cookiecutter-data-science.drivendata.org/) template. The structure is as follows:

```
├── figures
├── models
├── notebooks
├── reports
├── src
├── env.  
├── README.md         
├── requirements.txt
```

## Installation


1. Setup environment:
```bash
pip install -r requirements.txt
``` 
2. Install LLama
```bash
pip install llama-cpp-python
```
3. Copy and configure .env

```bash
MODELPATH="/path/to/your/model.gguf"
```
4. Run the simulation:
```bash
python src/run_all.sh
```




