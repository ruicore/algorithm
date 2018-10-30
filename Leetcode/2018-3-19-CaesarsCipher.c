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
// 为了简化输入逻辑，此代码默认进行加密操作
// key为正字母向后移动，key为负向前移动，key值正负交替，即可模拟加密与解密过程

void CaesarsCipher(char* text, char* result, int key);

int main()
{
	// 存储输入的明文(或密文)
	char* text = (char*)malloc(sizeof(char)*char_max);
	// 存储结果
	char* result = (char*)malloc(sizeof(char)*char_max);
	// 密钥
	int key = 0;
	// 临时变量，用于清空输入区
	int c = 0;

	// 输入失败的次数，连续3次输入失败程序将自动退出
	int fail_time = 0;
	//
	printf_s("请输入明文(或密文),以回车键结束:\n");
	// 从键盘获取输入
	gets(text);
	printf_s("请输入密钥(整数):");
	// 读取密钥必须是整数
	while (scanf_s("%d", &key) != 1)
	{
		// 清空缓冲区
		while ((c = getchar()) != '\n' && c != EOF);
		fail_time++;
		if (fail_time == 3)
		{
			printf_s("连续失败达到3次，程序自动退出\n");
			system("pause");
			return 0;
		}
		printf_s("请输入整数密钥:");
	}

	CaesarsCipher(text, result, key);
	printf_s("%s\n", result);
	free(text);
	free(result);

	system("pause");

	return 0;
}

void CaesarsCipher(char* text, char* result,int key)
{
	// 记录当前位置
	int pos = 0;
	// 记录有效的值
	int vaild = 0;
	// 字母的ascii码值
	int code = 0;
	// 初始化结果数组
	memset(result, 0, char_max*sizeof(char));
	// 对关键字取模运算
	key = abs(key) % 26;
	// 遍历输入的所有字符
	while (text[pos])
	{
		// 如果是字母，进行处理
		if (isalpha(text[pos]))
		{
			// 获取字母ASCII值
			code = toupper(text[pos]);
			// 进行加密或解密操作
			code += key;
			// 判断ASCII是否越界
			if (code > 90)
				code = code - 26;
			if (code < 65)
				code = code + 26;
			result[vaild] = (char)code;
			vaild++;
		}
		// 去掉所有' ','\t','\n','\v','\r','\f'显示为空的字符
		else if (isspace(text[pos]))
		{
			pos++;
			continue;
		}
		// 其它字符原样输入
		else
		{
			result[vaild] = text[pos];
			vaild++;
		}
		pos++;
	}

	return;
}
