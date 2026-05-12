from collections import Counter
import string


text = "Hello world! Hello AI. AI is powerful, and AI is the future."

# clean text
text = text.lower()
for char in string.punctuation:
    text = text.replace(char,"")

words = text.split()

# count + sort 
word_count = Counter(words)

for word, count in word_count.most_common():
    print(word, ":", count)


# import string

# text = "Hello world! Hello AI. AI is powerful, and AI is the future."

# # 1. Convert to lowercase
# text = text.lower()

# # 2. Remove punctuation
# for char in string.punctuation:
#     text = text.replace(char, "")

# # 3. Split into words
# words = text.split()

# # 4. Count frequency
# word_count = {}

# for word in words:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1

# # 5. Sort by frequency (descending)
# sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

# # 6. Print result
# for word, count in sorted_words:
#     print(word, ":", count)