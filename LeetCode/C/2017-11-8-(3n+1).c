#include<stdio.h>
#include<time.h>
#include<stdlib.h>

#define range_max 1000
#define times 3

//运行环境 Visual studio

int  judge(int guess)
{
	int count = 0;
	
	if (!(guess - 1))
	{
		printf_s("%d", 1);
		return count;
	}

	do
	{
		if (guess % 2)//如果是基数
		{
			guess = (times*guess + 1) / 2;
			count++;
		}
		else
		{
			guess = guess / 2;
			count++;
		}
	} while (guess - 1);

	return count;
}

int main()
{
	int seed = clock()*clock()*clock()*time(NULL);
	int test_times = 100;
	int rand_num_max = 1000, rand_num_min = 2, test_num = 0;
	int i = 0;
	srand(seed);

	for (i = 0; i < test_times; i++)
	{
		test_num = rand() % (rand_num_max - rand_num_min + 1) + rand_num_min;
		printf_s("%d===%d times\n", test_num, judge(test_num));
	}

	system("pause");
}
