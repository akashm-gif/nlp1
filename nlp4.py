from collections import Counter
from nltk.util import ngrams
import nltk
text = """
speech recognition system help users type faster .
speech recognition model predict the next word .
speech recognition and predictive text are important .
"""
tokens = text.lower().split()
ug = Counter(tokens)
bg = Counter(ngrams(tokens, 2))
tg = Counter(ngrams(tokens, 3))
V = len(ug)
k = 1
input_words = ["speech", "recognition"]
context = tuple(input_words)
next_words = set(tokens)
probabilities = {}

for word in next_words:
    trigram = context + (word,)
    trigram_count = tg[trigram]
    bigram_count = bg[context]
    prob = (trigram_count + k) / (bigram_count + k * V)
    probabilities[word] = prob
sorted_predictions = sorted(
    probabilities.items(),
    key=lambda x: x[1],
    reverse=True
)

print("Next word predictions (with Laplace smoothing):\n")
for word, prob in sorted_predictions:
    print(f"{word} : {prob:.4f}")
