a=int(input())
for i in range(a):
    print(i+1)
b=['a',4,'g','h','d',2]
c=b.pop
print(b,c,c)
size={'x':0}
size['x']=7
print(size)

size_x,size_y=(4,7)
face=list()
line=list()
for x in range(size_x):
    line.append('')
for y in range(size_y):
    face.append(line)

print(face[5][3],1)
print(face[1])