#include<stdio.h>
#include<malloc.h>
#include<stdlib.h>

int Get_length(char *str)
{
	int length = 0;

	while (str[length])
		length++;

	return length;
}

int strStr(char* haystack, char* needle)
{
	int haystack_length = 0, needle_lenth = 0;
	int i = 0, j = 0;

	haystack_length = Get_length(haystack);
	needle_lenth = Get_length(needle);
	if (haystack[0] == 0 && needle[0] == 0)
		return 0;
	if (haystack[0] == 0 && needle[0] != 0)
		return -1;
	if (haystack[0] != 0 && needle[0] == 0)
		return 0;
	if (haystack_length < needle_lenth)
		return -1;
	while (haystack[i] && needle[j])
	{
		if (haystack[i] == needle[j])
		{
			i++;
			j++;
		}
		else
		{
			i = i - j + 1;
			j = 0;
		}
	}

	if (j >= needle_lenth)
		return i - needle_lenth;
	else
		return -1;
}

int main()
{

	system("pause");
}