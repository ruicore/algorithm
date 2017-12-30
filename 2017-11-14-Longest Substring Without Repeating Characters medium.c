#include<stdio.h>
#include<time.h>
#include<stdlib.h>
#include<string.h>
#include<stdbool.h>	

//Given a string, find the length of the longest substring without repeating characters.
//
//Examples:
//
//Given "abcabcbb", the answer is "abc", which the length is 3.
//
//Given "bbbbb", the answer is "b", with the length of 1.
//
//Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

int CheckExit(int* str, char ch, int position) //check weather the char is already exist,if is,return id,if not, return 0 
{
	int temp = 0;
	temp = ch % 128 + 1;	 //每一个字母对应1-128中的一个数
	if (!str[temp])//如果不存在，则在该位置存入第一次出现的位置，从1开始编号
	{
		str[temp] = position; //position 为id号，从1开始编号
		return 0;
	}
	else
		return str[temp]; //返回值为该元素在区间【i，j）中第一次出现的位置加一
}

void Clear(int *clear_str,char* ori_str, int start, int end)//从起时开始清除，包括头尾
{
	int i = 0;
	int real_position = start;//真实id号
	for (i = 0; i <= end - start; i++)//start为str的真实id号
	{
		clear_str[ori_str[real_position] % 128 + 1] = 0;
		real_position++;
	}

	return;
}

int lengthOfLongestSubstring(char* s)
{
	int * str = calloc(sizeof(int),129);
	int Max = 0, count = 0;
	int Lenth = strlen(s);
	int i = 0, position = 0;
	int start = 0;


	for (i = 1; i <= Lenth; i++)
	{
		position = CheckExit(str, s[i-1], i);//position 为真实id号加一
		if (!position)
		{
			count = i - start;
		}	
		else
		{
			Clear(str, s, start, position - 1);//需要真实id号
			str[s[i - 1] % 128 + 1] = i;
			start = position;
			count = i - start;
		}
		if (Max < count)
		{
			Max = count;
		}			
	}
	
	return Max;
}
	
int main()
{
	char * s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmno";
	printf_s("%d", lengthOfLongestSubstring(s));
	system("pause");
}
