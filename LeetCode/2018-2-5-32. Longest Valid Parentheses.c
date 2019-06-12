#define _CRT_SECURE_NO_WARNINGS //去掉vs安全检查
#include<stdio.h>
#include<stdlib.h>
#include<limits.h>
#include<string.h>
#include<time.h>

int longestValidParentheses(char* s)
{
	int len = strlen(s), max = 0, top = 0, i, tmp = 0;
	int* pos_stack = (int*)malloc(sizeof(int)*len);
	char* str_stack = (char*)malloc(sizeof(char)*len);

	for (i = 0; s[i]; i++)
	{
		if (s[i] == '(')
		{
			str_stack[top] = '(';
			pos_stack[top] = i;
			top++;
		}
		else
		{
			if (str_stack[top - 1] == '(')//难道不会越界	
			{
				top--;
				if (top == 0)
					tmp = i + 1;
				else
					tmp = i - pos_stack[top - 1];
				max = max > tmp ? max : tmp;
			}
			else
			{
				str_stack[top] = ')';
				pos_stack[top] = i;
				top++;
			}
		}
	}

	return max;
}

int main()
{
	char *s=")()())()()(";
	printf_s("%d", longestValidParentheses(s));

	system("pause");
}

