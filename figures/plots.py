import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
df = pd.read_csv("figures/gender_bias_results.csv")

colors = {
    'female': '#A45FE0',
    'male': '#0B3D91',
    'non-binary': '#F5C900',
    'unknown': '#4A4A4A'
}

df.head(10)
df["gender"].value_counts()
df.groupby("profession")["gender"].value_counts()

# Nurse Statistics
n_fem_nurse = df[(df["profession"] == "nurse") & (df["gender"] == "female")].shape[0]
n_male_nurse = df[(df["profession"] == "nurse") & (df["gender"] == "male")].shape[0]
n_nonbinary_nurse = df[(df["profession"] == "nurse") & (df["gender"] == "non-binary")].shape[0]

plt.figure(figsize=(8, 6))
sns.barplot(x=["Female", "Male", "Non-Binary"],
            y=[n_fem_nurse, n_male_nurse, n_nonbinary_nurse],
            palette=['#A45FE0', '#0B3D91', '#F5C900'])
plt.xlabel('Gender')
plt.ylabel('Frequency')
plt.title('Gender Distribution among Nurses')
plt.tight_layout()
plt.savefig('figures/gender_distribution_nurse.png', dpi=150)
plt.show()

# Stacked bar plot
count = df.groupby(['profession', 'gender']).size().unstack(fill_value=0)
probs = count.div(count.sum(axis=1), axis=0)

probs.plot(kind='bar', stacked=True, figsize=(10, 7), color=[colors[col] for col in probs.columns])
plt.ylabel('Proportion')
plt.title('Gender Distribution by Profession')
plt.legend(title='Gender')
plt.tight_layout()
plt.savefig('figures/gender_distribution_by_profession.png', dpi=150)
plt.show()