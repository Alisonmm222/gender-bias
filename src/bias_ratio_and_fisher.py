import pandas as pd
from scipy.stats import chi2_contingency, fisher_exact

df = pd.read_csv("figures/gender_bias_results.csv", sep = ",", comment = "#")

df["is_female"] = df["gender"].apply(lambda x: 1 if x == "female" else 0) # Create a binary column for female
table = pd.crosstab(df["profession"], df["gender"])

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
latex_df = pd.DataFrame({
    "Profession": ["Nurse", "Doctor"],
    "Female": [table.loc["nurse", "female"], table.loc["doctor", "female"]],
    "Male": [table.loc["nurse", "male"], table.loc["doctor", "male"]],
    "Odds of Female": [odds_nurse, odds_doctor],
    "Chi-Square": [chi2, chi2],
    "Odds Ratio": [odds_ratio, odds_ratio]
})

# Generate LaTeX code
latex_table_odds = latex_df.to_latex(
    index=False,
    caption="Gender distribution and statistical tests",
    label="tab:gender_stats",
    float_format="%.2f"
)