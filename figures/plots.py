import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df_probs = pd.read_csv("figures/gender_props_results.csv")
df = pd.read_csv("figures/gender_bias_results.csv")

# Plot Gender Proportion by Profession
colors = {
    'female': '#A45FE0',
    'male': '#0B3D91',
    'unknown': '#4A4A4A'
}
# Plot stacked bar chart
plt.bar(df_probs['profession'], df_probs['prop_male'], color=colors['male'], label='Male')
plt.bar(df_probs['profession'], df_probs['prop_female'], bottom=df_probs['prop_male'], color=colors['female'], label='Female')
plt.bar(df_probs['profession'], df_probs['prop_unknown'], bottom=df_probs['prop_male'] + df_probs['prop_female'], color=colors['unknown'], label='Unknown')

plt.xlabel('Profession')
plt.ylabel('Proportion')
plt.title('Gender Proportions by Profession')
plt.ylim(0, 1)  # Ensure the y-axis goes from 0 to 1
plt.legend()
plt.show()


"""df_mean = (
    df_probs
    .groupby("profession")["gender"]
    .count()
)
x = np.arange(len(df_mean))
width = 0.35
plt.figure(figsize=(10, 6))
plt.bar(x - width/2, df_mean["prop_female"], width, label="Female")
plt.bar(x + width/2, df_mean["prop_male"], width, label="Male")

plt.xticks(x, df_mean.index, rotation=45, ha="right")
plt.ylim(0, 5)
plt.axhline(0.5, linestyle="--")
plt.title("Female Underrepresentation in Doctor Predictions Compared to Nurses", fontsize = 18)
plt.ylabel("Proportion", fontsize = 14)
plt.xlabel("Profession", fontsize = 14)
plt.legend()
plt.tight_layout()
plt.savefig('figures/', dpi=150)
plt.show()
"""

"""
# Plot Gender and Profession
plt.figure(figsize=(8, 6))
plt.plot(df_probs['run_id'], df_probs['prop_female'], color='#A45FE0')
plt.xlabel("Run")
plt.ylabel("Female proportion")
plt.title("Convergence of Female Pronoun Probability")
plt.tight_layout()
plt.savefig("figures/", dpi=150)
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
plt.savefig("figures/", dpi=150)
plt.show()

"""