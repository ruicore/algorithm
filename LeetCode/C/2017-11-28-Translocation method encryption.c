#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
#include <malloc.h>

//待加密的明文：Plain text
//密钥 ：key
//加密后的文章：Ciphertext
//加密：Encrypt
//解密：Decrypt

struct key_out //结构体，“AAA”排序为123
{
	char ch;
	int pos;
	bool flag;
};

void Free(char *str_free)
{
	char *p, *q;

	q = str_free;
	while (q)
	{
		p = q;
		q++;
		free(p);
	}
}

int *Get_order(char *key) //得到输出密钥的顺序
{
	int *key_order = NULL, key_num = 0;
	int i = 0, j = 0;
	struct key_out *key_temp = NULL, *temp = NULL;
	char *key_sort = NULL;
	char ch_temp = 'a';

	key_num = strlen(key);
	key_temp = malloc(sizeof(struct key_out) * key_num);// 需要在函数体内free
	key_sort = malloc(sizeof(char) * (key_num + 1));//需要要在函数内free
	key_order = calloc(sizeof(int), key_num);//需要在加密或解密函数内free
	temp = key_temp;
	key_sort[key_num] = NULL;

	for (i = 0; i < key_num; i++)
	{
		temp->ch = key[i];
		temp->pos = i;
		temp->flag = false;
		temp++;
		key_sort[i] = key[i];
	}

	for (i = 1; i < key_num; i++) //插入法排序
	{
		for (j = i; j > 0; j--)
		{
			if (key_sort[j] < key_sort[j - 1])
			{
				ch_temp = key_sort[j - 1];
				key_sort[j - 1] = key_sort[j];
				key_sort[j] = ch_temp;
			}
			else
				break;
		}
	}

	for (i = 0; i < key_num; i++)
	{
		temp = key_temp;
		while (key_sort[i] != (temp->ch))
		{
			temp++;
		}
		while (temp->flag)
		{
			temp++;
		}
		key_order[i] = temp->pos;
		temp->flag = true;
	}


	return key_order;
}

char *Encrypt(char *plain_text, char *key) //加密函数
{
	char *Ciphertext = NULL;
	int plain_text_num = 0, key_num = 0;
	int *key_order = NULL;
	int i = 0, j = 0, temp = 0;

	plain_text_num = strlen(plain_text), key_num = strlen(key);
	Ciphertext = malloc(sizeof(char) * (plain_text_num + 1));// 需要在主调函数内free
	Ciphertext[plain_text_num] = NULL;//// 

	key_order = Get_order(key);
	for (i = 0; i < key_num; i++)
	{
		j = key_order[i];
		while (j < plain_text_num)
		{
			Ciphertext[temp] = plain_text[j];
			j += key_num;
			temp++;
		}
	}

	return Ciphertext;
}

int main()
{
	char *key = "AAAA";
	char *plain = "thisisthenewquestion";

	printf_s("%s\n", Decrypt("tieqthsnuiiteeoshwsn", key));

	system("pause");
	return 0;
}
