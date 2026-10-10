sentence = input("Enter a sentence: ")

words = sentence.split()

word_count = len(words)
character_count = len(sentence)
characters_without_spaces = len(sentence.replace(" ", ""))

print(f"Word count: {word_count}")
print(f"Character count: {character_count}")
print(f"Characters without spaces: {characters_without_spaces}")
