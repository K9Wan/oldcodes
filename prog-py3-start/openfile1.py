f=open("newfile.txt",'w')
for i in range(1,11):
    data="It's %d line\n"%i
    f.write(data)
f.close()