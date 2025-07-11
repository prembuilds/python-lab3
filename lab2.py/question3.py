sentence = input("enter a sentence: ")
words = sentence.split(" ")
uniq_words = set(words)
d = {}
for word in uniq_words:
    d[word] = words.count(word)
print(d)

