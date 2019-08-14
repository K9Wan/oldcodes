#include <stdio.h>
#include <stdlib.h>

#define FILENAMELENGTH 300

int main(void)
{
	char filename[FILENAMELENGTH];
	FILE * fp;

	printf("Input File Name?\n");
	scanf("%s", filename);

	if ((fp = fopen(filename, "r")) == NULL)
	{
		perror("");
		exit(1);
	}



    fclose(fp);

    return 0;
}