#include<stdio.h>
#include<time.h>
#include<stdlib.h>
#include<string.h>
#include<stdbool.h>	

//Given a string s, find the longest palindromic substring in s.You may assume that the maximum length of s is 1000.
//
//Example:
//
//Input: "babad"
//
//	Output : "bab"
//
//	Note : "aba" is also a valid answer.
//	Example :
//
//	Input : "cbbd"
//
//	Output : "bb"



char* longestPalindrome(char* s) 
{
	int length = 0, max = 0, count = 0, result_length = 0;
	int i = 0, left= 0 , rigth = 0;
	int result_left = 0, result_right = 0;
	char *result = NULL;

	length = strlen(s);

	if (length - 1)
	{
		for (i = 0; i < length - 1; i++)
		{
			left = i, rigth = i + 1, count = 0;
			while (left >= 0 && rigth < length)
			{
				if (s[left] == s[rigth])
				{
					count++;
					left--;
					rigth++;
				}
				else
					break;
			}
			if (count > max)
			{
				max = count;
				result_left = left + 1;
				result_right = rigth - 1;
			}
		}
		for (i = 1; i < length - 1; i++)
		{
			left = i - 1, rigth = i + 1, count = 1;
			while (left >= 0 && rigth < length)
			{
				if (s[left] == s[rigth])
				{
					count++;
					left--;
					rigth++;
				}
				else
					break;
			}
			if (count > max)
			{
				max = count;
				result_left = left + 1;
				result_right = rigth - 1;
			}
		}
		result_length = result_right - result_left + 2;
		result = (char*)malloc(sizeof(char)*result_length);
		for (i = 0; i < result_length; i++)
		{
			result[i] = s[result_left];
			result_left++;
		}
		result[result_length - 1] = NULL;
		//printf_s("%d", result_left);
	}
	else
	{
		return	s;
	}

	return result;
}

int main()
{
	char *s ="civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth";
	printf_s("%s", longestPalindrome(s));
	system("pause");
}