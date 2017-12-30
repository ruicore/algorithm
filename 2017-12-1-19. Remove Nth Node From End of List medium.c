#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
#include <malloc.h>
#include <limits.h>

/*19. Remove Nth Node From End of List
Given a linked list, remove the nth node from the end of list and return its head.

For example,

Given linked list : 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note :
	Given n will always be valid.
	Try to do this in one pass*/

// Definition for singly-linked list.

struct ListNode {
	int val;
	struct ListNode *next;
};
	
struct ListNode* removeNthFromEnd(struct ListNode* head, int n)
{
	struct ListNode *faster = NULL, *slower = NULL, *temp = NULL;
	int i = 0;
	faster = head, slower = head, temp = head;

	for (i = 0; i < n; i++)
		faster = faster->next;
	if (faster == NULL)
		return head->next;
	while (faster->next)
	{
		faster = faster->next;
		slower = slower->next;
	}
	
	temp = slower->next;
	slower->next = temp->next;
	free(temp);

	return head;
}

int main()
	{

	system("pause");
	
	return 0;
}