from scipy.stats import chi2_contingency

table = np.array([
    [len(model1_results)-sum(model1_results), sum(model1_results)],
    [len(model2_results)-sum(model2_results), sum(model2_results)]
])

chi2, p, dof, expected = chi2_contingency(table)
print("Chi2:", chi2, "p-value:", p)