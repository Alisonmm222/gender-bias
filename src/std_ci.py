import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("figures/gender_bias_results.csv")

df["is_female"] = df["gender"].apply(lambda x: 1 if x == "female" else 0) # Create a binary column for female

# Group by profession and calculate statistics
grouped = df.groupby("profession")["is_female"]
summary = grouped.agg(["sum", "count", "mean", "std"])
print(summary)

# Calculate 95% confidence intervals
summary['ci_lower'] = summary['mean'] - 1.96 * (summary['std'] / np.sqrt(summary['count']))
summary['ci_upper'] = summary['mean'] + 1.96 * (summary['std'] / np.sqrt(summary['count']))
print(summary)

summary = summary.reset_index()

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(summary["profession"], summary["mean"], yerr=[summary["mean"] - summary["ci_lower"], summary["ci_upper"] - summary["mean"]], capsize=10,
        color=['lightcoral' if prof == 'nurse' else 'lightgreen' for prof in summary["profession"]])
plt.ylim(0, 1)
plt.ylabel('Proportion of Females')
plt.title('Proportion of Females in Each Profession with 95% CI')
plt.grid(axis='y')
plt.savefig('figures/proportion_females_by_profession.png', dpi=150)
plt.show()
