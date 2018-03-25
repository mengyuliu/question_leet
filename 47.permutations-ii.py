#
# [47] Permutations II
#
# https://leetcode.com/problems/permutations-ii/description/
#
# algorithms
# Medium (34.85%)
# Total Accepted:    157.2K
# Total Submissions: 450.6K
# Testcase Example:  '[1,1,2]'
#
# 
# Given a collection of numbers that might contain duplicates, return all
# possible unique permutations.
# 
# 
# 
# For example,
# [1,1,2] have the following unique permutations:
# 
# [
# ⁠ [1,1,2],
# ⁠ [1,2,1],
# ⁠ [2,1,1]
# ]
# 
# 
#


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        single = []
        nums = sorted(nums)
        self.help(nums, result, single)
        return result

    def help(self, nums, result, single):
        if len(nums) == len(single):
            val_list = []
            for index in single:
                val_list.append(nums[index])
            result.append(val_list)
            return
        last = None
        for i in range(len(nums)):
            if i in single:
                continue
            if last == nums[i]:
                continue
            else:
                single.append(i)
                self.help(nums, result, single)
                last = nums[single.pop()]

        return
