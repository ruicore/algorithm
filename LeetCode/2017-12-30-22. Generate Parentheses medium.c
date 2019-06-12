#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<malloc.h>
#include<limits.h>
#include<math.h>
#include<time.h>

//22. Generate Parentheses
//Given n pairs of parentheses, write a function to generate all combinations of well - formed parentheses.
//
//For example, given n = 3, a solution set is :
//
//[
//	"((()))",
//	"(()())",
//	"(())()",
//	"()(())",
//	"()()()"
//]
//void generate(int leftNum, int rightNum, string s, vector<string> &result)
//{
//	if (leftNum == 0 && rightNum == 0)
//	{
//		result.push_back(s);
//	}
//	if (leftNum>0)
//	{
//		generate(leftNum - 1, rightNum, s + '(', result);
//	}
//	if (rightNum>0 && leftNum<rightNum)
//	{
//		generate(leftNum, rightNum - 1, s + ')', result);
//	}
//}


void recursion(int left, int right, int position, char *s,char **result,int *count,int n)
{
	if (left == 0 && right == 0)
	{

		result[(*count)] = (char*)malloc(sizeof(char)*(2 * n));
		for (int i = 0; i < 2 * n; i++)
		{
			result[(*count)][i] = s[i];
			printf_s("%c", s[i]);
		}
		(*count) ++;
		printf_s(" count = %d\n", *count);
	
		return;
	}
	if (left > 0)
	{
		s[position] = '(';
		recursion(left - 1, right, position + 1, s, result, count, n);
	}
	if (right > 0 && left < right)
	{
		s[position] = ')';
		recursion(left, right - 1, position + 1, s, result, count, n);
	}
	 
}

char** generateParenthesis(int n, int* returnSize)
{
	int count = 0;
	char **result = (char**)malloc(sizeof(char*)*10000);//注意，动态分配好像有数量限制
	char *s = (char*)malloc(sizeof(char)*(2 * n + 1));

	recursion(n, n, 0, s, result, &count, n);
	
	*returnSize = count;
	return result;
}


int main()
{

	int returnSize=0;

	generateParenthesis(5, &returnSize);

	system("pause");

}