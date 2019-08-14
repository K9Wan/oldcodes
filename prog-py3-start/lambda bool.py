import math

print(math.sin(math.tau))
print(math.cos(1.5*math.pi))
print(math.tan(math.pi))
print(math.tan(0.5*math.pi))

bool1 = True, False
T1 = lambda x, y: x
F1 = lambda x, y: y
NEG1 = lambda b: b(F1, T1)
AND1 = lambda x, y: x(y, F1)    #x(y(T1, F1), F1)
OR1 = lambda x, y: x(T1, y)     #x(T1, y(T1, F1))
XOR1 = lambda x, y: x(NEG1(y), y)
NAND1 = lambda x, y: x(y(F1, T1), T1)
NOR1 = lambda x, y: x(F1, y(F1, T1))
NXOR1 = lambda x, y: x(y, NEG1(y))

PQ1 = lambda p, q: p(q(T1, F1), T1)
print(T1,F1)
T1.__repr__ = 'True'
F1.__repr__ = 'False'
print(T1,F1)
print(AND1(T1, T1)(*bool1), AND1(T1, F1)(*bool1), AND1(F1, T1)(*bool1), AND1(F1, F1)(*bool1))
print(OR1(T1, T1)(*bool1), OR1(T1, F1)(*bool1), OR1(F1, T1)(*bool1), OR1(F1, F1)(*bool1))
print(XOR1(T1, T1)(*bool1), XOR1(T1, F1)(*bool1), XOR1(F1, T1)(*bool1), XOR1(F1, F1)(*bool1))
print(NAND1(T1, T1)(*bool1), NAND1(T1, F1)(*bool1), NAND1(F1, T1)(*bool1), NAND1(F1, F1)(*bool1))
print(NOR1(T1, T1)(*bool1), NOR1(T1, F1)(*bool1), NOR1(F1, T1)(*bool1), NOR1(F1, F1)(*bool1))
print(NXOR1(T1, T1)(*bool1), NXOR1(T1, F1)(*bool1), NXOR1(F1, T1)(*bool1), NXOR1(F1, F1)(*bool1))
print(PQ1(T1, T1)(*bool1), PQ1(T1, F1)(*bool1), PQ1(F1, T1)(*bool1), PQ1(F1, F1)(*bool1))

print('-------')

t1 = None; f1 = None
class b1(int):
    def __new__(cls, val=0):
        if val:
            return t1
        else:
            return f1
    
    def __repr__(self):
        if self is t1:
            return 'True'
        else:
            return 'False'
    
    __str__ = __repr__
    
    def __call__(self, x, y):
        if self is t1:
            return x
        else:
            return y
    
    def __bool__(self):
        return self is t1
    
t1 = int.__new__(b1, 1)
f1 = int.__new__(b1, 0)

t2 = None; f2 = None
class b2(str):
    def __new__(cls, val):
        if val.lower()[0]=='t':
            return t2
        else:
            return f2
    
    def __repr__(self):
        return self
    
    __str__ = __repr__
    
    def __call__(self, x, y):
        if self is t2:
            return x
        else:
            return y
    
    def __bool__(self):
        return self is t2
    
t2 = str.__new__(b2, 'True')
f2 = str.__new__(b2, 'False')

