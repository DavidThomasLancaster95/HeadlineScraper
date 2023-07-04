from collections import Counter
import re

filename = 'allheadlines.txt'
blacklist_filename = 'blackwords.txt'

# Read the headlines from the text file
with open(filename, 'r', encoding='utf-8') as file:
    headlines = file.read()

# Perform lexical analysis and count word frequencies
words = re.findall(r'\w+', headlines.lower())
word_counts = Counter(words)

# Read the list of blacklisted words
with open(blacklist_filename, 'r', encoding='utf-8') as file:
    blacklisted_words = file.read().splitlines()

# Exclude blacklisted words from the word counts
for word in blacklisted_words:
    word_counts.pop(word, None)

# Print the top 40 most common words
print("Top 100 Most Common Words:")
for word, count in word_counts.most_common(100):
    print(f"{word}: {count}")
