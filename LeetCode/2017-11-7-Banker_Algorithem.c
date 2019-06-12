#include<stdlib.h>
#include<stdio.h>
#include<time.h>
#include<malloc.h>
#include<stdbool.h>

//数据结构
typedef 
struct MyStruct
{
	int* Allocated;
	int* MaxNeed;
	int* StillRequest;
	bool search;
} Process;

#define Max 17 //已分配资源最大上限
#define Min 3 //已分配资源下限
#define times_one  1.7 //最大需求资源与已分配资源比例
#define times_two 1.2 //系统总资源与最大资源比例

Process* Pro;
int* Sysava;
int* secure_sequence;	
int SUM[3];


void GetDataReady(int ProcessNum,int SourceNum)//进程资源初始化，包括初始已分配资源，最大需要资源，还需资源，系统资源
{
	int i = 0, j = 0, temper = 0;
	int seed = 0;
	int temp = 0;
	int sum = 0;
	seed = clock()*clock()*clock()*clock()*time(NULL);
	srand(seed);

	Pro = (Process*)malloc(sizeof(Process)*ProcessNum);
	Sysava = (int*)calloc(sizeof(int), SourceNum);
	secure_sequence = (int *)malloc(sizeof(int)*ProcessNum);

	for (i=0; i < ProcessNum; i++)
	{
		Pro[i].search = true;
		Pro[i].Allocated = (int *)calloc(sizeof(int),SourceNum);
		Pro[i].MaxNeed = (int *)calloc(sizeof(int),SourceNum);
		Pro[i].StillRequest = (int *)calloc(sizeof(int),SourceNum);
		for (j = 0; j < SourceNum; j++)
		{
			temp = rand() % (Max - Min + 1) + Min;
			Pro[i].Allocated[j] = temp;
		//	printf_s("%d ", temp);
			temp = rand() % (int)(Max*times_one - temp + 1) +temp;
			Pro[i].MaxNeed[j] = temp;
			Pro[i].StillRequest[j] = Pro[i].MaxNeed[j] - Pro[i].Allocated[j] + 3;
		}	
	//	printf_s("\n");
	}
	for (i = 0; i < SourceNum; i++)
	{	
		j = 0;
		temp = Pro[j].MaxNeed[0] - Pro[j].Allocated[0];
		for (; j < ProcessNum; j++)
		{
			sum += Pro[j].Allocated[i];
			if (Pro[j].MaxNeed[i] - Pro[j].Allocated[i] < temp)
				temp = Pro[j].MaxNeed[i] - Pro[j].Allocated[i];
		}
		temper = rand() % (int)(times_two * (sum + temp ) - (sum + temp) + 1) + ((sum + temp));
		Sysava[i] = temper;
		Sysava[i] = Sysava[i] - sum;
		SUM[i] = sum;
		temp = 0;
		temper = 0;
		sum = 0;
	}

	
	/*for (i = 0; i < SourceNum; i++)
	{
		printf_s("%2d ", Sysava[i]);
		
	}
	printf_s("\n");*/
}

int SouceCheck(int *request,int SourceNum)
{
	int i = 0;
	for (i=0; i < SourceNum; i++)
	{
		//printf_s("request[SourceNum]=%d", request[SourceNum]);
		if (request[i] > Pro[request[SourceNum]].StillRequest[i])
		{
		//	printf_s("资源请求判断===%d====", Pro[request[SourceNum]].StillRequest[i]);
			printf_s("资源请求不合法\n");
			return 0;
		}
	}

	return 1;
}
int  Solve(int *request, int ProcessNum, int SourceNum)//解决问题
{
	int i = 0, j = 0, m = 0, k = 0;
	int solvenum = 0,circle=0;
	bool flag = false;

	secure_sequence = (int *)calloc(sizeof(int), ProcessNum);
	int* temp = (int*)calloc(sizeof(int), ProcessNum);//结果序列，临时存储
	int* systemp = (int*)calloc(sizeof(int), SourceNum);//系统资源状态

	for (i = 0; i < ProcessNum; i++)
	{
		for (j = 0; j < SourceNum; j++)
		{
			printf_s("%2d ", Pro[i].Allocated[j]);
		}
		printf_s("---------------");
		for (j = 0; j < SourceNum; j++)
		{
			printf_s("%2d ", Pro[i].MaxNeed[j]);
		}
		printf_s("--------------");
		for (j = 0; j < SourceNum; j++)
		{
			printf_s("%2d ", Pro[i].StillRequest[j]);
		}
		printf_s("\n");
	}
	
	for (i = 0; i < SourceNum; i++)
	{
		printf_s("%2d ", Sysava[i]);
		systemp[i] = Sysava[i];
	}
	

	printf_s("\n");
	for (m = 0; m < ProcessNum; m++)
	{
		if (!Pro[m].search)
			continue;
		for (i = 0; i < SourceNum; i++)
		{
			if (Pro[m].StillRequest[i] > systemp[i])
			{
				flag = true;
				break;
			}
				
		}
		if (flag)
		{
			flag = false;
			continue;
		}

		secure_sequence[solvenum] = m;
	//	printf_s("m== %d", m);
		solvenum += 1;
		for (i = 0; i < SourceNum; i++)
		{
			systemp[i] += Pro[m].Allocated[i];
			Pro[m].StillRequest[i] = 0;
		}	

		Pro[m].search = false;
		m = -1;		
	}

	if (solvenum == ProcessNum)
		return 1;
	else
	{
		return 0;
	}

	for (m = 0; m < SourceNum; m++)
	{
		if (Sysava[m] < 0) return 0;
	}


	//
}

void Show(int Processnum)//
{
	int i = 0;
	printf_s("\n");
	for (; i < Processnum - 1; i++)
		printf_s("%d------>", secure_sequence[i]+1);
	printf_s("%d", secure_sequence[Processnum-1]+1);
}

int main()
{
	int p_num = 5, s_num = 4;
	int *request = (int *)calloc(sizeof(int), s_num + 1);

	request[0] = 2;
	request[1] = 4;
	request[2] = 3;//表示请求的三种资源对应的个数
	request[3] = 1;//表示编号为2（第三个资源）发出了请求
	request[4] = 2;

	/*GetDataReady(p_num, s_num);
	while (!SouceCheck(request, s_num))
	{
		GetDataReady(p_num, s_num);
	}
*/

	do
	{
		GetDataReady(p_num, s_num);
		while (!SouceCheck(request, s_num))
		{
			GetDataReady(p_num, s_num);
		}
	} while (!Solve(request, p_num, s_num));
	
	Show(p_num);

	scanf_s(" ");
}