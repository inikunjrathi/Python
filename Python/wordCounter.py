# In this file, I am going to write a code for counting the number of words in a file.
path = input(
    "Enter the path of the file for which you want to count the number of words : ")

file = open(path)

data = file.read()

words = data.split(" ")
numberOfWords = len(words)
print("Total number of words in this file is : " + str(numberOfWords))

sentences = data.split(".")
numberOfSentences = len(sentences) - 1
print("Total number of sentences in this file is : " + str(numberOfSentences))
