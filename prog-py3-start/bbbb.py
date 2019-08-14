readd=[44444,53535,4444,3333,222]
for read in readd:
    if read in range(0xac00,0xd7a4):
        read-=0xac00
        print(read,'aaaa')
    else:
        print(read,'bbbb')

