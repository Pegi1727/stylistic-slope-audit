# ==============================================================================
# Project: Measuring Stylistic Asymmetry in Large Language Models
# Script: 01_stylometric_analysis.R
# Purpose: Descriptive statistics, Kruskal-Wallis tests, and effect sizes.
# ==============================================================================
suppressPackageStartupMessages({library(tidyverse); library(knitr)})

df <- read.csv("../data/stylistic_asymmetry_complete_dataset.csv", stringsAsFactors=FALSE)
df$Tradition <- factor(df$Tradition, levels=c("Western","Postcolonial","Persian"))
df$Type <- factor(df$Type, levels=c("Human","GPT-4o"))
cat(">>> Dataset loaded. N =", nrow(df), "\n")

desc_stats <- df %>% group_by(Tradition, Type) %>% summarise(
  N=n(),
  MATTR_Mean=mean(MATTR), MATTR_SD=sd(MATTR),
  Burrows_Delta_Mean=mean(Burrows_Delta), Burrows_Delta_SD=sd(Burrows_Delta),
  MLS_Mean=mean(MLS), MLS_SD=sd(MLS),
  HLR_Mean=mean(HLR), HLR_SD=sd(HLR),
  LD_Mean=mean(Lexical_Density), LD_SD=sd(Lexical_Density),
  MWL_Mean=mean(Mean_Word_Len), MWL_SD=sd(Mean_Word_Len),
  .groups="drop")
write.csv(desc_stats, "../results/table_s3_descriptive_statistics.csv", row.names=FALSE)
cat(">>> Table S3 exported.\n")

gpt_df <- df %>% filter(Type=="GPT-4o")
for (m in c("Burrows_Delta","MLS","HLR","MATTR","Lexical_Density","Mean_Word_Len")) {
  cat("\n--- Kruskal-Wallis:", m, "---\n")
  print(kruskal.test(as.formula(paste(m,"~ Tradition")), data=gpt_df))
}
