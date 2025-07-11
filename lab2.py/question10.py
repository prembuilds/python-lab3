text = input("Enter a sentence: ")
vowels = {'a', 'e', 'i', 'o', 'u'}
sentence = text.lower()
found_vowels = set()

for char in sentence:
    if char in vowels:
        found_vowels.add(char)

print("Unique vowels:", found_vowels)
