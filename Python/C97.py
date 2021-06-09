# Take a sentence as an input from the user and count the number of words in it.
a = input("Enter a Word: ")
print(a)

# String is a list of charecters.
"""print(len(a))

numberOfWords = 0

for i in range(0, len(a)):
    print(a[i])
    if a[i] == " ":
        numberOfWords += 1

numberOfWords += 1

print("The total number of words are: ", numberOfWords)

words = a.split(" ")
print(words)
print(words[3])"""

# To check whether the entered string is palindrome or not.
s = 0
c = int(len(a)//2)
e = len(a) - 1

print(s, c, e)

flag = 0
while (s < c):
    if a[s] == a[e]:
        s += 1
        e -= 1
    else:
        flag = 1
        break

if flag == 0:
    print("The word entered is a palindrome")
elif flag == 1:
    print("The word entered is not a palindrome")
