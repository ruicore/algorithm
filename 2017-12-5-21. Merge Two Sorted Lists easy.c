#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
#include <malloc.h>
#include <limits.h>

//Merge two sorted linked lists and return it as a new list.The new list should be made by splicing together the nodes of the first two lists.
//
//Example:
//
//Input: 1->2->4, 1->3->4
//Output : 1->1->2->3->4->4

/**
* Definition for singly-linked list.
* struct ListNode {
*     int val;
*     struct ListNode *next;
* };
*/

struct ListNode {
	int val;
	struct ListNode *next;
};

struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2)
{
	struct ListNode *head = NULL, *prev = NULL;
	struct ListNode *temp_l1 = l1, *temp_l2 = l2;

	if (!l1)return l2;
	if (!l2)return l1;

	head = prev = (struct ListNode*)malloc(sizeof(struct ListNode));
	while (temp_l1&&temp_l2)
	{
		if (temp_l1->val < temp_l2->val)
		{
			prev->next = temp_l1;
			prev = temp_l1;
			temp_l1 = temp_l1->next;
		}
		else
		{
			prev->next = temp_l2;
			prev = temp_l2;
			temp_l2 = temp_l2->next;
		}
	}
	if (!temp_l1)
	{
		prev->next = temp_l2;
	}
	else
		prev->next = temp_l1;

	prev = head->next;
	free(head);

	return prev;
}

int main()
	{
	struct ListNode *l1 = (struct ListNode*)malloc(sizeof(struct ListNode));
	struct ListNode *l2 = (struct ListNode*)malloc(sizeof(struct ListNode));
	
	l1->val = 1;
	l1->next = (struct ListNode*)malloc(sizeof(struct ListNode));
	l1->next->val = 2;
	l1->next->next = (struct ListNode*)malloc(sizeof(struct ListNode));;
	l1->next->next->val = 4;
	l1->next->next->next = NULL;



	system("pause");
	
	return 0;
}