import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency, fisher_exact

df = pd.read_csv("figures/gender_bias_results.csv")

df["is_female"] = df["gender"].apply(lambda x: 1 if x == "female" else 0) # Create a binary column for female
table = pd.crosstab(df["profession"], df["gender"])

# Odds Ratio Calculation
# Odds of being female
odds_doctor = table.loc["doctor", "female"] / table.loc["doctor", "male"]
odds_nurse = table.loc["nurse", "female"] / table.loc["nurse", "male"]

# Odds Ratio
# OR = 1 means no association
# OR > 1 nurses more likely to get female pronouns that doctors
# OR < 1 doctors more likely to get female pronouns
odds_ratio = odds_nurse / odds_doctor
print("Odds Ratio (Nurse vs Doctor):", odds_ratio)

# Chi-square test for independence
chi2, p, dof, ex = chi2_contingency(table)
print("Chi-square Statistic:", chi2)
print("p-value:", p)

# Fisher Exact Test

table_2x2 = [[table.loc["nurse", "female"], table.loc["nurse", "male"]],
             [table.loc["doctor", "female"], table.loc["doctor", "male"]]]
oddsratio, p_value = fisher_exact(table_2x2)
print("Fishers exact test p-value:", p_value, "Odds Ratio by Fisher:", oddsratio)


