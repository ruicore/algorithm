#include<stdio.h>
#include<malloc.h>
#include<stdlib.h>
#include<limits.h>
#include<math.h>
#include<stdbool.h>

// This code is copied from http://www.voidcn.com/article/p-qrwimfvx-gq.html
// for more information please visit this site

int getBits(int num)
{
	int length = 0;

	while (num)
	{
		length++;
		num = num >> 1;
	}

	return length;
}

int getBit(int num, int pos)
{
	pos = pos - 1;
	int index = 1 << pos;

	if ((num&index) >> pos)
		return 1;
	else
		return 0;
}

int divide(int dividend, int divisor)
{
	int divide = 0, res = 0;

	bool minus = false, minValue = false;

	if (dividend < 0 || divisor < 0)
	{
		if (dividend < 0 && divisor < 0)
		{
			dividend = -dividend;
			divisor = -divisor;
		}
		else
		{
			dividend = abs(dividend);
			divisor = abs(divisor);
			minus = true;
		}
		if (dividend == -2147483648)
		{
			minValue = true;
			dividend = dividend - 1;
		}
		if (divisor == -2147483648)
		{
			if (minValue)
				return 1;
			return 0;
		}
	}
	if (dividend<divisor)
		return 0;

	if (divisor == 1)
	{
		if (minus)
		{
			if (minValue)
				return -dividend - 1;
			else
				return -dividend;
		}
		else
			return dividend;
	}
	int index = getBits(dividend);
	while (index>0)
	{
		int val = getBit(dividend, index--);
		divide = (divide << 1) + val;

		if (divide<divisor)
			res = res << 1;
		else {
			res = (res << 1) + 1;
			divide = divide - divisor;
		}
	}
	if (minValue && (divide + 1) >= divisor)
	{
		res++;
		divide = divide + 1 - divisor;
	}
	if (minus) {
		return -res;
	}
	return res;
}


int main()
{
	printf_s("%ld", divide(1010369383,-2147483648));
	system("pause");
}