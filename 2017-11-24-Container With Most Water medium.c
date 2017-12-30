//11. Container With Most Water

int maxArea(int* height, int heightSize) 
{
	int result_max = 0, temp_max = 0;
	int left = 0, right = heightSize - 1;

	while (left<right)
	{
		if (height[left] < height[right])
		{
			temp_max = (right - left)*height[left];
			left++;
		}
		else
		{
			temp_max = (right - left)*height[right];
			right--;
		}
		if (temp_max > result_max)
			result_max = temp_max;
			
	}

	return result_max;
}