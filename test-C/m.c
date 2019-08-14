#include <stdio.h>

int main(void)
{
    static int cnt = 10;
    if(cnt<0)
    {
        puts("");
        return 0;
    }
    printf("%d ",cnt);
    cnt--;

    main();
}