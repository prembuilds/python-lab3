text = input("Enter some text: ")
char_count = {}
lower_text = text.lower()

for char in lower_text:
    if char.isalpha():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

for letter, freq in char_count.items():
    print(f"{letter}:{freq}", end=" ")
