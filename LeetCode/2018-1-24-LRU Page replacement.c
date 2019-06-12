#include<stdio.h>
#include<stdlib.h>
#include<limits.h>
#include<string.h>
#include<time.h>
#include<stdbool.h>

void LRU_PageReplacement(int *resource, int *times,int length, int page_num);
//保持和FIFO的接口风格一致，增添了times参数，来记录上次使用的次数，因此resource里面的标识符由原来的三位变成两位

int main()
{
	int length = 4;//内存页面最大长度
	int *resource = (int *)calloc(sizeof(int), length + 2);//分配空间,0号位为标识符，1号位为此次替换的位置，2号位为下一次替换的位置
	int *times = (int*)calloc(sizeof(int), length);//分配空间，相应的位置表示已经停留在内存中的次数,此处一定要初始化为0
	int i = 0;

	for (i = 0; i < length + 2; i++)
	{
		resource[i] = -1;//初始化为-1，表示空
	}
	for (i = 0; i < length; i++)
	{
		times[i] = 0;
	}


	//------------------测试----------------------
	int list[25] = { 7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1 };
	int j = 0;
	for (i = 0; i < 20; i++)
	{
		LRU_PageReplacement(resource,times, length, list[i]);

		for (j = 0; j < length + 2; j++)
			printf_s("%d ", resource[j]);
		printf_s("	");
		for (j = 0; j < length; j++)
		{
			printf_s("%d ", times[j]);
		}
		printf_s("\n");
	}

	system("pause");
}

void LRU_PageReplacement(int *resource, int* times,int length, int page_num)//length为内存能容纳的最大长度，page_num为请求的页面
{
	int i = 0, j = 0;
	int max = 0, max_pos = 0;

	for (i = 2; i < length + 2; i++)
	{
		if (page_num == resource[i])//表示请求的页面在已经分配的内存中
		{
			resource[0] = 0;//0表示不需要请求新的页面
			resource[1] = i;//请求的页面在第i号位置
			times[i - 2] = 1;//记录请求的页面的在内存中的次数重置为1
			for (j = 0; j < length; j++)//循环遍历内存中页面的停留次数
			{
				if (times[j] == 0)//如果该位置的停留次数为0，表示该位置还从来没有被分配过页面，跳过
					continue;
				if (j == i - 2)
					continue;//分配内存对应的记录次数的位置，重置为1，表示下一次请求时，该页面已经在内存中停留了一次
				else 
					times[j] += 1;//其余位置依次增加1个停留时间
			}

			return;
		}
	}

	//请求的页面不在已分配的内存中
	max = times[0];
	for (j = 0; j < length; j++)//找到停留最久的页面在内存中的位置
	{
		if (times[j] == 0)//如果该位置还没有被分配过，则直接分配
		{
			max_pos = j;
			break;
		}
		if (times[j] > max)
		{
			max = times[j];
			max_pos = j;
		}
	}

	resource[max_pos + 2] = page_num;
	resource[0] = 1;
	resource[1] = max_pos + 2;
	times[max_pos] = 1;

	for (j = 0; j < length; j++)//循环遍历内存中页面的停留次数
	{
		if (times[j] == 0)//如果该位置的停留次数为0，表示该位置还从来没有被分配过页面，跳过
			continue;
		if (j == max_pos)
			continue;//分配内存对应的记录次数的位置，重置为1，表示下一次请求时，该页面已经在内存中停留了一次
		else
			times[j] += 1;//其余位置依次增加1个停留时间
	}

	return;
}
