import numpy as np
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath("./src"))
from create_metadata import get_metadata
metadata = get_metadata()

df = pd.read_csv("figures/gender_bias_results.csv", comment="#", sep = ",")

# Binary Column for male and female
df["is_female"] = (df["gender"] == "female").astype(int)
df["is_male"]   = (df["gender"] == "male").astype(int)

summary = (
    df
    .groupby("profession")
    .agg(
        female_n=("is_female", "sum"),
        male_n=("is_male", "sum"),
        female_prop=("is_female", "mean"),
        male_prop = ("is_male", "mean"),
    )
    .reset_index()
)

# 95% CI for female proportion
z = 1.96
summary["se_f"] = np.sqrt(
    summary["female_prop"] * (1 - summary["female_prop"]) / 10000)

summary["ci_lower_female"] = summary["female_prop"] - z * summary["se_f"]
summary["ci_upper_female"] = summary["female_prop"] + z * summary["se_f"]

# 95% CI for male proportion
summary["se_m"] = np.sqrt(
    summary["male_prop"] * (1 - summary["male_prop"]) / 10000)

summary["ci_lower_male"] = summary["male_prop"] - z * summary["se_m"]
summary["ci_upper_male"] = summary["male_prop"] + z * summary["se_m"]

# calculate unknown
summary["unknown_prop"] = 1 - (summary["female_prop"] + summary["male_prop"])
summary["unknown_n"] = 10000 - (summary["female_n"] + summary["male_n"])

# Save summary to a new file
summary.to_csv("./figures/summary.csv", index=False)

# Write metadata and DataFrame to CSV
summary_file = "./figures/summary.csv"

with open(summary_file, "w", encoding="utf-8") as f:
    for key, value in metadata.items():
        f.write(f"# {key}: {value}\n")
    f.write("# ----------------------------\n")
    summary.to_csv(f, index=False)

# Create Latex Table
summary['Female (%)'] = (summary['female_prop'] * 100).round(1).astype(str)
summary['CI Female'] = (
        '['
        + (summary['ci_lower_female'] * 100).round(1).astype(str)
        + ', '
        + (summary['ci_upper_female'] * 100).round(1).astype(str)
        + ']')

summary['Male (%)'] = (summary['male_prop'] * 100).round(1).astype(str)
summary['CI Male'] = (
        '['
        + (summary['ci_lower_male'] * 100).round(1).astype(str)
        + ', '
        + (summary['ci_upper_male'] * 100).round(1).astype(str)
        + ']')

latex_std_ci = summary[['profession', 'Female (%)', 'CI Female', 'Male (%)', 'CI Male']]

latex_table = latex_std_ci.to_latex(
    index=False,
    caption="Female pronoun proportions with 95\\% confidence intervals",
    label="tab:gender_bias",
    column_format="lcc")