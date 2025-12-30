import numpy as np
from src.prompt import outputs_doc, outputs_nurse, n_male_nurse, n_fem_doc, n_male_doc, n_nonbinary_nurse, n_nonbinary_doc

## Nurse Statistics
# Calculate mean, standard deviation and 95% confidence interval for the proportion of female nurses
N_nurse = (n_fem_nurse + n_male_nurse + n_nonbinary_nurse) # total number of samples with usefull info
mean_nurse = round((n_fem_nurse / N_nurse), 4)
std_nurse =  round(((mean_nurse * (1 - mean_nurse)) ** 0.5), 4)

z = 1.96
ci_lower_nurse = round((mean_nurse - z * std_nurse / np.sqrt(N_nurse)), 4)
ci_upper_nurse = round((mean_nurse + z * std_nurse / np.sqrt(N_nurse)), 4)

print("Mean Female Nurses:", mean_nurse) # mean
print("Std:", std_nurse) # Standard deviation of the proportion 0.0446
print("95% CI:", (ci_lower_nurse, ci_upper_nurse)) # 95% Confidence Interval: (0.985, 1.011) -> 50% is not in the Range


## Doctor Statistics
# Calculate mean, standard deviation and 95% confidence interval for the proportion of female doctors
N_doc = (n_fem_doc + n_male_doc + n_nonbinary_doc) # total number of samples with usefull info
mean_doc = round((n_fem_doc / N_doc), 4)
std_doc =  round(((mean_doc * (1 - mean_doc)) ** 0.5), 4)

z = 1.96
ci_lower_doc = round((mean_doc - z * std_doc / np.sqrt(N_doc)), 4)
ci_upper_doc = round((mean_doc + z * std_doc / np.sqrt(N_doc)), 4)

print("Mean Female Doctors:", mean_doc) # mean 0.998
print("Std:", std_doc) # Standard deviation of the proportion 0.0446
print("95% CI:", (ci_lower_doc, ci_upper_doc)) # 95% Confidence Interval: (0.985, 1.011) -> 50% is not in the Range