#
# [46] Permutations
#
# https://leetcode.com/problems/permutations/description/
#
# algorithms
# Medium (46.93%)
# Total Accepted:    225.5K
# Total Submissions: 479.9K
# Testcase Example:  '[1,2,3]'
#
# 
# Given a collection of distinct numbers, return all possible permutations.
# 
# 
# 
# For example,
# [1,2,3] have the following permutations:
# 
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
# 
#
import copy
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        for i in range(len(nums)):
            single = [nums[i]]
            result = self.insert_data(result, single, nums)

        return result

    def insert_data(self, result,single, nums):
        if len(single) == len(nums):
            data = copy.deepcopy(single)
            result.append(data)
            # print single, result
            return result

        for val in nums:
            if val in single:
                continue
            else:
                single.append(val)
                result = self.insert_data(result, single, nums)
                single.pop()

        return result


