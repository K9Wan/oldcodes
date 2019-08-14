k=list()
while True:
    try:
        a=input()
        k.append(a)
    except EOFError:
        break
kk={'도':523,'레':587,'미':659,'파':698,'솔':784,'라':880}
for i in k:
    print('sound [{} 500]'.format(kk[i]),end=' ')
