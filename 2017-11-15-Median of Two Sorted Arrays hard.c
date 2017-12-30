#include<stdio.h>
#include<time.h>
#include<stdlib.h>
#include<string.h>
#include<stdbool.h>	

//There are two sorted arrays nums1 and nums2 of size m and n respectively.
//
//Find the median of the two sorted arrays.The overall run time complexity should be O(log(m + n)).
//
//Example 1:
//nums1 = [1, 3]
//nums2 = [2]
//
//The median is 2.0
//Example 2 :
//	nums1 = [1, 2]
//	nums2 = [3, 4]
//
//	The median is(2 + 3) / 2 = 2.5


double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size)
{
	int nums1_pos = 0, nums2_pos = 0;
	int medium = 0;
	int temp = 0, i = 0;
	bool isnums1_break = false, isnums2_break = false;
	bool end_with_nums1 = false, end_with_nums2 = false;
	bool isPrime = false;//是否是奇数个


	medium = (nums1Size + nums2Size) / 2;
	if ((nums1Size + nums2Size) % 2)
		isPrime = true;

	if (!nums1Size)
	{
		if (isPrime)
			return nums2[medium];
		else
			return (nums2[medium - 1] + nums2[medium]) / 2.0;
	}
	if (!nums2Size)
	{
		if (isPrime)
			return nums1[medium];
		else
			return (nums1[medium - 1] + nums1[medium]) / 2.0;
	}//处理有一个数列为空的情况

	if (isPrime)
	{
		for (i = 0; i < medium; i++)
		{
			if (nums1[nums1_pos] <= nums2[nums2_pos])
				nums1_pos++;
			else
				nums2_pos++;
			if (nums1_pos == nums1Size)
				return nums2[medium - nums1_pos];
			if (nums2_pos == nums2Size)	
				return nums1[medium - nums2_pos];
		}
		if (nums1[nums1_pos] <= nums2[nums2_pos])
			return nums1[nums1_pos];	
		else
			return nums2[nums2_pos];
	}
	else
	{
		for (i = 0; i < medium; i++)
		{
			if (nums1[nums1_pos] <= nums2[nums2_pos])
			{
				nums1_pos++;
				end_with_nums1 = true;
				end_with_nums2 = false;
			}
			else
			{
				nums2_pos++;
				end_with_nums1 = false;
				end_with_nums2 = true;
			}

			if (nums1_pos == nums1Size)
			{
				if (i + 1 == medium)
					return (nums1[nums1Size - 1] + nums2[nums2_pos]) / 2.0;
				else
					return (nums2[medium - nums1Size] + nums2[medium - nums1Size - 1]) / 2.0;
			}

			if (nums2_pos == nums2Size)
			{
				if (i + 1 == medium)
					return (nums2[nums2Size - 1] + nums1[nums1_pos]) / 2.0;
				else
					return (nums1[medium - nums2Size] + nums1[medium - nums2Size - 1]) / 2.0;
			}
		}
		if (end_with_nums1)
		{
			temp = nums1[nums1_pos] <= nums2[nums2_pos] ? nums1[nums1_pos] : nums2[nums2_pos];
			return (temp + nums1[nums1_pos - 1]) / 2.0;
		}
		if (end_with_nums2) 
		{
			temp = nums2[nums2_pos] <= nums1[nums1_pos] ? nums2[nums2_pos] : nums1[nums1_pos];
			return (temp + nums2[nums2_pos - 1]) / 2.0;
		}
	}

	return 0;
}

int main()
{
	int nums1[8] = {2}, nums2[10] = {1,3 };
	
	printf_s("%f\n", findMedianSortedArrays(nums1,1, nums2, 2));
	
	system("pause");
}
