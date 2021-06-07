"""a = float(input("Enter the first number : "))
b = float(input("Enter the second number : "))
c = a+b
print("Sum of the numbers is : ", c)"""

a = int(input("Enter the number : "))
if a % 2 == 0:
    print("The number you have entered is even.")
else:
    print("The number you have entered is odd.")

print("Table of :", a)

for i in range(1, 11):
    print(a, "*", i, "=", int(a*i))

# Checking whether a number is prime or not except for 1 and 2

flag = 0

for i in range(2, int(a)):
    if a % i == 0:
        print("The number you have entered is not a prime number.")
        flag = 1
        break

    else:
        continue

if flag == 0:
    print("The number you have entered is a prime number.")

# Checking wheter number is prime or not if user enters 1 or 2
if a == 2:
    print("The number you have entered is a prime number.")
elif a == 1:
    print("The number you have entered is not a prime number.")
