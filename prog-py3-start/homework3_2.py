DIRECTION=[(-1,0),(0,1),(1,0),(0,-1)]

i=0
j=0
d=2
list_i=[0]
list_j=[0]
list_P=[[0,0]]

def TL():
    global d
    d=(d-1)%4
def TR():
    global d
    d=(d+1)%4
def GO():
    global i,j,d
    global P,DIRECTION
    global list_i,list_j,list_P
    
    i=i+DIRECTION[d][0]
    j=j+DIRECTION[d][1]
    P=[i,j]
    list_i.append(i)
    list_j.append(j)
    list_P.append(P)
def draw():
    global list_i,list_j
    min_i=min(list_i)
    min_j=min(list_j)
    max_i=max(list_i)
    max_j=max(list_j)
    row=max_i-min_i
    col=max_j-min_j
    #print(list_P)
    #print(max_i,min_i,max_j,min_j)
    #print(row,col)
    for y in range(row+1):
        for x in range(col+1):
            if [y+min_i,x+min_j] in list_P:
                print('.',end=' ')
            else:
                print('#',end=' ')
        print()

length=int(input('''length
'''))
path=list(input('path\n'))
path=path[:length]
for e in path:
    if e=='F':
        GO()
    elif e=='L':
        TL()
    elif e=='R':
        TR()
    else:
        continue
draw()
