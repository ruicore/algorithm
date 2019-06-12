#include<stdio.h>
#include<malloc.h>
#include<stdlib.h>

void FIFO_PageReplacement(int *resource, int length, int page_num);

int main()
{
	int length = 4;//内存页面最大长度
	int *resource = (int *)calloc(sizeof(int),length);//分配空间
	int i = 0;

	for (i = 0; i < length; i++)
	{
		resource[i] = -1;//初始化为-1，表示空
	}


	//------------------测试----------------------
	int list[10] = { 0,4,7,4,8,6,7,2,0,4 };
	int j = 0;
	for (i = 0; i < 10; i++)
	{
		FIFO_PageReplacement(resource, 4, list[i]);
		
		for (j = 0; j < 4; j++)
			printf_s("%d ", resource[j]);
		printf_s("\n");
	}

	system("pause");
}

void FIFO_PageReplacement(int *resource,int length,int page_num)//length为内存能容纳的最大长度，page_num为请求的页面
{
	int i = 0, temp = 0;

	for (i = 0; i < length; i++)//判断是否还有空的位置，如果有，则将请求的页面放入空的位置，返回
	{
		if (resource[i] == -1)
		{
			resource[i] = page_num;
			return;
		}		
	}
	
	for (i = 0; i < length; i++)//执行到这里表示没有空的页面，判断请求的页面在已分配的页面中是否已经存在，若存在，则直接返回
	{
		if (resource[i] == page_num)
			return;
	}

	for (i = 1; i < length; i++)//执行到这里表示没有空的页面，且请求的页面没有在已分配的页面中，则从前往后依次替换一个页面，把请求的页面放到最后一个位置
	{
		resource[i - 1] = resource[i];
	}
	resource[length-1] = page_num;
}