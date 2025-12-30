import matplotlib.pyplot as plt
import seaborn as sns
from src.prompt import n_fem_nurse, n_male_nurse, n_nonbinary_nurse

# Hist Nurse
plt.figure(figsize=(8, 6))
plt.bar(['Female Nurses'], [mean_nurse], color='skyblue', yerr=[[mean_nurse - ci_lower_nurse], [ci_upper_nurse - mean_nurse]], capsize=10)
plt.ylim(0, 1)
plt.ylabel('Proportion')
plt.title('Proportion of Female Nurses with 95% CI')
plt.grid(axis='y')
plt.savefig('figures/nurse_statistics.png', dpi=150)
plt.show()

# Gender Bar Nurse
plt.figure(figsize=(8, 6))
plt.bar(["Female", "Male", "Non-Binary"],
        ["n_fem_nurse", "n_male_nurse", "non_binary_nurse"],
        fill=True, color=['skyblue', 'lightgreen', 'lightcoral'],
        alpha=0.7)
plt.xlabel('Gender')
plt.ylabel('Frequency')
plt.title('Gender Distribution among Nurses')
plt.legend()
plt.tight_layout()
plt.savefig('figures/gender_distribution_nurse.png', dpi=150)
plt.show()

# Gender Bar Doctor
plt.figure(figsize=(8, 6))
plt.bar(["Female", "Male", "Non-Binary"],
        ["n_fem_doc", "n_male_doc", "non_binary_doc"],
        fill=True, color=['skyblue', 'lightgreen', 'lightcoral'],
        alpha=0.7)
plt.xlabel('Gender')
plt.ylabel('Frequency')
plt.title('Gender Distribution among Doctors')
plt.legend()
plt.tight_layout()
plt.savefig('figures/gender_distribution_doc.png', dpi=150)
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(["n_fem_nurse", "n_male_nurse", "non_binary_nurse",
         "n_fem_doc", "n_male_doc", "non_binary_doc"],
    ["Female Nurse", "Male Nurse", "Non-Binary Nurse",
         "Female Doctor", "Male Doctor", "Non-Binary Doctor"],
        fill=True, color=['skyblue', 'lightgreen', 'lightcoral',
                          'skyblue', 'lightgreen', 'lightcoral'],
        alpha=0.7)
plt.xlabel('Gender and Profession')
plt.ylabel('Frequency')
plt.title('Distribution of Female Proportions in Nurses and Doctors')
plt.legend()
plt.tight_layout()
plt.savefig('figures/nurse_doc_distr.png', dpi=150)
plt.show()


plt.figure(figsize=(8, 6))
plt.bar([mean_doc], ["Female Doctor"], color='lightgreen', yerr=[[mean_doc - ci_lower_doc], [ci_upper_doc - mean_doc]], capsize=10)
plt.ylim(0, 1)
plt.ylabel('Proportion')
plt.title('Proportion of Female Doctors with 95% CI')
plt.grid(axis='y')
plt.savefig('figures/doctor_statistics.png', dpi=150)
plt.show()

