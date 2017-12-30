int reverse(int x) 
{
	bool negative = false;
	int num = 0, temp_num = 0, temp = 0;
	int i = 0;

	if (x < 0)
	{
		negative = true;
		x = -x;
	}
	while (x)
	{
		if (num > (INT_MAX - x % 10) / 10)//这句话用来判断是否一出，这句话不懂
			return 0;
		num = num * 10 + x % 10;
		x = x / 10;
	}

	if (negative)
		return -num;
	return num;
}