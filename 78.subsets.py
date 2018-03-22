#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (44.36%)
# Total Accepted:    224.8K
# Total Submissions: 506K
# Testcase Example:  '[1,2,3]'
#
# 
# Given a set of distinct integers, nums, return all possible subsets (the
# power set).
# 
# Note: The solution set must not contain duplicate subsets.
# 
# 
# For example,
# If nums = [1,2,3], a solution is:
# 
# 
# 
# [
# ⁠ [3],
# ⁠ [1],
# ⁠ [2],
# ⁠ [1,2,3],
# ⁠ [1,3],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ []
# ]
# 
#
import copy
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        cur = []
        result = []
        self.insert_data(cur, result, nums, 0)
        return result


    def insert_data(self, cur, result, nums, index):
        #确定返回条件
        # c_cur = ''.join([str(val) for val in sorted(cur)])
        # if c_cur not in result:
        data = copy.deepcopy(cur)
        result.append(data)
        # result.append(cur[:])             #这种就是复制里面的内容，不用考虑不用deepcopy这个函数

        for i in range (index, len(nums)):
            val = nums[i]
            if val in cur:
                continue
            else:
                cur.append(val)
                self.insert_data(cur, result, nums, i+1)
                cur.pop()

        return