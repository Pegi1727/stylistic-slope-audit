import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("stylometric_raw_data.xlsx")

mattr_gap = df["Human_MATTR"] - df["GPT4o_MATTR"]
mls_gap = df["Human_MLS"] - df["GPT4o_MLS"]
hapax_gap = df["Human_Hapax"] - df["GPT4o_Hapax"]

plt.figure()
plt.plot(df["Cohort"], mattr_gap, marker='o', label="MATTR Gap")
plt.plot(df["Cohort"], mls_gap, marker='o', label="MLS Gap")
plt.plot(df["Cohort"], hapax_gap, marker='o', label="Hapax Gap")
plt.ylabel("Human–Model Gap")
plt.title("Integrated Stylometric Gap")
plt.legend()
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("real_figure5_distance_gap.png", dpi=300)
plt.show()
