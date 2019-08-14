#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define scanfss(p,n) do {\
	int t = (n)-1;\
	int s = t;\
	int digits = 0;\
	while (t)\
	{\
		t /= 10;\
		digits++;\
	}\
	char* f = (char*)malloc((digits + 3) * sizeof(char));\
	memset(f, 0, digits+3);\
	sprintf(f, "%%%ds", s);\
	scanf(f, p);\
	free(f);\
} while (0)

int scanfs(char* p, size_t n)
{
	int t = n - 1;
	int s = t;
	int digits = 0;
	while (t)
	{
		t /= 10;
		digits++;
	}
	char* f = (char*)malloc((digits + 3) * sizeof(char));
	//memset(f, 0, sizeof(f));	//wrong
	memset(f, 0, digits+3);
	sprintf(f, "%%%ds", s);
	int r = scanf(f, p);
	free(f);
	return r;
}

int main(void)
{
	char k1[10]={0,};
	char k2[10]={0,};
	char k3[10]={0,};
	//fgets(k1,10,stdin);
	scanfss(k1, 10);
	scanfs(k2, 10);
	int aaa=scanf("%10c", k3);
	printf("||%s--\n", k1);
	printf("||%s--\n", k2);
	printf("||%s--\n", k3);
	printf("%d\n",aaa);
	for(int i=0;i<10;i++)
	{
		printf("%d ",k3[i]);
	}
	

	return 0;
}