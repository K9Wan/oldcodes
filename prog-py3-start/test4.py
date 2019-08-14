print(dir(str))
'''['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
'''
print(isinstance(str, object))

print(dir(object))
'''['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
'''

print(isinstance(KeyboardInterrupt, BaseException))
print(issubclass(KeyboardInterrupt, BaseException))


print(isinstance(KeyboardInterrupt, object))
print(issubclass(KeyboardInterrupt, object))

class Sample:  
    #name = ''
    average = 0.0
    values = None # list cannot be initialized here!


s1 = Sample()
s1.name = "sample 1"
s1.values=[]
s1.values.append(1)
s1.values.append(2)
s1.values.append(3)

s2 = Sample()
s2.name = "sample 2"
s2.values=[]
s2.values.append(4)

for v in s1.values:   # prints 1,2,3 --> OK.
    print(v)
print("***")
for v in s2.values:   # prints 4 --> OK.
    print(v)

print(s1.name,s2.name, '--'+'Sample.name'+'--')

class aaa:
    #__slots__=['name','age','lists']
    def __init__(self,name='Anne',age='-1',lists=(3,2,1)):
        self.name=name
        self.age=age
        self.lists=list(lists)
        print('aaaaaaaa',self.__dict__)
    

a=aaa(lists=(3,4,5))

print(a.name, a.age, a.lists)
a.name='Alice'
print(a.name)
class bbb:
    def __init__(self,**kwds):
        self.__dict__.update(kwds)

b=bbb(kkk=123,jjj=231)
print(bbb.__dict__.keys())
print(b.jjj)
print(b.__dict__['kkk'])
print(vars(bbb), end = '\n---\n')

class ccc:
    def __init__(self,**kwargs):
        for key,value in kwargs.items():
            setattr(self,key,value)
    def aa(self):
        pass

c=ccc(kkk=5,jjj=4)
print(ccc.__dict__.keys())
print(c.jjj)
print(c.__dict__['kkk'])

'''
setattr(aaa, 'name', 5) #AttributeError: 'aaa' object attribute 'name' is read-only
print(aaa.name,a.name)
setattr(a, 'name', 7)
print(aaa.name,a.name)

setattr(aaa, 'ddff', 5)
print(aaa.ddff,a.ddff)
setattr(a, 'ddff', 7)
print(aaa.ddff,a.ddff)
'''
print({'bbb':5,'ccc':'tt','tt':aaa}.items())
aaa='\'pgnfsadbueabapberbuoaebpaebneubipeaeba'.replace('p','{'+'p'+'}')+'\''+'.format(p=3.14)'
bb=eval(aaa)
print(aaa)
print(bb)
print(str(exec("print(6, str(exec('print(5)')))")))

print(dir(Sample))
print(type(object.__init__))
print(type(ccc.aa))
print(type(ccc))
print(isinstance(object.__init__,object))

print(isinstance(ccc.aa,object))

print(type(object.__init__) == type(ccc.__init__))

print(vars(Sample))
print('')
print(dir(aaa))
if '__dict__' in dir(aaa):
    print(vars(aaa))


print((5).__add__(3))
'''
sum=0
while(True):
    kkk=input('kkk')
    if not kkk:
        break
    ki=int(kkk)
    sum+=ki

print(sum)

sum=0
a=None
while(a!=0):
    a=int(input('aaa:'))
    sum+=a

print(sum)
'''
