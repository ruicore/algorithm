# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-10 18:12:23
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-10 18:16:58


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype
        """
        # 如果没有节点或者只有一个节点，返回False
        if head == None or head.next == None:
            return False
        # 声明两个指针，slow指针每次走一步，fast指针每次走两步
        slow, fast = head, head.next
        while slow != fast:
            # 如果走到了末尾，返回False
            if fast == None or fast.next == None:
                return False
            # slow向后走一步
            slow = slow.next
            # fast向后走两步
            fast = fast.next.next

        return True
