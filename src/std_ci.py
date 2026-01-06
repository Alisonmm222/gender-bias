import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("figures/gender_bias_results.csv")

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
    summary["female_prop"] * (1 - summary["female_prop"]) / 10000
)

summary["ci_lower_female"] = summary["female_prop"] - z * summary["se_f"]
summary["ci_upper_female"] = summary["female_prop"] + z * summary["se_f"]

# 95% CI for male proportion
summary["se_m"] = np.sqrt(
    summary["male_prop"] * (1 - summary["male_prop"]) / 10000
)

summary["ci_lower_male"] = summary["male_prop"] - z * summary["se_m"]
summary["ci_upper_male"] = summary["male_prop"] + z * summary["se_m"]

# Plot
x = np.arange(len(summary["profession"]))
width = 0.35
fig, ax = plt.subplots(figsize=(10,6))

# Female bars
ax.bar(x + width/2, summary["female_prop"], width,
       yerr=[summary["female_prop"] - summary["ci_lower_female"],
             summary["ci_upper_female"] - summary["female_prop"]],
       capsize=5, label="Female", color='#bd86ee')

# Male bars
ax.bar(x - width/2, summary["male_prop"], width,
       yerr=[summary["male_prop"] - summary["ci_lower_male"],
             summary["ci_upper_male"] - summary["male_prop"]],
       capsize=5, label="Male", color='#2a5db2')

# Horizontal benchmark line at 0.5
ax.axhline(0.5, color='gray', linestyle='--', linewidth=1)
ax.text(len(summary["profession"])-0.5, 0.51, '50% benchmark', color='gray', ha='right')

ax.set_xticks(x)
ax.set_xticklabels(summary["profession"])
ax.set_ylim(0,0.7)
ax.set_ylabel("Proportion", fontsize = 14)
ax.set_title("Proportion of Gender by Profession with 95% CI Sample", fontsize = 18)
ax.legend()
plt.savefig('figures/proportion_by_profession_sample_true.png', dpi=150)
plt.show()