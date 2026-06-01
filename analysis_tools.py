python
import math
import re
from collections import Counter
‌
class StylometricAudit:
"""
Tools for investigating Algorithmic Homogenization in LLMs.
Includes TTR, MLS, and Burrows' Delta configurations.
"""
‌
def __init__(self, text):
self.text = text
self.tokens = self._tokenize()
‌
def _tokenize(self):
# Cleaning and tokenizing text
clean_text = re.sub(r'[^\w\s]', '', self.text.lower())
return clean_text.split()
‌
def calculate_ttr(self):
"""Calculates Type-Token Ratio (Lexical Diversity)"""
if not self.tokens:
return 0
types = set(self.tokens)
return len(types) / len(self.tokens)
‌
def calculate_mls(self):
"""Calculates Mean Length of Sentence"""
sentences = re.split(r'[.!?]+', self.text)
sentences = [s.strip() for s in sentences if len(s.strip()) > 0]
if not sentences:
return 0
total_words = len(self.tokens)
return total_words / len(sentences)
‌
@staticmethod
def burrows_delta(target_freqs, ref_freqs):
"""
Calculates Burrows' Delta distance between target and reference frequencies.
Used to detect 'Stylistic Slope' towards LLM homogenization.
"""
delta = 0
for word in target_freqs:
if word in ref_freqs:
# Standardized distance calculation
delta += abs(target_freqs[word] - ref_freqs[word])
return delta / len(target_freqs)
‌
# Example usage for verification:
if __name__ == "__main__":
sample_text = "Your sample text from Western or Non-Western literary traditions goes here."
audit = StylometricAudit(sample_text)
print(f"TTR: {audit.calculate_ttr():.4f}")
print(f"MLS: {audit.calculate_mls():.2f}")
