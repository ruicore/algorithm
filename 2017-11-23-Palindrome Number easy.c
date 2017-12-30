int Get_length(int x)
{
	int count = 0;

	while (x)
	{
		x /= 10;
		count++;
	}

	return count;
}
bool isPalindrome(int x) 
{
	int length = 0;
	int max = 1,min=1;
	int i = 0, times = 0;
	int temp = x, left = 0, right = 0;


	if (x < 0)
		return false;
	if (x < 10)
		return true;
	length = Get_length(x);
	times = (length + 1) / 2;
	for (i = 0; i < length - 1; i++)
		max *= 10;

	left = temp / max;
	right = temp % 10;

	for (i = 0; i < times; i++)
	{
		if (left == right)
		{
			max /= 10;
			min *= 10;
			left = (temp / max) % 10;
			right = (temp / min) % 10;
		}
		else
			return false;
	}

	return true;
}