#include <stdio.h>

int main(void)
{
    static int limit = 1000;
    static int a, b = 1;

    if(a>limit)
    {
        puts("");
        return 0;
    }
    printf("%d ",a);
    b=a+b;
    a=b-a;

    main();
}