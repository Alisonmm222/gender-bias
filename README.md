# Gender Bias in Llama 3.2

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

## Project Organization

**Course**: Simulations Tools 2025/2026

**Authors:** Alison Moldovan-Mauer, Taner Yasadur

**Date:** January 2026

**Model:** llama-3.2-3b-instruct-q4_k_m.gguf 

## Project Structure
**Hypothesis:**  Female and male pronouns have the same probability of appearing in the output across professions.

A Monte Carlo simulation is used to let the model choose a possessive determiner for two different prompts and professions (nurse and doctor). 

This project is organized following the [Cookiecutter Data Science](https://cookiecutter-data-science.drivendata.org/) template. The structure is as follows:

```
├── figures (simulation results and plots will be stored here) 
├── models (safe model here and add path to your .env)
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
3. Configure .env

```bash
MODELPATH="/path/to/your/model.gguf"
```
4. Run results:
```bash
python notebooks/results.ipynb
```