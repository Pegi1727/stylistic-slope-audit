import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("stylometric_raw_data.xlsx")

plt.figure()
plt.plot(df["Cohort"], df["Human_Hapax"], marker='o', label="Human")
plt.plot(df["Cohort"], df["GPT4o_Hapax"], marker='o', label="GPT-4o")
plt.ylabel("Hapax Legomena (%)")
plt.title("Rare Word Usage (Hapax Legomena)")
plt.legend()
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("real_figure4_hapax.png", dpi=300)
plt.show()
