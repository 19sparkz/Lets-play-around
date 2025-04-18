# while loop = execute some code WHILE some condition remians true

# name = input("enter your name:")

# while name == "":
#    print("You did not enter your name")

# age = int(input("enter your age:"))

# while age < 0:
#    print("age cant be negative")

# print(f"you are {age} years old")

num = int(input("enter a #between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("enter a #between 1 - 10: "))

print(f"your number is {num}")
