#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
#include <malloc.h>
#include <limits.h>

char c[10][10] = { "","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz" };//数字代表的字符  
int total[10] = { 0,0,3,3,3,3,3,4,3,4 };//数字代表的字符个数  

void RS(int *number, int *answer, int index, int n,int *retunSize,char **result)
{

	if (index == n)//判断是否为最后一位  
	{
		int i = 0;
		result[(*retunSize)] = (char*)malloc(sizeof(char)*n);
		for (i = 0; i < n; i++)
			result[(*retunSize)][i] = c[number[i]][answer[i]];
		result[(*retunSize)][i] = NULL;
		(*retunSize)++;

		return;
	}
	for (answer[index] = 0; answer[index] < total[number[index]]; answer[index]++)
		RS(number, answer, index + 1, n, retunSize, result);
}

char** letterCombinations(char* digits, int* returnSize) 
{
	char ** result = NULL;
	int *numbers = NULL, *answers = NULL;
	int digit_num = 0, temp_result_num = 1, result_num = 0;
	int i = 0;

	digit_num = strlen(digits);
	if (digit_num)
	{
		numbers = (int*)calloc(sizeof(int), digit_num);
		answers = (int*)calloc(sizeof(int), digit_num);

		for (i = 0; i < digit_num; i++)
			numbers[i] = (int)digits[i] - '0';
		for (i = 0; i < digit_num; i++)
			temp_result_num *= 4;
		result = (char**)malloc(sizeof(char*)*temp_result_num);
		RS(numbers, answers, 0, digit_num, &result_num, result);
		free(numbers);
		free(answers);
		*returnSize = result_num;
	}
	else
	{
		*returnSize = 0;
		return NULL;
	}

	return result;
}

int main()
	{

		int number[11] = {2,5,6};//储存电话号码  
		int n = 3, i = 0, j = 0, num = 0;
		int answer[11] = { 0 };//数字代表的字符的位置  
		char *digits = "32";
		int *returnSize = &num;
		char **re = NULL;

		re=letterCombinations(digits, returnSize);

		//printf_s("%d", num);
		for (i = 0; i < num; i++)
		{
			for (j = 0; j < 4; j++)
				printf_s("%c", re[i][j]);
			printf_s("\n");
		}
		system("pause");
		return 0;
}