#define _CRT_SECURE_NO_WARNINGS 
#include<stdio.h>
#include<stdlib.h>
#include<limits.h>
#include<string.h>
#include<time.h>
#include<stdbool.h>
#include <ctype.h>

// 定义最长能够允许输入的明文（密文）字符个数
#define char_max 1000

// 此代码运行环境 Visual Studio 2017
// "#define _CRT_SECURE_NO_WARNINGS" 去掉VS安全检查
// !!!请不要输入中文字符

// 加密解密函数
void singleTablereplacement(char* text, char *result, char*key, bool isEnycript);
// 检查密钥函数
bool check_key(char *key);

int main()
{
	 // 存储输入的明文(或密文)
	char* text = (char*)calloc(sizeof(char),char_max);
	// 存储结果
	char* result = (char*)calloc(sizeof(char),char_max);
	// 存储密钥
	char *key = (char*)calloc(sizeof(char), 27);
	// 加密还是解密
	bool isEnycript = true;
	char ch = 'Y';
	// 错误输入次数，连续出错三次程序退出
	int fail_time = 0;
	// 临时变量，用于清空输入区
	int c = 0;


	printf_s("请输入明文(或密文),以回车键结束:\n");
	// 获取需要加密或解密的字符
	gets(text);
	// 获取密钥
	printf_s("请输入密钥:");
	gets(key);
	
	// 读取密钥,保证输入的密钥只含字母
	while (!check_key(key))
	{
		// 如果连续输入错误超过3次，程序退出
		fail_time++;
		if (fail_time == 3)
		{
			printf_s("连续输入错误超过3次,程序退出\n");
			system("pause");
			return 0;
		}
		printf_s("密钥含有非法字符,请重新输入(密钥只能为字母,且长度小于等于26):");
		gets(key);
		

	}
	fail_time = 0;
	// 选择加密或解密
	printf_s("请问是加密(Y)或解密(N):");
	scanf_s("%c", &ch);
	while (toupper(ch)!='Y'&&toupper(ch)!='N')
	{
		while ((c = getchar()) != '\n' && c != EOF);
		fail_time++;
		if (fail_time == 3)
		{
			printf_s("连续输入错误超过3次,程序退出\n");
			system("pause");
			return 0;
		}
		printf_s("请输入Y(加密)或N(解密):");
		scanf_s("%c", &ch);
	}
	// 执行加密
	singleTablereplacement(text, result, key,true);
	printf_s("%s\n", result);

	free(text);
	free(result);

	system("pause");
	return 0;
}

bool check_key(char *key)
{
	int i = 0, length = 0;

	length = strlen(key);
	for (i = 0; i < length; i++)
	{
		if (!isalpha(key[i]))
			return false;
	}
	return true;
}
void singleTablereplacement(char* text,char *result,char*key,bool isEnycript)
{
	// 存储明文
	char *plain_table = (char*)calloc(sizeof(char), 27);
	// 存储密文
	char *cipher_table = (char*)calloc(sizeof(char), 27);
	// 检查密文中的字母是否重复，哈希值
	int *check_repeat = (int*)calloc(sizeof(int), 27);
	int i = 0, pos = 0, pass = 0;

	// 明文字母
	for (i = 65; i < 91; i++)
	{
		plain_table[i-65] = (char)i;
	}

	// 填写密文字母
	i = 0;
	// 依次遍历密钥
	while (key[i])
	{
		// 如果该字母还没有出现过，该字母哈希值所在位置对应为0
		if (!check_repeat[(toupper(key[i]) - 65)])
		{
			// 将密钥放到密文表中
			cipher_table[pos] = toupper(key[i]);
			// 标记该字母已经出现过
			check_repeat[(toupper(key[i]) - 65)] = 1;
			pos++;
		}
		i++;
	}
	for (i = 65; i < 91; i++)
	{
		// 把没有出现过的密钥字母填入密文表中
		if (!check_repeat[i - 65])
		{
			cipher_table[pos] = (char)i;
			check_repeat[i - 65] = 1;
			pos++;
		}
	}

	// 进行加密或解密
	i = 0;
	if (isEnycript)
	{
		while (text[i])
		{
			// 如果是字母,找到该明文字母对应的密文字母
			if (isalpha(text[i]))
				result[i - pass] = cipher_table[toupper(text[i]) - 65];
			// 去掉所有' ','\t','\n','\v','\r','\f'显示为空的字符
			else if (isspace(text[i]))
			{
				i++;
				pass++;
				continue;
			}
			// 其它字符原样输出
			else
				result[i - pass] = text[i];
			i++;
		}
	}
	else
	{
		while (text[i])
		{
			if (isalpha(text[i]))
				result[i - pass] = plain_table[toupper(text[i] - 65)];
			else if (isspace(text[i]))
			{
				i++;
				pass++;
				continue;
			}
			else
				result[i - pass] = text[i];
			i++;
		}
	}

	return;
}