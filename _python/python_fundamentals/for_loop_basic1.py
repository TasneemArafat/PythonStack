# Basic
for x in range (151):
    print(x, end=",")

# Multiples of Five
for x in range (5,1001,5):
    print(x, end=",")

# Counting, the Dojo Way
for x in range (1,101):
    if (x % 5) == 0:
        print("coding")
    if (x % 10) == 0:
        print("coding Dojo")

# Whoa. That Sucker's Huge
sum = 0
for x in range (1,500000,2):
    sum = sum + x
print(sum)

# Countdown by Fours
for x in range (2018,0,-4):
    print(x, end=",")

# Flexible Counter
lowNum = 2
highNum = 9
mult = 3
for x in range (lowNum, highNum+1):
    if(x % mult) == 0:
        print(x)