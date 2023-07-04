from collections import Counter
import re

filename = 'allheadlines.txt'

# Read the headlines from the text file
with open(filename, 'r', encoding='utf-8') as file:
    headlines = file.read()

# Perform lexical analysis and count word frequencies
words = re.findall(r'\w+', headlines.lower())
word_counts = Counter(words)

# Print the top 40 most common words
print("Top 40 Most Common Words:")
for word, count in word_counts.most_common(40):
    print(f"{word}: {count}")
