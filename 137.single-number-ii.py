#
# [137] Single Number II
#
# https://leetcode.com/problems/single-number-ii/description/
#
# algorithms
# Medium (42.56%)
# Total Accepted:    132.4K
# Total Submissions: 311K
# Testcase Example:  '[1]'
#
# 
# Given an array of integers, every element appears three times except for one,
# which appears exactly once. Find that single one.
# 
# 
# 
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement
# it without using extra memory?
# 
#
class Solution(object):
    def singleNumber_bad(self, nums):   #负数处理的不太好
        """
        :type nums: List[int]
        :rtype: int
        """
        # 利用bit位来来存储每一位的值，最后利用去余的方式取出来。
        result = 0
        for i in range(0, 32):
            count = 0
            for val in nums:
                count += (val >> i) & 1

            result += (count % 3) << i

        return result if result < 0x7FFFFFFF else result | (~0x100000000 + 1)

    def singleNumber(self, nums):
        #最笨的办法
        nums_count = {}
        for val in nums:
            nums_count[val] = nums_count.get(val, 0) + 1

        for k, v in nums_count.items():
            if v == 1:
                return k


