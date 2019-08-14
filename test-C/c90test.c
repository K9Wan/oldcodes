#include <stdio.h>
#include <stdlib.h>

void printArray(int arr[], int count)
{
    for (int i = 0; i < count; i++)
    {
        printf("%d ", arr[i]);
    }

    printf("\n");
}

int main()
{
    // 복합 리터럴 방식으로 배열을 넘겨줌
    printArray((int[]) { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 }, 10);

    typedef struct {
        int a[3];
        int i[];
    } a,*pa;
    
    pa k=malloc(sizeof(*k)+20*sizeof(int));

    (k->i)[10]=8;
    printf("%d",k->i[10]);

    {
    char kkkk[10];
    }
    struct aaa{
        struct{
            int xyz[3];
            struct{
                int x;
                int y;
                int z;
            };
        };
    };

    int ttt=0;
    ttt+=7;
    printf("%d",ttt);
    
    int yyy;
    for(yyy=0;yyy<5;yyy++)
    {
        printf("%d",yyy);
    }
    

    return 0;
}

//-std=c90 -pedantic 옵션으로 컴파일시 for(int i)에러, //주석 사용에러, 복합리터럴 경고 나타남
//cd "/home/k9w/aaaa/test-C/" && gcc c90test.c -o c90test -std=c90 -pedantic && "/home/k9w/aaaa/test-C/"c90test
//cd "/home/k9w/aaaa/test-C/" && gcc c90test.c -o c90test -std=c99 -pedantic && "/home/k9w/aaaa/test-C/"c90test