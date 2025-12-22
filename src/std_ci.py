import numpy as np
from src.prompt import n_fem_nurse, n_male_nurse, outputs

# Calculate mean, standard deviation and 95% confidence interval
mean = n_fem_nurse / (n_fem_nurse + n_male_nurse)
std =  (mean * (1 - mean)) ** 0.5

N = (n_fem_nurse + n_male_nurse) # total number of samples with usefull info
z = 1.96

ci_lower = mean - z * std / np.sqrt(N)
ci_upper = mean + z * std / np.sqrt(N)

print("Mean:", mean) # mean 0.998
print("Std:", std) # Standard deviation of the proportion 0.0446
print("95% CI:", (ci_lower, ci_upper)) # 95% Confidence Interval: (0.985, 1.011) -> 50% is not in the Range