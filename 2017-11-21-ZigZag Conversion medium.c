char* convert(char* s, int numRows) 
{
	int i = 0, difference = 0, position_result = 0, position_s = 0;
	int length = strlen(s);
	int differenc_change = 1;
	char * result = (char*)malloc(sizeof(char)*(length + 1));

	if (numRows == 1)
		return s;

	position_s = 0;
	difference = 2 * numRows - 2;
	while (position_s < length)
	{
		result[position_result] = s[position_s];
		position_s += difference;
		position_result++;
	}

	for (i = 1; i < numRows - 1; i++)
	{
		differenc_change = 1;
		difference = 2 * numRows - 2 * (i + 1);
		position_s = i;
		while (position_s < length)
		{
			result[position_result] = s[position_s];
			differenc_change++;
			if (!(differenc_change % 2))
				difference = 2 * numRows - 2 * (i + 1);
			else
				difference = i * 2;
			position_s += difference;
			position_result++;
		}
	}
	
	position_s = numRows - 1;
	difference = 2 * numRows - 2;
	while (position_s < length)
	{
		result[position_result] = s[position_s];
		position_s += difference;
		position_result++;
	}
	result[length] = NULL;

	return result;
}