# PracticeProject.py

# Code to practice using Git

def main():
 """Calculate the nth fibonacci number"""

num = int(input("Which fib number do you want? "))

# start n = 1 -> 1
#       n = 2 -> 1
#       n = 3 -> 2

if num == 1 or num == 2:
    print(f"The {num}st/nd fibonaci number is 1")

l = []
x=1
y=1
for i in range(num):
   a = x + y
   x = y
   y = a
   a.append(l)

print(a)

# 112358



if __name__ == "__main__":
    main()
