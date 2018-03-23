#
# [136] Single Number
#
# https://leetcode.com/problems/single-number/description/
#
# algorithms
# Easy (55.33%)
# Total Accepted:    286.2K
# Total Submissions: 517.1K
# Testcase Example:  '[1]'
#
# Given an array of integers, every element appears twice except for one. Find
# that single one.
# 
# 
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement
# it without using extra memory?
# 
#
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = 0
        for val in nums:
            num  =num ^ val

        return  num

    def singleNumber_sort(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_count = {}
        for val in nums:
            nums_count[val] = nums_count.get(val, 0) +1

        for k, v in nums_count.items():
            if v ==1:
                return k
