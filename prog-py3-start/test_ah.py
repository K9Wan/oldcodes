#0   1   2  3   4   5  6   7   8  9  10  11  12 13  14  15  16 17  18
#ㄱ, ㄲ, ㄴ, ㄷ, ㄸ, ㄹ, ㅁ, ㅂ, ㅃ, ㅅ, ㅆ, ㅇ, ㅈ, ㅉ, ㅊ, ㅋ, ㅌ, ㅍ, ㅎ
#0   1   2  3   4   5  6   7   8  9  10  11  12 13  14  15  16 17  18 19  20
#ㅏ, ㅐ, ㅑ, ㅒ, ㅓ, ㅔ, ㅕ, ㅖ, ㅗ, ㅘ, ㅙ, ㅚ, ㅛ, ㅜ, ㅝ, ㅞ, ㅟ, ㅠ, ㅡ, ㅢ, ㅣ
#0 1   2   3  4   5   6  7   8  9  10  11  12  13 14  15  16 17  18 19  20  21  22 23  24  25 26  27
#, ㄱ, ㄲ, ㄳ, ㄴ, ㄵ, ㄶ, ㄷ, ㄹ, ㄺ, ㄻ, ㄼ, ㄽ, ㄾ, ㄿ, ㅀ, ㅁ, ㅂ, ㅄ, ㅅ, ㅆ, ㅇ, ㅈ, ㅊ, ㅋ, ㅌ, ㅍ, ㅎ
#19,21,28
stroke=(0,2,4,4,2,5,5,3,5,7,9,9,7,9,9,8,4,4,6,2,4,-1,3,4,3,4,4,-1)
(x,y)=(0,0)
(dx,dy)=(0,1)
changedirection=1
STACK=list()
for i in range(26):
    STACK.append([])
QUEUE=[]

def push(s,n):
    STACK[s].append(n)
def pop(s):
    try:
        t=STACK[s][-1]
        del STACK[s][-1]
        return t
    except IndexError:
        return None
def enqueue(n):
    QUEUE.append(n)
def dequeue():
    try:
        t=QUEUE[0]
        del QUEUE[0]
        return t
    except IndexError:
        pass

currentbuffer=0

def ii(n):
    if currentbuffer!=21 and currentbuffer!=27:
        push(currentbuffer,n)
    elif currentbuffer==21:
        enqueue(n)
    else:
        pass
def oo():
    if currentbuffer!=21 and currentbuffer!=27:
        out=pop(currentbuffer)
    elif currentbuffer==21:
        out=dequeue()
    else:
        pass
    return out



'''
code_temp=list()
while True:
    put=input()
    code_temp.append(tuple(put))
    if not put:
        break
code=tuple(code_temp)
print(code)
'''
code_temp=list()
print("code")
while True:
    try:
        put=input()
    except EOFError:
        break
    code_temp.append(tuple(put))
code=tuple(code_temp)
print(code)

read=0
onset=0
nucleus=0
coda=0

while True:
    changedirection=1
    
    print(x,y,dx,dy)
    print(code[y][x])
    pause=input()
    
    try:
        read=ord(code[y][x])
    except IndexError:
#    except IndexError as err:
#        print(err)
        if dx>0 and dy==0:
            x=0
            #print('x1')
        elif dx<0 and dy==0:
            '''
            t=0
            while(True):
                try:
                    check=code[y][t]
                except IndexError:
                    break
                t+=1
            x=t-1
            #print('x2')
            '''

            x=-1
        elif dx==0 and dy>0:
            y=0
            #print('y1')
        elif dx==0 and dy<0:
            '''
            t=0
            while(True):
                try:
                    check=code[t][x]
                except IndexError:
                    break
                t+=1
            y=t-1
            #print('y2')
            '''

            y=-1
        else:
            break
        read=ord(code[y][x])
    if read in range(0xac00,0xd7a4):
        read-=0xac00
        onset=(read//21)//28
        coda=read%28
        if onset==2:
            a1=oo()
            a2=oo()
            if a1 is None or a2 is None:
                if a1 is not None:
                    ii(a1)
                changedirection*=-1
            else:
                try:
                    r=a2//a1
                    ii(r)
                except ZeroDivisionError:
                    ii(0)
        elif onset==3:
            a1=oo()
            a2=oo()
            if a1 is None or a2 is None:
                if a1 is not None:
                    ii(a1)
                changedirection*=-1
            else:
                r=a1+a2
                ii(r)
        elif onset==4:
            a1=oo()
            a2=oo()
            if a1 is None or a2 is None:
                if a1 is not None:
                    ii(a1)
                changedirection*=-1
            else:
                r=a1*a2
                ii(r)
        elif onset==5:
            a1=oo()
            a2=oo()
            if a1 is None or a2 is None:
                if a1 is not None:
                    ii(a1)
                changedirection*=-1
            else:
                try:
                    r=a2%a1
                    ii(r)
                except ZeroDivisionError:
                    ii(0)
        elif onset==6:
            if coda==21:
                a=oo()
                if a is None:
                    changedirection*=-1
                else:
                    print(a,end='')
            elif coda==27:
                a=oo()
                if a is None:
                    changedirection*=-1
                else:
                    print(chr(a),end='')
            else:
                if oo() is None:
                    changedirection*=-1
        elif onset==7:
            if coda==21:
                try:
                    iii=int(input('put integer\n'))
                    ii(iii)
                except ValueError:
                    ii(-1)
                except EOFError:
                    ii(-1)
            elif coda==27:
                try:
                    iii=ord(input('put char\n')[:1])
                    ii(iii)
                except EOFError:
                    ii(-1)

            else:
                ii(stroke[coda])
        elif onset==8:
            a=oo()
            if a is None:
                changedirection*=-1
            else:
                ii(a)
                ii(a)
        elif onset==9:
            currentbuffer=coda
        elif onset==10:
            a=oo()
            if a is None:
                changedirection-1
            else:
                t=currentbuffer
                currentbuffer=coda
                ii(a)
                currentbuffer=t
        elif onset==11:
            pass
        elif onset==12:
            a1=oo()
            a2=oo()
            if a1 is None or a2 is None:
                if a1 is not None:
                    ii(a1)
                changedirection*=-1
            else:
                if a2>=a1:
                    ii(1)
                else:
                    ii(0)
        elif onset==14:
            a=oo()
            if not a:
                changedirection*=-1
            else:
                pass
        elif onset==16:
            a1=oo()
            a2=oo()
            if a1 is None or a2 is None:
                if a1 is not None:
                    ii(a1)
                changedirection*=-1
            else:
                r=a2-a1
                ii(r)
        elif onset==17:
            a1=oo()
            a2=oo()
            if a1 is None or a2 is None:
                if a1 is not None:
                    ii(a1)
                changedirection*=-1
            else:
                if currentbuffer!=21 and currentbuffer!=27:
                    ii(a1)
                    ii(a2)
                elif currentbuffer==21:
                    ii(a2)
                    ii(a1)
        elif onset==18:
            break
        nucleus=(read//28)%21
        if nucleus==0:
            dx,dy=1,0
        elif nucleus==2:
            dx,dy=2,0
        elif nucleus==4:
            dx,dy=-1,0
        elif nucleus==6:
            dx,dy=-2,0
        elif nucleus==8:
            dx,dy=0,-1
        elif nucleus==12:
            dx,dy=0,-2
        elif nucleus==13:
            dx,dy=0,1
        elif nucleus==17:
            dx,dy=0,2
        elif nucleus==18:
            dy=-dy
        elif nucleus==19:
            dx,dy=-dx,-dy
        elif nucleus==20:
            dx=-dx
        else:
            pass
        dx*=changedirection
        dy*=changedirection

    else:
        pass
    x+=dx
    y+=dy
    

push(4,7)
push(4,9)
push(4,2)
pop(4)

print('\n------')
a='가힣'

for b in a:
    print(ord(b))
    print(hex(ord(b)))