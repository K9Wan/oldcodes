a={'0':'바','1':'밤빠나','2':'반','3':'받','4':'밤','5':'발','6':'밦','7':'밝','8':'밣','9':'밞','+':'다','-':'타','*':'따','/':'나'}
s=input()
for i in s:
    print(a[i],end='')
print('망하')
k=list()
for i in s:
    if i in '0123456789':
        k.append(i)
    if i in '+-*/':
        k.append('\n')
a=''
print(a.join(k))
print(type('dddd'))
