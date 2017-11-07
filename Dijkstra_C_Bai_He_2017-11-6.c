#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <malloc.h>
#include <time.h>
//
//
////算法初始化，计算可用资源量available和还需要的资源量need
//void resourceInit(int *available, int *max, int *allocation, int *need);
//
////资源请求合法性检查，检查此次申请的数量是否合法，即本次分配之后，占有资源量是否超出声明量，返回值为0时代表不合法
//int requestInspect();
//
////资源分配检查，检查剩余资源是否满足此次申请的数量，返回值为0时代表无法满足要求
//int resourceInspect();
//
////获得解决方案（安全序列），返回值为0时代表找不到安全序列，即不安全
//int getSolution(int *available, int *max, int *allocation, int *need, int *request, int *secured_sequence, int p_num, int r_num);
//
////拷贝两个指定大小的int形指针的内容，第一个拷贝给第二个
//void copyIntPointer(int *a, int *b, int size);
//
////释放全部指针
//void freePointer();

void Create(int range_max, int range_min, float times_one, float times_two, int p_num, int r_num, int *allocation, int *max, int *available) //range_max 已分配资源上限, int range_min 已分配资源下限,float times_one ,float times_two
{
	int seed = 0;
	seed = clock()*clock()*clock()*clock()*time(NULL);
	srand(seed);
	int i = 0, j = 0, temp = 0, tempmin = 0, sum = 0;
	for (; i < p_num*r_num; i++)
	{
		temp = rand() % (range_max - range_min + 1) + range_min;
		allocation[i] = temp;
		//printf_s("%d ", temp);
	}
	printf_s("\n");
	for (i = 0; i < p_num*r_num; i++)
	{
		temp = rand() % (int)(range_max*times_one - allocation[i] + 1) + allocation[i];
		max[i] = temp;
		//printf_s("%d ", temp);
	}
	tempmin = max[0] - allocation[0];
	////printf_s("\n");
	for (i = 0; i < r_num; i++)
	{
		for (j = 0; j < p_num; j++)
		{
			sum += allocation[j*r_num + i];
		}
		for (j = 0; j < p_num; j++)
		{
			if (max[j*r_num + i] - allocation[j*r_num + i] < tempmin)
				tempmin = max[j*r_num + i] - allocation[j*r_num + i];
		}

		temp = rand() % (int)(times_two * (sum+tempmin)- (sum + tempmin) + 1) + ((sum + tempmin));
		max[i] = temp;
		sum = 0;
		tempmin = 0;
	}

	///*for (i = 0; i < r_num; i++)
	//{
	//	printf_s("%d ", max[i]);
	//}*/
}

int main()
{
	int *available;//剩余资源向量
	int *max;//最大所需资源矩阵
	int *allocation;//已分配资源矩阵
					//	int *need;//剩余需求矩阵
					//	int *request;//新请求资源向量，最后一个值为request对应的进程号（从0开始）
					//	int *secured_sequence;//安全序列向量，全部初始化为-1
					//	int p_num;//进程数量向量
					//	int r_num;//资源种类向量
	allocation = (int *)malloc(sizeof(int) * 12);
	max = (int *)malloc(sizeof(int) * 12);
	available = (int *)malloc(sizeof(int) * 3);
	Create(15, 5, 1.5, 1.2, 4, 3, allocation, max, available);
	scanf_s(" ");
}



//int getSolution(int *available, int *max, int *allocation, int *need, int *request, int *secured_sequence, int p_num, int r_num)
//{
//	int i, j, m;
//	int flag;
//
//	int finish = (int *)calloc(p_num, sizeof(int));
//
//	int *work = (int *)calloc(r_num, sizeof(int));
//	int *allo = (int *)calloc(p_num*r_num, sizeof(int));
//	int *ned = (int *)calloc(p_num*r_num, sizeof(int));
//
//	copyIntPointer(available, work, r_num);
//	copyIntPointer(allocation, allo, p_num*r_num);
//	copyIntPointer(need, ned, p_num*r_num);
//
//	for (i = 0; i<r_num; i++)//预分配，计算这次资源请求后，系统资源情况
//	{
//		work[i] = work[i] - request[i];
//		allo[request[r_num]][i] = allo[request[r_num]][i] + request[i];
//		ned[request[r_num]][i] = ned[request[r_num]][i] - request[i];
//	}
//	//while (secured_sequence[p_num-1] == 0)
//	for (m = 0; m<p_num; m++)
//	{
//		for (j = 0; j<p_num; j++)
//		{
//			flag = 1;
//			if (finish[j] == 0)
//			{
//				for (i = 0; i<r_num; i++)
//				{
//					if (ned[j][i] > work[i])
//					{
//						flag = 0;
//						break;
//					}
//				}
//				if (flag == 1)
//				{
//					secured_sequence[m] = j;
//					break;
//				}
//				else
//				{
//					continue;
//				}
//			}
//			else
//			{
//				continue;
//			}
//		}
//		if (secured_sequence[m] == -1)
//		{
//			return 0;//无法找到安全序列，返回false
//		}
//	}
//	return 1;//找到安全序列，返回true；安全序列储存在secured_sequence中
//}
