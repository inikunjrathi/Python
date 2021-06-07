# Take a sentence as an input from the user and count the number of words in it.
a = input("Enter a sentence: ")
print(a)

# String is a list of charecters.
print(len(a))

numberOfWords = 0

for i in range(0, len(a)):
    print(a[i])
    if a[i] == " ":
        numberOfWords += 1

numberOfWords += 1

print("The total number of words are: ", numberOfWords)

words = a.split(" ")
print(words)
print(words[3])
