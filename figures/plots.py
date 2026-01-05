import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df_probs = pd.read_csv("figures/gender_props_results.csv")
df = pd.read_csv("figures/gender_bias_results.csv")

# Plot Gender and Profession
plt.figure(figsize=(8, 6))
plt.plot(df_probs['run_id'], df_probs['prop_female'], color='#A45FE0')
plt.xlabel("Run")
plt.ylabel("Female proportion")
plt.title("Convergence of Female Pronoun Probability")
plt.tight_layout()
plt.savefig("figures/convergence_gender_profession.png", dpi=150)
plt.show()

# Bar Plot
colors = {
    "female": "#A45FE0",
    "male": "#0B3D91",
    "unknown": "#4A4A4A"
}
counts = (
    df
    .groupby(["profession", "gender"])
    .size()
    .unstack(fill_value=0)
)

props = counts.div(counts.sum(axis=1), axis=0)

x = np.arange(len(counts))
width = 0.25

plt.figure(figsize=(9, 6))

for i, gender in enumerate(props.columns):
    plt.bar(
        x + (i - len(props.columns)/2) * width,
        props[gender],
        width,
        label=gender.capitalize(),
        color=colors.get(gender)
    )

plt.xlabel("Profession")
plt.ylabel("Count")
plt.title("Gender by Profession")
plt.xticks(x, counts.index, rotation=45, ha="right")
plt.axhline(0.5, linestyle="--", linewidth=1)
plt.legend()
plt.tight_layout()
plt.savefig("figures/barplots_gender_profession.png", dpi=150)
plt.show()