# conditional expression
# print or assign one of two values based on a condition
# X if condition else y

num = 6
a = 6
b = 7
age = 13
temperature = 30
user_role = "Student"

# print("positive" if num > 0 else "Negative")
# result = "EVEN" if num % 2 == 0 else "ODD"
# status = "Adult" if age >= 18 else "Child"
access_level = "Full Access" if user_role == "admin" else "Limited Access"


print(access_level)
