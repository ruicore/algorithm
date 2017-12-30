// 12. Integer to Roman
char* intToRoman(int num) 
{
	char string[13][3] = { "M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I" };
	int      value[13] = { 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 };
	char * result = malloc(sizeof(char) * 100);
	int i = 0,j=0, temp_num = num, position = 0;
	int length = 0;

	for (i = 0; temp_num; i++)
	{
		while (temp_num>=value[i])
		{
			length = strlen(string[i]);
			j = 0;
			while (length)
			{
				result[position] = string[i][j];
				j++;
				position++;
				length--;
			}
			temp_num -= value[i];
		}
	}
	
	result[position] = NULL;

	return result;
}