#include<stdio.h>
#include<malloc.h>


// Definition for singly - linked list.

struct ListNode {
	int val;
	struct ListNode *next;
	
};

struct ListNode* swapPairs(struct ListNode* head)
{
	if (!head || !head->next)
		return head;
	
	struct ListNode *temp = head->next;
	head->next = swapPairs(temp->next);
	temp->next = head;

	return temp;
}