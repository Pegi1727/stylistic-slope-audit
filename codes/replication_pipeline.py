import pandas as pd
from scipy import stats

def run_replication():
    print("=" * 60)
    print("REPLICATION PIPELINE: STYLISTIC ASYMMETRY IN LLMs")
    print("=" * 60)
    df = pd.read_csv("../data/stylistic_asymmetry_complete_dataset.csv")
    print(f"[+] Loaded dataset with {len(df)} observations.")
    metrics = ["MATTR","Burrows_Delta","MLS","HLR","Mean_Word_Len","Lexical_Density"]
    print("\n[+] Descriptive Statistics (Table S3):")
    print(df.groupby(["Tradition","Type"])[metrics].agg(["mean","std"]).round(3))
    gpt_df = df[df["Type"] == "GPT-4o"]
    print("\n[+] Kruskal-Wallis on GPT-4o outputs across traditions:")
    for m in metrics:
        groups = [g[m].values for _, g in gpt_df.groupby("Tradition")]
        stat, p = stats.kruskal(*groups)
        print(f"  - {m:<15}: H = {stat:6.3f}, p = {p:.4e}")
    print("\n[+] Inter-Rater Reliability (Krippendorff's Alpha):")
    print(pd.read_csv("../data/krippendorff_alpha.csv").to_string(index=False))

if __name__ == "__main__":
    run_replication()
