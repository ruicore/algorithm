#define _CRT_SECURE_NO_WARNINGS //去掉vs安全检查
#include<stdio.h>
#include<stdlib.h>
#include<limits.h>
#include<string.h>
#include<time.h>

#define SIZE 1000

typedef struct Node
{
	char *word;
	int times;
	struct Node *next;
}data;

int hash(char* word)//根据word计算得到一个随机值，这个值的范围在[0,SIZE)之间
{
	int i = 0, h = 0;
	for (i = 0; word[i];i++)
	{
		h = (h * 31 + word[i] ) % SIZE;
	}

	return h;
}

int InsertMap(data**map, char *word, int lenw)
{
	int h = hash(word);//计算得到一个随机值，次随机值就是数组的下标

	if (map[h] == NULL)
	{
		map[h] = (data*)malloc(sizeof(data));
		map[h]->word = (char*)malloc(sizeof(char)*(lenw + 1));
		map[h]->times = 1;
		strcpy(map[h]->word, word);
		map[h]->next = NULL;
		return 1;//当前位置只有一个word
	}
	else
	{
		data*p = map[h];
		while (p->next)
		{
			if (strcmp(p->word, word) == 0)
			{
				p->times++;
				return p->times;//返回次数
			}
			p = p->next;
		}
		if (strcmp(p->word, word) == 0)
		{
			p->times++;
			return p->times;
		}
		else
		{
			data *tmp = (data*)malloc(sizeof(data));
			tmp->word = (char*)malloc(sizeof(char)*(lenw + 1));
			tmp->times++;
			strcpy(tmp->word, word);
			tmp->next = NULL;
			p->next = tmp;
			return 1;
		}
		
	}
}

int FindMap(data**map, char* sub)
{
	int h = hash(sub);
	if (map[h] == NULL)
	{
		return -1;
	}
	else
	{
		data*p = map[h];
		while (p!=NULL)
		{
			if (strcmp(p->word, sub) == 0)
			{
				return p->times;
			}
			p = p->next;
		}
		return -1;
	}
}
char *substring(char *s, int start, int len)
{
	char *sub = (char*)malloc(sizeof(char)*(len + 1));
	int i = 0;

	for (; i < len; i++)
	{
		sub[i] = s[i + start];
	}
	sub[i] = 0;
	return sub;
}

int *findSubstring(char *s, char **words, int wordSize, int* returnSize)
{
	int lenw = strlen(words[0]), lens = strlen(s), length = wordSize;
	int *res = (int*)malloc(sizeof(int)*(lens - lenw * length + 1));
	data** map = (data**)malloc(sizeof(data*)*SIZE);
	data** tmp = (data**)malloc(sizeof(data*)*SIZE);
	int i = 0, j = 0;

	for (i = 0; i < SIZE; i++)
	{
		map[i] = NULL;
		tmp[i] = NULL;
	}
	for (i = 0; i < length; i++)
	{
		InsertMap(map, words[i], lenw);
	}
	*returnSize = 0;
	for (i = 0; i < lens - lenw * length + 1; i++)
	{
		for (j = 0; j < SIZE; j++)
		{
			if (tmp[j] != NULL)
			{
				free(tmp[j]);
				tmp[j] = NULL;
			}
		}
		for (j = 0; j < length; j++)
		{
			char *sub = substring(s, i + j * lenw, lenw);
			int  mapnum = FindMap(map, sub);
			if (mapnum == -1)
				break;
			int num = InsertMap(tmp, sub, lenw);
			if (mapnum < num)
				break;
			free(sub);
		}
		if (j >= length)
			res[(*returnSize)++] = i;
	}
	for (i = 0; i < SIZE; i++)
	{
		if (map[i] != NULL)
			free(map[i]);
	}
	free(map);

	return res;
}
int main()
{
	char a[100] = { '1','2','\0' };
	char b[3] = { '3','4','\0' };
	printf("%s", strcpy(a, b));
	system("pause");
}

