
# Countdown 
count = []
def countdown (num):
    for x in range(0,num+1,1):
        count.append(num-x)
    return count

print(countdown(5))


# Print and Return 
def print_and_return (two):
    print(two[0])
    return two[1]

print(print_and_return([3,5]))

# First Plus Length
sum = 0
def first_plus_length(lst):
    sum = lst[0] + len(lst)
    return sum

print(first_plus_length([1,2,3,4,5]))

# Values Greater than Second 
def values_greater_than_second(lst):
    if(len(lst)<2):
        return "False"
    else:
        newlst = []
        count = 0
        for x in range(0, len(lst)):
            if(lst[x] > lst[1]):
                count+=1
                newlst.append(lst[x])
    print(count)
    return newlst

print(values_greater_than_second([5,2,3,2,1,4]))

# This Length, That Value 
def length_and_value(x,y):
    lst = []
    for i in range(x):
        lst.append(y)
    return lst
print(length_and_value(6,2))
