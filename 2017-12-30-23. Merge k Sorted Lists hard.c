#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<malloc.h>
#include<limits.h>
#include<math.h>
#include<time.h>

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

struct ListNode* mergeKLists(struct ListNode** lists, int listsSize)
{
	int count = 2;
	struct ListNode* temp = NULL;

	if (listsSize == 1)
		return lists[0];
	else if (listsSize == 2)
	{
		temp = mergeTwoLists(lists[0], lists[1]);
		return temp;
	}
	else
	{
		temp = mergeTwoLists(lists[0], lists[1]);
		while (count< listsSize)
		{
			temp = mergeTwoLists(temp, lists[count]);
			count++;
		}
		return temp;
	}

}

int main()
{
	struct ListNode** l= (struct ListNode**)malloc(sizeof(struct ListNode*)*3);
	struct ListNode *l1 = (struct ListNode*)malloc(sizeof(struct ListNode));
	struct ListNode *l2 = (struct ListNode*)malloc(sizeof(struct ListNode));
	struct ListNode *l3 = (struct ListNode*)malloc(sizeof(struct ListNode));
	struct ListNode*t = NULL;
	l1->val = 2;
	l1->next = NULL;


	l3->val = -100000;
	l3->next = NULL;
	l[0] = l1;
	l[1] = NULL;
	l[2] = l3;
	t=mergeKLists(l, 3);
	printf_s("%d", t->val);
	printf_s("%d", t->next->val);

	system("pause");

	return 0;
}
