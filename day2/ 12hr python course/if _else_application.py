# if = #do some code only if some condition is true
#      else do something else
age = int(input("Enter your age:"))

if age == range(18, 40):
    print("You are now signed up!")
elif age < 0:
    print("you have not been born yet!")
elif age > 40:
    print("WTF ARE YOU EVEN DOING HERE RETARD")
else:
    print("you must be 18+ to sign up")
