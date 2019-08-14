#include <stdio.h>

int main(void)
{

    char c;
    scanf("%c",&c);
    switch(c)
    {
    case 'A' ... 'Z':
    printf("aaaa");
    break;
    case 'b':
    printf("bb");
    break;
    default:
    printf("cc");
    }

    printf("saaaa");
    int a=0;
    a++;
    int b=a+2;
    printf("%d",b);
    scanf("%d",&a);
    int sqr[a];
    for(int i=0;i<a;i++)
    {
        sqr[i]=i*i;
        printf("%d ",sqr[i]);
    }
    char bbb[a];
    gets(bbb);
    printf("fff");
    puts(bbb);

    return 0;
}