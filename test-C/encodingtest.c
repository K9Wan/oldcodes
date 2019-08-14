#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef union bits_{
    unsigned char ch;
    struct {
        _Bool b1:1;
        _Bool b2:1;
        _Bool b3:1;
        _Bool b4:1;
        _Bool b5:1;
        _Bool b6:1;
        _Bool b7:1;
        _Bool b8:1;
    };
}bits;

void utf8test(bits * str, unsigned * ints)
{
    int cnt=0;
    int byte=0;
    unsigned temp;
    for(int i=0;;i++)
    {
        if(!str[i].ch)
        {
            ints[cnt]=0;
            return;
        }
        if(str[i].b8==0)
        {
            ints[cnt]=str[i].ch;
            cnt++;
        }
        if(str[i].b8&&str[i].b7&&!str[i].b6)
        {
            byte=2;
            temp=(unsigned char)(str[i].ch<<3)>>3;
        }
        if(str[i].b8&&str[i].b7&&str[i].b6&&!str[i].b5)
        {
            byte=3;
            temp=(unsigned char)(str[i].ch<<4)>>4;
        }
        if(str[i].b8&&str[i].b7&&str[i].b6&&str[i].b5&&!str[i].b4)
        {
            byte=4;
            temp=(unsigned char)(str[i].ch<<5)>>5;
        }
        if(str[i].b8&&str[i].b7&&str[i].b6&&str[i].b5&&str[i].b4&&!str[i].b3)
        {
            byte=5;
            temp=(unsigned char)(str[i].ch<<6)>>6;
        }
        if(str[i].b8&&str[i].b7&&str[i].b6&&str[i].b5&&str[i].b4&&str[i].b3&&!str[i].b2)
        {
            byte=6;
            temp=(unsigned char)(str[i].ch<<7)>>7;
        }
        if(str[i].b8&&!str[i].b7)
        {
            if(byte>1)
            {
                byte--;
                temp<<=6;
                temp+=(unsigned char)(str[i].ch<<2)>>2;
                if(byte==1)
                {
                    ints[cnt]=temp;
                    cnt++;
                    byte--;
                }
            }
            else return;
        }
    }
}

void printbits(bits bits)
{
    printf("%i",bits.b1);
    printf("%i",bits.b2);
    printf("%i",bits.b3);
    printf("%i",bits.b4);
    printf("%i",bits.b5);
    printf("%i",bits.b6);
    printf("%i",bits.b7);
    printf("%i",bits.b8);
    puts("");
}

int main(void)
{
    unsigned char han[30]="한글aaa";
    bits b[30];
    unsigned i[30];
    memcpy(b,han,sizeof(b));

    for(int i=0;han[i];i++)
    {
        printf("%hhx ",han[i]);
    }
    puts("");

    puts((const char *)(&han[0]));

    bits ttt={.ch=(han[1]<<2)};
    ttt.ch>>=2;
    printbits(ttt);
    unsigned char tt=95;
    int kk=(char)(tt<<2)>>2;
    printf("%i\n",kk);

    utf8test(b,i);
    for(int k=0;i[k];k++)
    {
        printf("%x ",i[k]);
    }
    puts("");

    return 0;
}