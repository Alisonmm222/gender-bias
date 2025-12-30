import matplotlib as plt
# Hist Nurse

def plot_nurse_statistics(mean_nurse, ci_lower_nurse, ci_upper_nurse):
    plt.figure(figsize=(8, 6))
    plt.bar(['Female Nurses'], [mean_nurse], color='skyblue', yerr=[[mean_nurse - ci_lower_nurse], [ci_upper_nurse - mean_nurse]], capsize=10)
    plt.ylim(0, 1)
    plt.ylabel('Proportion')
    plt.title('Proportion of Female Nurses with 95% CI')
    plt.grid(axis='y')
    plt.savefig('figures/nurse_statistics.png', dpi=150)
    plt.close()
plot_nurse_statistics(mean_nurse, ci_lower_nurse, ci_upper_nurse)

def plot_female_proportions_distribution(mean_nurse, mean_doc):
    plt.figure(figsize=(8, 6))
    plt.hist([mean_nurse, mean_doc], bins=10, color=['skyblue', 'lightgreen'], label=['Nurses', 'Doctors'])
    plt.xlabel('Proportion of Females')
    plt.ylabel('Frequency')
    plt.title('Distribution of Female Proportions in Nurses and Doctors')
    plt.legend()
    plt.grid(axis='y')
    plt.savefig('figures/female_proportions_distribution.png', dpi=150)
    plt.close()
def plot_doctor_statistics(mean_doc, ci_lower_doc, ci_upper_doc):
    plt.figure(figsize=(8, 6))
    plt.bar(['Female Doctors'], [mean_doc], color='lightgreen', yerr=[[mean_doc - ci_lower_doc], [ci_upper_doc - mean_doc]], capsize=10)
    plt.ylim(0, 1)
    plt.ylabel('Proportion')
    plt.title('Proportion of Female Doctors with 95% CI')
    plt.grid(axis='y')
    plt.savefig('figures/doctor_statistics.png', dpi=150)
    plt.close()
plot_doctor_statistics(mean_doc, ci_lower_doc, ci_upper_doc)
