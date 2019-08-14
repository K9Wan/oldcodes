def t(f):
    c=(f-32)/1.8
    return c
a=[31,168,48,123]
for i in range(0,4):
    print('{:>6.1f}'.format(a[i]))

s1='개굴 '
s2='개구리'
s3='노래를'
s0='프로그 코딩을 한다~'
print(s1*2+s2,s3+s0[7:])

print('({3} - {1:.<2} {0:->2}) / 7{2}{4:0>7.3f}인데, 아무튼 {ahh:~^6} 과제하기 {hate:!<5})'.format(98%8, [1][0], " = ", 100//12, 5/7, ahh='아아', hate='싫다'))

animal='aaa개'
if('개' in animal):
    print('멍멍')
else:
    print('야옹')

def printscore(n):
    if(n<40):
        score='F'
    elif(n<50):
        score='D'
    elif(n<70):
        score='c'
    elif(n<90):
        score='B'
    elif(n<100):
        score='A'
    else:
        score=False
    if(score!=False):
        print('당신의 점수는 {0}점이군요. 결과는 {1}입니다.'.format(n,score))
    else:
        print('Door has broken by mad students!')
s=[45,95,60,70,49.99,2**5]
for i in range(0,6):
    printscore(s[i])

n=7
list1=[]
for i in range(0,n):
    list1.insert(i,10*(i+1))
print(list1)

l=[50, 20, 40, 10, 30]
print(id(l))
l.insert(1,14)
print(l[2])
del l[0]
print(l[3])
print(l[0])
l.sort()
l[0:2]=[]
for i, ll in enumerate(l):
    print(ll*9//10)
print(id(l))