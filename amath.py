import math
def stat_mean(list):
    return(sum(list)/len(list))
def stat_median(list):
    list.sort()
    if len(list) % 2 == 1:
        a = (len(list)-1)/2
        a = int(a)
        return(list[a])
    elif len(list) % 2 == 0:
        a = len(list)/2
        a = int(a)
        b = a - 1
        return((list[a]+list[b])/2)
def stat_range(list):
    list.sort()
    a = len(list)-1
    return(list[a]-list[0])
def root(a,b):
    return(round(a**(1/b),3))
def prime(num):
    num = int(num)
    for i in range(2,num):
        if num % i == 0:
            return(False)
            break
        else:
            pass
    return(True)
def gcf(a,b):
    for i in range(1,a+1):
        if b % i == 0 and a % i == 0:
            c = i
    return(c)
def lcm(a,b):
    return((a*b)/gcf(a,b))
def factorial(x):
    y = 1
    for i in range(1,x+1):
        y = y*i
    return(y)
def pair(x,y):
    x1 = factorial(x)
    y1 = factorial(y)
    z = x-y
    z = factorial(z)
    y = y1*z
    return(x1/y)
