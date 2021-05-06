# Biggie Size
def biggie_size(lst):
    for x in range(len(lst)):
        if(lst[x]>0):
            lst[x]="big"
    return lst

print(biggie_size([-1,3,5,-5]))

# Count Positives
def count_positives(lst):
    count = 0
    for x in range(len(lst)):
        if(lst[x] > 0):
            count += 1
    lst[len(lst)-1] = count
    return lst

print(count_positives([1,6,-4,-2,-7,-2]))

# Sum Total 
def sum_total(lst):
    sum = 0
    for x in range (len(lst)):
        sum += lst[x]
    return sum

print(sum_total([1,2,3,4]))

# Average
def average(lst):
    sum = 0
    for x in range (len(lst)):
        sum += lst[x]
    return (sum/len(lst))

print(average([1,2,3,4])) 

# Length 
def length(lst):
    return len(lst)

print(length([37,2,1,-9]))

# Minimum 
def minimum(lst):
    if(len(lst) == 0):
        return "False"
    else:
        min = lst[0]
        for x in range (len(lst)):
            if(lst[x]<min):
                min = lst[x]
    return min

print(minimum([37,2,1,-9])) 

# Maximum 
def maximum(lst):
    if(len(lst) == 0):
        return "False"
    else:
        max = lst[0]
        for x in range (len(lst)):
            if(lst[x]>max):
                max = lst[x]
    return max

print(maximum([37,2,1,-9])) 

# Ultimate Analysis 
def ultimate_analysis(lst):
    my_dictionary = {"sumTotal":sum_total(lst), "average":average(lst),"minimum":minimum(lst),"maximum":maximum(lst),"length":len(lst)}
    return my_dictionary

print(ultimate_analysis([37,2,1,-9]))

# Reverse List
def reverse_list(lst):
    temp = 0
    for x in range (int(len(lst)/2)):
        temp = lst[x]
        lst[x] = lst[len(lst)-1-x]
        lst[len(lst)-1-x] = temp
    return lst

print(reverse_list([37,2,5,1,-9]))