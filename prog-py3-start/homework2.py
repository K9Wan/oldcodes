import math
if __name__=="__main__":
    n=0
    while(n!=3):
        n=int(input('1-triang 2-sphere 3-exit\n'))
        if n==1:
            a=float(input('number\n'))
            print(math.sqrt(3)/4*a**2)
        elif n==2:
            a=float(input('number\n'))
            print(4/3*math.pi*a**3)
        elif n==3:
            pass
        else:
            continue
else:
    print('imported')

import random

def suffle_iteration(l):
    i=0
    while(i<len(l)*2):
        n=random.randrange(len(l))
        a=l[n]
        del l[n]
        l.append(a)
        i+=1
    return l

def suffle_recursion(l,size):
    if size<0:
        return l
    else:
        n=random.randrange(len(l))
        a=l[n]
        del l[n]
        l.append(a)
        return suffle_recursion(l,size-1)

l=[1,2,3,4,5,6,7,8,9,0]
print(suffle_iteration(l))
print(suffle_recursion(l,len(l)*2))
