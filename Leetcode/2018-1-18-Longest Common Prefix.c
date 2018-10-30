#include<stdio.h>
#include<malloc.h>
#include<stdlib.h>
#include<limits.h>
#include<math.h>
#include<stdbool.h>
#include<string.h>


char* longestCommonPrefix(char** strs, int strsSize)
{
	char* str = strs[0];
	int i, j;
	if (strsSize == 0)return "";
	for (i = 1; i<strsSize; i++) 
	{
		j = 0;
		while (str[j] && strs[i][j] && str[j] == strs[i][j])j++;
		str[j] = 0;
	}

	return str;
}

int main()
{
	printf_s("%ld", divide(1010369383,-2147483648));
	system("pause");
}