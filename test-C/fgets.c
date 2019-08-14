#include <stdio.h>
#include <stdlib.h>

#define SIZE 7



int main(void)
{
    char str1[SIZE];
    char str2[SIZE];
    char str3[SIZE];
    char aaa[999];

    fgets(str1,SIZE,stdin);
    //scanf("%6[^ ]",str1);
    //int c=scanf("%6[^\n]",str1);
    //int a=scanf("%[^\n]%*c",aaa);
    //int a=scanf("%[^\n]",aaa);
    //getchar();
    //printf("%d %d",c,a);
    char* bb=fgets(str2,SIZE,stdin);
    //scanf("%6s",str2);
    char* cc=fgets(str3,SIZE,stdin);

    printf("||%s--",str1);
    printf("||%s--",str2);
    printf("||%s--",str3);

    printf("%p\n%p\n%p\n%p",str2,bb,cc,NULL);


    return 0;

}