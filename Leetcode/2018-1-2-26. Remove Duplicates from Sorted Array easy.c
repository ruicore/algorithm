
// Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.

// Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

// Example:

// Given nums = [1,1,2],

// Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
// It doesn't matter what you leave beyond the new length.

int removeDuplicates(int* nums, int numsSize)
{
	int index = 0, i = 0;
	if (!numsSize)
		return index;

	index = 1;
	for (i = 1; i < numsSize; i++)
	{
		if (nums[i] != nums[i - 1])
		{
			nums[index] = nums[i];
			index++;
		}
	}

	return index;
}