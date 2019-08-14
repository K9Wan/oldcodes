#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void)
{
    char list[3][10]={"라멘","돈가스","짜장면"};
    srand(time(NULL));
    printf("%s\n",list[rand()&3]);

    return 0;
}