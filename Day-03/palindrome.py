word = input("Enter a word: ").strip().lower()

reversed_word = word[::-1]

print("Original word:", word)
print("Reversed word:", reversed_word)

if word == reversed_word:
    print("It is a palindrome!")
else:
    print("It is not a palindrome.")
