import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset("penguins").dropna()

print(penguins.head)

sns.scatterplot(
    data=penguins,
    x="flipper_length_mm",
    y="body_mass_g"
)

plt.show()

