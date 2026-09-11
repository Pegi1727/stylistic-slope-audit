import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("stylometric_raw_data.xlsx")

plt.figure()
plt.bar(df["Cohort"], df["Burrows_Delta"])
plt.ylabel("Burrows' Delta")
plt.title("Stylometric Distance (Burrows' Delta)")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("real_figure1_burrows_delta.png", dpi=300)
plt.show()
