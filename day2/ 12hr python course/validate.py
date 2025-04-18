# name = input("Enter your full name:")
# phone_number = input("Enter you phone number")


# result = name.find("y")
# name = name.capitalize()
# name = name.upper()
# name = name.lower()
# result = name.isdigit()
# result = name.isalpha()
# phone_number = phone_number.count("_")


# print(result)
# print(phone_number)

# print(help(str))

username = input("Enter your username:")
if len(username) > 12:
    print("your username can't be more than 12 characters")
elif not username.find(" ") == -1:
    print(f"Welcome{username}")
elif not username.isalpha():
    print("your username cant contain numbers")
else:
    print(f"welcome{username}")
