#include <stdio.h>

#define ARRAYSIZE 100

char stack[ARRAYSIZE];
int top = -1;

_Bool isFull(void)
{
	if (top >= ARRAYSIZE - 1)
	{
		return (_Bool)1;
	}
	else
	{
		return (_Bool)0;
	}
}

_Bool isEmpty(void)
{
	if (top < 0)
	{
		return (_Bool)1;
	}
	else
	{
		return (_Bool)0;
	}
}

_Bool push(char p)
{
	if (isFull())
	{
		return 0;
	}
	top++;
	stack[top] = p;
	return 1;
}

char pop(void)
{
	if (isEmpty())
	{
		return 0;
	}
	char p = stack[top];
	top--;
	return p;
}

int main(void)
{
	char st;
	char a;
	while (1)
	{
		printf("1 or 2 or 0\n");
		scanf("%hhi", &st);
		switch (st)
		{
		case 1:
			printf("push\n");
			scanf("%hhi", &a);
			push(a);
			break;
		case 2:
			printf("pop\n");
			printf("%i\n", pop());
			break;
		default:
			break;
		}
		if (!st)
		{
			break;
		}
	}


	return 0;
}