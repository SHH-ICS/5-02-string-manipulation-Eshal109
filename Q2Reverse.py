# Create a program that will accept a word and output the word one letter at a time in reverse.

word = input("Enter a word:")
for letter in reversed(word):
    print(letter)

def word_triangle():
    word = input("Enter a word: ")

    for i in range(1, len(word) + 1):
        print(word[:i])

word_triangle()
