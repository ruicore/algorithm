#include<stdio.h>
#include<malloc.h>
#include<stdlib.h>
// Definition for singly - linked list.

struct ListNode {
	int val;
	struct ListNode *next;

};

int Get_length(struct ListNode *head)
{
	int count = 0;

	while (head)
	{
		count++;
		head = head->next;
	}

	return count;
}

void reverse(struct ListNode* start, struct ListNode* end, int num)
{
	struct ListNode* head = NULL, *temp = NULL, *temp_head = NULL, *isolate = NULL;
	int i = 0;

	temp_head = start->next;
	temp = head = start;
	head->next = NULL;

	for (i = 0; i < num - 1; i++)
	{
		temp = temp_head;
		temp_head = temp_head->next;
		isolate = head;
		head = temp;
		head->next = isolate;
	}

	return;
}

struct ListNode* reverseKGroup(struct ListNode* head, int k)
{
	struct ListNode *start = NULL, *end = NULL, *Head = NULL, *hold = NULL, *tail = NULL;
	int length = 0, times = 0;
	int i = 0, j = 0;

	length = Get_length(head);
	times = length / k;

	if (!times)
		return head;
	if (k == 1)
		return head;
	else
	{
		tail = hold = end = start = head;

		for (j = 0; j < times; j++)
		{
			for (i = 0; i < k - 1; i++)
				end = end->next;
			hold = end->next;
			reverse(start, end, k);
			if (j == 0)
			{
				Head = end;
				start = end = hold;
			}
			else
			{
				tail->next = end;
				tail = start;
				start = end = hold;
			}
		}
	}

	tail->next = hold;

	return Head;

}
