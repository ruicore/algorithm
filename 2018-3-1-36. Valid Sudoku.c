#define _CRT_SECURE_NO_WARNINGS 
#include<stdio.h>
#include<stdlib.h>
#include<limits.h>
#include<string.h>
#include<time.h>
#include<stdbool.h>


bool isValidSudoku(char** board, int boardRowSize, int boardColSize) 
{
	int map[10], i = 0, j = 0, row = 0, col = 0, row_start = 0, col_start = 0, num = 0;
	
	if (boardRowSize != 9 | boardColSize != 9)return false;

	for (i = 0; i < 9; i++)
	{
		memset(map, 0, sizeof(map));
		for (j = 0; j < 9; j++)
		{
			if (board[i][j] == '.')
				continue;
			if (board[i][j]<'0' || board[i][j]>'9')
				return false;
			num = board[i][j] - '0';//所求得的值刚好再1~9
			if (map[num] != 0)return false;
			map[num] = 1;
		}
	}

	for (i = 0; i < 9; i++)
	{
		memset(map, 0, sizeof(map));
		for (j = 0; j < 9; j++)
		{
			if (board[j][i] == '.')
				continue;
			if (board[j][i]<'0' || board[j][i]>'9')
				return false;
			num = board[j][i] - '0';
			if (map[num] != 0)
				return false;
			map[num] = 1;
		}
	}
	for (i = 0; i < 9; i += 3)
	{
		for (j = 0; j < 9; j += 3)
		{
			memset(map, 0, sizeof(map));
			row_start = j;
			col_start = i;
			for (row = row_start; row < row_start + 3; row++)
			{
				for (col = col_start; col < col_start + 3; col++)
				{
					if (board[row][col] == '.')
						continue;
					if (board[row][col]<'0' || board[row][col]>'9')
						return false;
					num = board[row][col] - '0';
					if (map[num] != 0)
						return false;
					map[num] = 1;
				}
			}
		}
	}

	return true;
}