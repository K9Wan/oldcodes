class Animal:
    LEGS=0

    def __init__(self):
        self.arms=2
    
    def cry(self):
        print('aaaah'*self.arms)
    
    def ccry(self):
        print('aaaahh'*Animal.LEGS)

class Duck(Animal):
    LEGS=2
    
    def __init__(self):
        self.arms=0
    
    def cry(self):
        print('quack quack')

class Human(Animal):
    def cry(self):
        print('ooooh')

a1=Animal()
a2=Animal()
a1.LEGS=-1
a1.arms=1
d1=Duck()
h=Human()

print(a1.LEGS)
print(a2.LEGS)
print(a1.arms)
print(a2.arms)
a1.cry()
a2.cry()
a1.ccry()
a2.ccry()
print(d1.LEGS)
print(h.arms)
print(d1.arms)
h.cry()
d1.cry()