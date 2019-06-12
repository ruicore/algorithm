# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-04-07 10:43:47
# @Last Modified by:   何睿
# @Last Modified time: 2019-04-07 11:00:22


class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.recursion(root))

    def recursion(self, root):
        # result[0] 表示偷当前的房子，result[1] 表示不偷当前的房子
        if not root: return [0, 0]
        result = [0, 0]
        left = self.recursion(root.left)
        right = self.recursion(root.right)
        # 偷当前的房子 ：result[0] ：当前节点的值+ 左右子树中不偷子树根节点房子的最大值
        result[0] = root.val + left[1] + right[1]
        # 不偷当前的房子：result[1] 那么左右子树的根节点偷不偷都可以，选最大值
        result[1] = max(left[0], left[1]) + max(right[0], right[1])
        return result