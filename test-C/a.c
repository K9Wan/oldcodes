#include <stdio.h>
#include <stdlib.h>
#include <uchar.h>

_Noreturn void kkk(void)
{
    exit(1);
}

int main(void)
{
    printf("hello world");
    FILE* fp;
    if((fp=fopen("a","rb"))==NULL)
    {
        exit(1);
    }
    char buffer[10000];
    fread(buffer,sizeof(char),9999,fp);
    printf("%s",buffer);
    
    _Complex a;
    double __complex__ b;
    _Bool c=1;

    puts("aaaa");
    int n;
    printf("dd\n");
    scanf("%d",&n);
    scanf("%d",&n);
    puts("aaaa");
    printf("%d",n);
    int k[n];

    for(int i=0;i<n;i++)
    {
        k[i]=(i+1)*(i+1);
        printf("ddd");
    }
    printf("%d",k[n-3]);

    quick_exit(1);



    

    return 0;
}