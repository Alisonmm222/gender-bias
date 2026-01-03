import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import time
df = pd.read_csv("figures/gender_bias_results.csv")

colors = {
    'female': '#A45FE0',
    'male': '#0B3D91',
    'non-binary': '#F5C900',
    'unknown': '#4A4A4A'
}


df["gender"].value_counts().show()
df.groupby("profession")["gender"].value_counts()



# dynamic plot
plt.ion()

fig, ax = plt.subplots()
labels = ['Female', 'Male', 'Non-Binary', 'Unknown']
counts = [0, 0, 0]

bars = ax.bar(labels, counts, color=['#A45FE0', '#0B3D91', '#F5C900'])
ax.set_ylim(0, 1000)
ax.set_ylabel("Count")

for i in range(1000):
    # simulate updates
    counts[i % 3] += 1

    # update bars
    for bar, c in zip(bars, counts):
        bar.set_height(c)

    ax.set_title(f"Simulation step {i+1}")
    plt.pause(0.01)

plt.ioff()
plt.title(f"Simulation step {i+1}")
plt.show()
