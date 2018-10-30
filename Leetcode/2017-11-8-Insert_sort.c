#include<stdio.h>
#include<time.h>
#include<stdlib.h>

void Insert_sort(int *list,int list_num)
{
	int count = 0;
	int temp = 0;
	int i = 0, j = 0;

	for(i=1;i<list_num;i++)
		for (j = i; j >0; j--)
		{
			if (list[j] > list[j - 1])
			{
				temp = list[j];
				list[j] = list[j - 1];
				list[j - 1] = temp;
				continue;
			}
			count++;
			break;
		}

	printf_s("%d\n", count);
}

//主调函数调用
// int main()
// {
// 	int length = 1000000, i = 0;
// 	int range_max = 100, range_min = 10;
// 	int seed = 0;
// 	int t1 = 0, t2 = 0;
// 	t1 = clock();

// 	int *sort_list = (int *)calloc(sizeof(int), length);
// 	seed = clock()*clock()*clock()*clock()*clock()*time(NULL);
// 	srand(seed);

// 	for (int j = 0; j < 1; j++)
// 	{
// 		for (i = 0; i < length; i++)
// 			sort_list[i] = rand() % (range_max - range_min + 1) + range_min;
// 		Insert_sort(sort_list, length);
// 	}
// 	t2 = clock();

// 	printf_s("%d---------------",(t2-t1)/1000);

// 	system("pause");
// }
