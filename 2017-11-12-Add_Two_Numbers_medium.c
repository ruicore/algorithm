#include<stdio.h>
#include<time.h>
#include<stdlib.h>
#include<string.h>
#include<stdbool.h>	


////
//You are given two non - empty linked lists representing two non - negative integers.The digits are stored in reverse order and each of their nodes contain a single digit.Add the two numbers and return it as a linked list.
//
//You may assume the two numbers do not contain any leading zero, except the number 0 itself.
//
//Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
//	Output : 7 -> 0 -> 8
// Definition for singly-linked list.

 struct ListNode {
     int val;
     struct ListNode *next;
 };

int GetLength(struct ListNode* mylist)
{
	int count = 0;
	do
	{
		count++;
		mylist = mylist->next;
	} while (mylist);

	return	count;
}

struct ListNode* Equal(struct ListNode* l1, struct ListNode* l2,int Length)
{
	int i = 0, j = 0, flag_move = 0, temp_num = 0;
	struct ListNode* head = NULL;
	struct ListNode* temp = NULL;

	head = (struct ListNode*)malloc(sizeof(struct ListNode));
	temp = head;
	for (i = 0; i < Length - 1; i++)
	{
		temp_num = l1->val + l2->val + flag_move;
		if (temp_num / 10)
		{
			temp->val = temp_num % 10;
			flag_move = 1;

		}
		else
		{
			temp->val = temp_num;
			flag_move = 0;
		}
		temp->next = (struct ListNode*)malloc(sizeof(struct ListNode));
		temp = temp->next;
		l1 = l1->next;
		l2 = l2->next;
	}
	temp_num = l1->val + l2->val + flag_move;
	if (temp_num / 10)
	{
		temp->val = temp_num % 10;
		flag_move = 1;
		temp->next = (struct ListNode*)malloc(sizeof(struct ListNode));
		temp = temp->next;
		temp->val = 1;
		temp->next = NULL;

	}
	else
	{
		temp->val = temp_num;
		flag_move = 0;
		temp->next = NULL;
	}

	return head;
}

void  Coda(struct ListNode* coda_result, struct ListNode* coda_leave,int Length)
{
	int i = 0, j = 0, temp_num = 0, flag_move = 0;

	flag_move = coda_result->val;
	for (i = 0; i < Length - 1; i++)
	{
		temp_num = flag_move + coda_leave->val;
		if (temp_num / 10)
		{
			coda_result->val = temp_num % 10;
			flag_move = 1;
		}
		else
		{
			coda_result->val = temp_num;
			flag_move = 0;
		}
		coda_result->next= (struct ListNode*)malloc(sizeof(struct ListNode));
		coda_result = coda_result->next;
		coda_leave = coda_leave->next;
	}
	temp_num = flag_move + coda_leave->val;
	if (temp_num / 10)
	{
		coda_result->val = temp_num % 10;
		flag_move = 1;
		coda_result->next= (struct ListNode*)malloc(sizeof(struct ListNode));
		coda_result = coda_result->next;
		coda_result->val = 1;
		coda_result->next = NULL;
	}
	else
	{
		coda_result->val = temp_num;
		flag_move = 0;
		coda_result->next = NULL;
	}

	return;
}

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2)
{
	int length_one = GetLength(l1);
	int i = 0, j = 0;
	int length_two = GetLength(l2);
	struct ListNode* head = NULL;
	struct ListNode* temp = NULL;
	struct ListNode* long_list = NULL;

	//printf_s("length_one = %d length_two =%d", length_one, length_two);

	head = (struct ListNode*)malloc(sizeof(struct ListNode));

	if (length_one == length_two)
	{
		head = Equal(l1, l2, length_one);
		return head;
	}
	if (length_one > length_two)
	{
		head = Equal(l1, l2, length_two);
		temp = head;
		long_list = l1;
		for (i = 0; i < length_two-1; i++)
		{
			temp = temp->next;
			long_list = long_list->next;
		}
		if (!temp->next)
		{
			temp->next = (struct ListNode*)malloc(sizeof(struct ListNode));
			temp = temp->next;
			temp->val = 0;
		}
		else
		{
			temp = temp->next;
		}
		long_list = long_list->next;
		Coda(temp, long_list, length_one - length_two);	
	}

	if (length_two> length_one)
	{
		head = Equal(l1, l2, length_one);
		temp = head;
		long_list = l2;
		for (i = 0; i < length_one-1; i++)
		{
			temp = temp->next;
			long_list = long_list->next;
		}
		if (!temp->next)
		{
			temp->next = (struct ListNode*)malloc(sizeof(struct ListNode));
			temp = temp->next;
			temp->val = 0;
		}
		else
			temp = temp->next;
		long_list = long_list->next;
		Coda(temp, long_list, length_two - length_one);

	}

	return  head;
}

int main()
{
	struct ListNode * list_one;
	struct ListNode * list_two;
	struct ListNode * list_result;

	list_one = (struct ListNode*)malloc(sizeof(struct ListNode));
	list_one->val = 0;
	list_one->next = NULL;
	
	list_two = (struct ListNode*)malloc(sizeof(struct ListNode));
	list_two->val = 7;
	list_two->next = (struct ListNode*)malloc(sizeof(struct ListNode));
	list_two->next->next = NULL;
	list_two->next->val = 3;
	
	list_result=addTwoNumbers(list_one, list_two);
	printf_s("---%d", list_result->val);
	printf_s("%d", list_result->next->val);
	system("pause");
}
