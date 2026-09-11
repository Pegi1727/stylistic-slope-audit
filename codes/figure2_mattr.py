import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("stylometric_raw_data.xlsx")

plt.figure()
plt.plot(df["Cohort"], df["Human_MATTR"], marker='o', label="Human")
plt.plot(df["Cohort"], df["GPT4o_MATTR"], marker='o', label="GPT-4o")
plt.ylabel("MATTR")
plt.title("Lexical Diversity (MATTR)")
plt.legend()
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("real_figure2_mattr.png", dpi=300)
plt.show()
