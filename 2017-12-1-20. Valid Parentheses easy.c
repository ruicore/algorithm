#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
#include <malloc.h>
#include <limits.h>

/*20. Valid Parentheses
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not*/

bool isValid(char* s) 
{
	int s_sum = 0, pos = 0;
	int i = 0;
	char* s_stack = NULL;

	s_sum = strlen(s);
	if (!s_sum)
		return false;
	if (!(s_sum % 2))
	{
		s_stack = (char*)malloc(sizeof(char)*s_sum);
		for (i = 0; i < s_sum; i++)
		{
			switch (s[i])
			{
			case '(':
			case '{':
			case '[':
				s_stack[pos] = s[i];
				pos++;
				break;
			case ')':
				if (pos == 0 || s_stack[(pos-1)] != '(')
					return false;
				pos--;
				break;
			case '}':
				if (pos == 0 || s_stack[(pos-1)] != '{')
					return false;
				pos--;
				break;
			case ']':
				if (pos == 0 || s_stack[(pos-1)] != '[')
					return false;
				pos--;
				break;		
			default:
				break;
			}
		}
	}
	else
		return false;

	if (pos == 0)
		return true;
	else 
		return false;
}
int main()
	{
	char c[10] = { '(',')'};
	if (isValid(c))
		printf_s("true\n");
	else
		printf_s("false\n");
	system("pause");
	
	return 0;
}