# -*- coding: utf-8 -*-
# @Author:             何睿
# @Create Date:        2019-01-07 22:11:59
# @Last Modified by:   何睿
# @Last Modified time: 2019-01-08 17:17:50


class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        remain, i, gasnum = 0, 0, len(gas)
        while i < gasnum:
            # 如果当前汽车站的汽油小于需要消耗的汽油，则继续往后走
            if gas[i] < cost[i]:
                i += 1
            else:
                # 当前位置往下一个剩下的汽油
                remain = gas[i]-cost[i]
                # j表示下一位置
                j = (i+1) % gasnum
                # 只要汽油还有剩余，则继续往下走
                while remain+gas[j]-cost[j] >= 0:
                    remain += gas[j]-cost[j]
                    j = (j+1) % gasnum
                    # 如果再次走回到了i则返回
                    if j == i:
                        return i
                # 否则继续从刚才停下的位置继续往后寻找
                if j > i:
                    i = j
                else:
                    i += 1
        return -1


if __name__ == "__main__":
    so = Solution()
    res = so.canCompleteCircuit([3, 3, 4], [3, 4, 4])
    print(res)
