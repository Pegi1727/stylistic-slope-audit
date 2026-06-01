python
import nltk
from nltk.tokenize import word_tokenize
from collections import Counter
‌
# Ensure you have the necessary NLTK data
# nltk.download('punkt')
‌
def calculate_ttr(text):
"""Calculates Type-Token Ratio (Lexical Richness)"""
tokens = word_tokenize(text.lower())
types = set(tokens)
return len(types) / len(tokens) if len(tokens) > 0 else 0
‌
def calculate_hapax_ratio(text):
"""Calculates the ratio of words that appear only once"""
tokens = word_tokenize(text.lower())
counts = Counter(tokens)
hapaxes = [token for token, count in counts.items() if count == 1]
return len(hapaxes) / len(tokens) if len(tokens) > 0 else 0
‌
def calculate_mls(text):
"""Calculates Mean Length of Sentence (Syntactic Complexity)"""
sentences = nltk.sent_tokenize(text)
word_counts = [len(word_tokenize(s)) for s in sentences]
return sum(word_counts) / len(sentences) if len(sentences) > 0 else 0
‌
# Example usage for researchers:
# print(f"TTR: {calculate_ttr(sample_text)}")
