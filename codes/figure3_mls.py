import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("stylometric_raw_data.xlsx")

plt.figure()
plt.plot(df["Cohort"], df["Human_MLS"], marker='o', label="Human")
plt.plot(df["Cohort"], df["GPT4o_MLS"], marker='o', label="GPT-4o")
plt.ylabel("Mean Length of Sentence")
plt.title("Sentence Length Comparison (MLS)")
plt.legend()
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("real_figure3_mls.png", dpi=300)
plt.show()
