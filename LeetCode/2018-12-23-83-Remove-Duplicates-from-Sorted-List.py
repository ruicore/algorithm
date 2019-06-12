# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2018-12-23 21:18:30
# @Last Modified by:   何睿
# @Last Modified time: 2018-12-23 21:19:39

class Solution:
    def deleteDuplicates(self, head):
        if head == None or head.next == None:
            return head
        p = head
        while p.next:
            # 如果相等则删除
            if p.val == p.next.val:
                p.next = p.next.next
            else:
                # 否则p指向下一个元素
                p = p.next
        return head