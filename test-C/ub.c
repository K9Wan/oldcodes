#include <stdio.h>
#include <stdlib.h>
//UB
int main(void) {
	int a[10][10];
	for(int i=0;i<10;i++)
	{
		for(int j=0;j<10;j++)
		{
			a[i][j] = i*10+j;
		}
	}
 
	int * p=a[0];
 
	struct {
		int a[10];
	} *pa;
	struct {
		int a[10];
		int b[];
	} *pb;
 
	pa = malloc(100*sizeof *pa);
	pb = malloc(100*sizeof *pb);
 
	for(int i=0;i<100;i++)
	{
		pa->a[i] = i;
		pb->a[i] = i;
	}
 
	printf("%d %d %d %d %d %d\n",p[35],a[0][36],a[4][-3],(p+40)[-2], a[11][-71], a[-1][50]);
	printf("%d %d %d\n",pa->a[45],pb->b[36],pb->a[47]);
 
	free(pa);
	free(pb);
 
	return 0;
}