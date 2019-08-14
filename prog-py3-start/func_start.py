def print_atar(m):
    print('*'*m)

n=input('height: ')
n=int(n)
for i in range(1,n+1):
    print_atar(i)

def sorting_hat(t):
    if t>24:
        print('too hot')
    elif 18<=t<24:
        print('bearable')
    else:
        print('too cold')
t_now=int(input('temperature: '))
sorting_hat(t_now)

def yo():
    print('yo')

for i in range(0,5):
    yo()

def plus(a,b):
    return a+b

for i in range(0,5):
    print(plus(i,i+1))

def so_funky(a, b=20):
    return a + b
def any_func(x, y, z):
    return x * 100 + y * 10 + z
def recur_bomb(num):
    if num <= 0:
        return 0
    return num + recur_bomb(num - 1)

print(recur_bomb(10))
print(recur_bomb(100))
print(recur_bomb(997.000000))
#print(recur_bomb(997.000001))

a: float
a = 10 / 5

b: int
b = "b"

