#include<stdio.h>
#include<stdlib.h>
#include<limits.h>
#include<string.h>
#include<time.h>
#include<stdbool.h>

bool isMatch(char* s, char* p) 
{
	if (*p == '\0') return *s == '\0';

	if (*(p + 1) != '*')
	{
		if (*p == *s || *p == '.'&&*s != '\0')
			return isMatch(s + 1, p + 1);

		return false;
	}
	else
	{
		while (*p == *s || *p == '.'&&*s != '\0')
		{
			if (isMatch(s, p + 2))
				return true;
			s++;
		}
		return isMatch(s, p + 2);
	}
}


int main()
{

	system("pause");
}