# ==============================================================================
# Script: 02_publication_figures.R  |  ggplot2 publication figures
# ==============================================================================
suppressPackageStartupMessages({library(tidyverse); library(patchwork)})

df <- read.csv("../data/stylistic_asymmetry_complete_dataset.csv")
df$Tradition <- factor(df$Tradition, levels=c("Western","Postcolonial","Persian"))
df$Type <- factor(df$Type, levels=c("Human","GPT-4o"))

theme_pub <- function() theme_classic(base_size=12) + theme(
  plot.title=element_text(face="bold",size=13),
  axis.title=element_text(face="bold",size=11),
  legend.position="top")

p1 <- ggplot(df %>% filter(Type=="GPT-4o"), aes(x=Tradition, y=Burrows_Delta, fill=Tradition)) +
  geom_boxplot(width=0.4, alpha=0.7, outlier.shape=21, show.legend=FALSE) +
  geom_jitter(width=0.1, size=2.5, alpha=0.8, shape=21, fill="white", color="black", show.legend=FALSE) +
  scale_fill_manual(values=c("#64748B","#F59E0B","#EF4444")) +
  labs(title="A. Distributional Distance (Burrows' Delta)", y="Delta Score", x="Tradition") + theme_pub()

p2 <- ggplot(df, aes(x=Tradition, y=MLS, fill=Type)) +
  geom_bar(stat="summary", fun="mean", position=position_dodge(0.7), width=0.6, color="black") +
  geom_errorbar(stat="summary", fun.data="mean_se", position=position_dodge(0.7), width=0.2) +
  scale_fill_manual(values=c("Human"="#1F2937","GPT-4o"="#2563EB")) +
  labs(title="B. Mean Length of Sentence (MLS)", y="Words / Sentence", x="Tradition", fill="Type") + theme_pub()

ggsave("../results/figure_stylometric_asymmetry.png", p1+p2, width=11, height=5, dpi=300)
cat(">>> Figure exported to /results directory.\n")
