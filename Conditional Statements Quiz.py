# Quiz Game
# Author: Jimmy
# Date: Dec 4

counter = 0
q1 = input("What is 32 + 37? ").lower().strip("-")

if q1 == "69" or q1 == "sixty nine" or q1 == "sixtynine":
    counter += 1
    print("Correct")
else:
    print("Incorrect")

q2 = input("Are you a guy? ").lower().strip(".")

if q2 == "yes" or q2 == "yea" or q2 == "yup" or q1 == "correct":
    counter += 1
    print("Correct")
else:
    print("Incorrect")

q3 = input("Whos the coolest person you know? ").lower().strip(",.")

if q3 == "jimmy":
    print("Correct!")
    counter += 1
else:
    print("Incorrect. It is Jimmy")

q4 = input("How old are you? ")

if q4 == "17" or q4 == "seventeen":
    counter += 1
    print("Correct")
else:
    print("Incorrect")

q5 = input("How many seconds are in an hour? ").lower().strip("-")

if q5 == "3600" or q5 == "thirty six hundred" or q5 == "three thousand six hundred":
    print("Correct")
    counter += 1
else:
    print("Incorrect")

print(f"Your score is {counter}")