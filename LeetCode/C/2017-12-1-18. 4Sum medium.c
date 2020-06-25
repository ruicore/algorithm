#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
#include <malloc.h>
#include <limits.h>

void Insert_sort(int *nums, int numSize)
{
	int i = 0, j = 0;
	int temp = 0;

	for (i = 1; i < numSize; i++)
	{
		for (j = i; j > 0; j--)
		{
			if (nums[j] < nums[j - 1])
			{
				temp = nums[j - 1];
				nums[j - 1] = nums[j];
				nums[j] = temp;
			}
			else
			{
				break;
			}
		}
	}

	return;
}

void threeSum(int* nums, int numsSize,int start, int target,int **result,int *count)//start 是起始目标位置
{
	int left = 0, right = 0;
	int temp_target = 0;
	int i = 0, j = 0;

	for (i = start; i < numsSize; i++)
	{
		if (i != start&&nums[i] == nums[i - 1])
			continue;
		left = i + 1, right = numsSize - 1;
		temp_target = target - nums[i];
	  //printf_s("temp_target = %d target = %d nums[i]= %d", target, temp_target, nums[i]);
	  //printf_s("\n");
		while (left<right)
		{
			if (nums[left] + nums[right] < temp_target)
				left++;
			else if (nums[left] + nums[right] > temp_target)
				right--;
			else
			{
				result[(*count)] = (int*)malloc(sizeof(int) * 4);
				result[(*count)][0] = nums[start - 1];
				result[(*count)][1] = nums[i];
				result[(*count)][2] = nums[left];
				result[(*count)][3] = nums[right];
				(*count)++;
			//	printf_s("count = %d\n", *count);
				left++;
				right--;
			}
		}
	}
}
int** fourSum(int* nums, int numsSize, int target, int* returnSize) 
{
	int **result = NULL, **temp_result = NULL;
	int addres_mall = 1, count = 0, temp_count = 1, temp_target = 0;
	int left = 0, right = 0;
	int i = 0, j = 0;

	if (numsSize<4)
		return NULL;
	Insert_sort(nums, numsSize);
	/*for (i = 0; i < numsSize; i++)
		printf_s("%d ", nums[i]);
	printf_s("\n");*/
	addres_mall = numsSize*numsSize;
	temp_result = (int**)malloc(sizeof(int*)*addres_mall);
	for (i = 0; i < numsSize - 3; i++)
	{
	//	printf_s("----------------\n");
		if (i&&nums[i] == nums[i - 1])
			continue;
		threeSum(nums, numsSize, i + 1, target - nums[i], temp_result, &count);
	//	printf_s("\n");
	}
	
	if (count)
	{
		temp_count = count;
		result = (int**)malloc(sizeof(int*)*temp_count);
		result[0] = (int*)malloc(sizeof(int) * 4);
		for (i = 0; i < 4; i++)
			result[0][i] = temp_result[0][i];
		count = 0;
		for (i = 1; i < temp_count; i++)
		{
			if (temp_result[i][0] == result[count][0] && temp_result[i][1] == result[count][1] && temp_result[i][2] == result[count][2] && temp_result[i][3] == result[count][3])
				continue;
			else
			{
				count++;
				result[count] = (int*)malloc(sizeof(int) * 4);
				result[count][0] = temp_result[i][0];
				result[count][1] = temp_result[i][1];
				result[count][2] = temp_result[i][2];
				result[count][3] = temp_result[i][3];
			}
		}
		count++;
		for (i = 0; i < temp_count; i++)
			free(temp_result[i]);

	}

	*returnSize = count;
	return result;
}

int main()
	{
//int nums[60] = {-495,-477,-464,-424,-411,-409,-363,-337,-328,-328,-325,-320,-310,-285,-278,-235,-208,-151,-149,-147,-144,-132,-115,-107,-101,-98,-83,-58,-58,-56,-51,-46,-45,-7,0,4,4,21,51,52,57,60,104,109,124,141,158,205,206,241,278,278,291,314,379,416,437,447,452,496 };
	int nums[9] = { 2,0,3,0,1,2,4 };
	int numsSize = 7,target = 7;
	int n = 0, i = 0;
	int *returnSize = &n;
	int ** re = NULL;
	re= fourSum(nums, numsSize, target, returnSize);
	//printf_s("%d", *returnSize);
	for (i = 0; i < *returnSize; i++)
	{
		for (int j = 0; j < 4; j++)
			printf_s("%d ", re[i][j]);
		printf_s("\n");
	}
	system("pause");
	
	return 0;
}