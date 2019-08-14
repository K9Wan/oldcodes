f=open("newfile.txt",'a')
for i in range(11,20):
    data="It's %d line.\n"%i
    f.write(data)
f.close()