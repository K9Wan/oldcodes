f=open('newfile.txt',"r")
while True:
    line=f.readline()
    if not line: break
    print(line)
f.close()

f=open("newfile.txt",'r')
lines=f.readlines()
for line in lines:
    print(line)
f.close()