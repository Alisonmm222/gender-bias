import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df_probs = pd.read_csv("figures/gender_probs_results.csv")
df = pd.read_csv("figures/gender_bias_results.csv")

colors = {
    'female': '#A45FE0',
    'male': '#0B3D91',
    'unknown': '#4A4A4A'
}

# Plot Gender and Profession

plt.figure(figsize=(8, 6))
plt.plot(df_probs['run_id'], df_probs['prop_female'], color='#A45FE0')
plt.xlabel("Run")
plt.ylabel("Female proportion")
plt.title("Convergence of Female Pronoun Probability")
plt.tight_layout()
plt.savefig("figures/hist_gender_profession.png", dpi=150)
plt.show()


# Bar Plot Gender and Profession

plt.figure(figsize=(8, 6))
plt.plot(df["gender"], df["profession"], color = colors)
plt.xlabel("Gender")
plt.ylabel("Profession")
plt.title("Profession of Female Pronoun")
plt.tight_layout()
plt.safefig("/figures/bar_gender_profession.png", dip = 150)
plt.show()


# Plot with Labels

fig, ax = plt.subplots(figsize=(8, 6))
ax = sns.barplot(
    data=df_probs,
    x="profession",
    y="proportion",
    hue="gender",
    palette={
        "female": "#A45FE0",
        "male": "#0B3D91",
        "unknown": "#4A4A4A"
    }
)
ax.set_ylim(0, 1)
ax.set_ylabel("Proportion")
ax.set_xlabel("Profession")
ax.set_title("Gender Distribution by Profession")

for bar in ax.patches:
    height = bar.get_height()
    if height <= 0:
        continue
    ax.annotate(
        f"{height*100:.1f}%",
        (bar.get_x() + bar.get_width() / 2, height),
        ha="center",
        va = "center" if height > 0.1 else "bottom",
        y = bar.get_y() + height / 2 if height > 0.1 else height,
        fontsize=9,
        xytext=(0, 3),
        textcoords="offset points")
plt.tight_layout()
plt.savefig("figures/bar_gender_profession_props.png", dpi=150)
plt.show()