import random
def randInt(min=0, max=100):
    if(min<0):
        min =0
    if(min>max):
        min,max = max,min
    if(min != 0):
        num = random.random()*(max-min) + min
    else:
        num = random.random()*max + min
    
    print(min)
    return round(num)

print(randInt())


