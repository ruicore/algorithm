#include<stdio.h>
#include<malloc.h>
#include<stdlib.h>
#include<limits.h>
#include<math.h>
#include<stdbool.h>
#include<string.h>


// this code is come from http://blog.csdn.net/runningtortoises/article/details/45557659

int myAtoi(char* str)
{
	int flag = 1, res = 0, dig = 0;

	while (*str == ' ')
		str++;
	
	if (*str == '-')
	{
		flag = -1;
		str++;
	}
	else if (*str == '+')
	{
		str++;
	}

	while (*str)
	{
		if (*str<'0' || *str>'9')
		{
			return flag * res;
		}
		dig = *str - '0';
		if (flag == 1 && res*10.0 + dig > INT_MAX)
		{
			return INT_MAX;
		}
		else if (flag == -1 && -res * 10.0 - dig < INT_MIN)
		{
			return INT_MIN;
		}
		res = res * 10 + dig;
		str++;
	}

	return flag * res;
}

int main()
{
	printf_s("%ld", divide(1010369383,-2147483648));
	system("pause");
}