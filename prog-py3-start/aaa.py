(x,y)=(0,0)
(dx,dy)=(0,1)
print(x)
code_temp=list()
while True:
    try:
        put=input()
    except EOFError:
        break
    code_temp.append(tuple(put))
code=tuple(code_temp)
print(code)

read=0

aaaa=0

while True:
    try:
        read=ord(code[y][x])
        print(read)
    except IndexError:
        if dx>0 and dy==0:
            read=ord(code[y][0])
        elif dx<0 and dy==0:
            read=ord(code[y][-1])
        elif dx==0 and dy>0:
            read=ord(code[0][x])
        elif dx==0 and dy<0:
            read=ord(code[-1][x])
        else:
            break
    if read in range(0xac00,0xd7a4):
        read-=0xac00
        print("@@",read,"%%")
    x+=dx
    y+=dy
    aaaa+=1
    if aaaa>30:
        break