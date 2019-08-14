def factorial_recur(n):
    if(n<=0):
        return 1
    else:
        return n*factorial_recur(n-1)

def factorial_iter(n):
    if(n<=0):
        return 1
    else:
        x=1
        while(n>0):
            x*=n
            n-=1
        return x
    
n=float(input('''number
'''))
print(factorial_iter(n))
print(factorial_recur(n))