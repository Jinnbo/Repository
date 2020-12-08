# Quiz Game
# Author: Jimmy
# Date: Dec 4

counter = 0
q1 = input("What is 32 + 37? ").lower().strip("-,./!")

if q1 == "69" or q1 == "sixty nine" or q1 == "sixtynine":
    counter += 1
    print("Correct!")
else:
    print("Incorrect. The answer is 69")

q2 = input("Are you a guy? ").lower().strip(",./!")

if q2 == "yes" or q2 == "yea" or q2 == "yup" or q1 == "correct":
    counter += 1
    print("You are correct!")
else:
    print("Hmmmm")

q3 = input("Whos the coolest person you know? ").lower().strip(",./!")

if q3 == "jimmy":
    print("Correct!")
    counter += 1
else:
    print("Incorrect. It is Jimmy")

q4 = input("How old is Jimmy? ").lower().strip(",./!")

if q4 == "17" or q4 == "seventeen":
    counter += 1
    print("Correct!")
else:
    print("Incorrect")

q5 = input("How many seconds are in an hour? \n A. 3600 \n B. 600 \n C. 36000 \n D. 6000 \n").lower().strip("-,./!")

if q5 == "a":
    print("Correct!")
    counter += 1
else:
    print("Incorrect. There are 3600 seconds in an hour")

if counter >= 3:
    print(f"Congrats you passed! Your score is {counter/5*100}%")
elif counter < 3:
    print(f"YOU FAILED. You got {counter/5*100}%")