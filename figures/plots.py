import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys
import os

sys.path.append(os.path.abspath("./src"))
from create_metadata import get_metadata

summary = pd.read_csv("figures/summary.csv", sep = ",",  comment = "#")
df = pd.read_csv("figures/gender_bias_results.csv",  sep = ",", comment = "#")

metadata = get_metadata()
metadata_str = {k: str(v) for k,v in metadata.items()}

## Plot Proportion with CI py Profession
x = np.arange(len(summary["profession"]))
fig, ax = plt.subplots(figsize=(10, 6))
width = 0.35

# Female bars
ax.bar(x + width / 2, summary["female_prop"], width,
       yerr=[summary["female_prop"] - summary["ci_lower_female"],
             summary["ci_upper_female"] - summary["female_prop"]],
       capsize=5, label="Female", color='#bd86ee')

# Male bars
ax.bar(x - width / 2, summary["male_prop"], width,
       yerr=[summary["male_prop"] - summary["ci_lower_male"],
             summary["ci_upper_male"] - summary["male_prop"]],
       capsize=5, label="Male", color='#2a5db2')

# Horizontal benchmark line at 0.5
ax.axhline(0.5, color='gray', linestyle='--', linewidth=1)
ax.text(len(summary["profession"]) - 0.5, 0.51, '50% benchmark', color='gray', ha='right')
ax.set_xticks(x)
ax.set_xticklabels(summary["profession"], fontsize=14)
ax.set_ylim(0, 0.7) # shorter because benchmark is at 0.5
ax.set_ylabel("Proportion", fontsize=12)
ax.set_title("Proportion of Gender by Profession with 95% CI", fontsize=18)
ax.legend()
plt.figtext(
    0.01, 0.01,
    f"Seed={metadata_str['seed']} | {metadata_str['date']} | commit={metadata_str['git_commit']}",
    fontsize=7, ha='left', va='bottom', alpha=0.6)
plt.savefig('figures/proportion_by_profession_ci.png',
            metadata={"Seed": metadata_str['seed'], "Date": metadata_str['date'],
                      "GitCommit": metadata_str['git_commit']}, dpi=300)
plt.show()

## Stacked Bar Plot Gender Proportion by Profession

plt.figure(figsize=(10, 6))
plt.bar(summary['profession'], summary['male_prop'], color='#2a5db2', label='Male', width=0.5)
plt.bar(summary['profession'], summary['female_prop'], bottom=summary['male_prop'], color='#bd86ee',
        label='Female', width=0.5)
plt.bar(summary['profession'], summary['unknown_n'], bottom=summary['male_prop']
        + summary['female_prop'], color='#7c7c7c', label='Unknown', width=0.5)

# order legend
handles, labels = plt.gca().get_legend_handles_labels()
order = ["Unknown", "Female", "Male"]
ordered_handles = [handles[labels.index(lbl)] for lbl in order]

# percentages on bars
ax = plt.gca()
for i, profession in enumerate(summary['profession']):
    y_male = summary.loc[i, 'male_prop']
    y_female = summary.loc[i, 'female_prop']
    y_unknown = summary.loc[i, 'unknown_prop']

    # Male label
    if y_male > 0:
        ax.text(
            i,
            y_male / 2,
            f"{y_male:.0%}",
            ha='center',
            va='center',
            color='#151414',
            fontsize=12
        )

    # Female label
    if y_female > 0:
        ax.text(
            i,
            y_male + y_female / 2,
            f"{y_female:.0%}",
            ha='center',
            va='center',
            color='#151414',
            fontsize=12
        )

    # Unknown label
    if y_unknown > 0:
        ax.text(
            i,
            y_male + y_female + y_unknown / 2,
            f"{y_unknown:.0%}",
            ha='center',
            va='center',
            color='#151414',
            fontsize=14
        )
plt.xticks(fontsize=14)
plt.title('Gender Proportions by Profession', fontsize=18)
plt.ylim(0, 1)
ax.yaxis.set_major_formatter(lambda y, _: f"{int(y*100)}%")
plt.legend(ordered_handles, order)
plt.savefig('figures/proportion_by_profession_bar.png',
                metadata={"Seed": metadata_str['seed'], "Date": metadata_str['date'],
                          "GitCommit": metadata_str['git_commit']}, dpi=300)
plt.figtext(
    0.01, 0.01,
    f"Seed={metadata_str['seed']} | {metadata_str['date']} | commit={metadata_str['git_commit']}",
    fontsize=7, ha='left', va='bottom', alpha=0.6)
plt.show()