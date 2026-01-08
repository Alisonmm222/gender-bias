import pandas as pd
from scipy.stats import chi2_contingency, fisher_exact

df = pd.read_csv("figures/gender_bias_results.csv", sep = ",", comment = "#")
summary = pd.read_csv("figures/summary.csv", sep = ",", comment = "#")

df["is_female"] = df["gender"].apply(lambda x: 1 if x == "female" else 0) # Create a binary column for female
table = pd.crosstab(df["profession"], df["gender"])
print(table)

# Bias
prop_doc = round((table.loc["doctor", "female"] / 10000), 2) * 100
prop_nurse = round((table.loc["nurse", "female"] / 10000), 2) * 100

b = 50.0 # baseline at 50%
bias_doc = round((prop_doc - b), 2)
bias_nurse = round((prop_nurse - b), 2)

latex_bias = pd.DataFrame({
    "Professions":  ["Nurse", "Doctor"],
    "Gender Bias": [bias_nurse, bias_doc],
    "Probabilities": [prop_nurse, prop_doc],
})

# Generate LaTeX code
latex_table_bias = latex_bias.to_latex(
    index=False,
    caption="Gender Bias",
    label="tab:gender_stats_bias",
    float_format="%.2f"
)

# Odds Ratio Calculation
# Odds of being female
odds_doctor = table.loc["doctor", "female"] / table.loc["doctor", "male"]
odds_nurse = table.loc["nurse", "female"] / table.loc["nurse", "male"]

# Odds Ratio
odds_ratio = odds_nurse / odds_doctor
# OR = 1 means no association
# OR > 1 nurses more likely to get female pronouns that doctors
# OR < 1 doctors more likely to get female pronouns

# Chi-square test for independence
chi2, p, dof, ex = chi2_contingency(table)

# Fisher Exact Test
table_2x2 = [[table.loc["nurse", "female"], table.loc["nurse", "male"]],
             [table.loc["doctor", "female"], table.loc["doctor", "male"]]]

p_fisher = fisher_exact(table_2x2) # odds ration and fisher odds ratio the same

# Create DataFrame for LaTeX table
latex_odds = pd.DataFrame({
    "Profession": ["Nurse", "Doctor"],
    "Female": [table.loc["nurse", "female"], table.loc["doctor", "female"]],
    "Male": [table.loc["nurse", "male"], table.loc["doctor", "male"]],
    "Odds of Female": [odds_nurse, odds_doctor],
    "Chi-Square and p": [chi2, p],
    "Odds Ratio": [odds_ratio, odds_ratio],
})

# Generate LaTeX code
latex_table_odds = latex_odds.to_latex(
    index=False,
    caption="Gender distribution and statistical tests",
    label="tab:gender_stats",
    float_format="%.2f"
)