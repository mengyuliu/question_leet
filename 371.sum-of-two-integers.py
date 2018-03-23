#
# [371] Sum of Two Integers
#
# https://leetcode.com/problems/sum-of-two-integers/description/
#
# algorithms
# Easy (50.93%)
# Total Accepted:    93.3K
# Total Submissions: 183.3K
# Testcase Example:  '1\n2'
#
# Calculate the sum of two integers a and b, but you are not allowed to use the
# operator + and -.
# 
# Example:
# Given a = 1 and b = 2, return 3.
# 
# 
# Credits:Special thanks to @fujiaozhu for adding this problem and creating all
# test cases.
#
class Solution(object):
    def getSum_wrong(self, a, b): #主体思路是这样的，但是还需要处理负数的问题
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while(b):
            carry = a & b
            a = a ^ b
            b = carry << 1
            # print a, b
        return a

    def getSum(self, a, b):
        while (b):
            carry = a & b
            a = (a ^ b) % 0x100000000
            b = (carry << 1) % 0x100000000
            # print , b
        return a if a <= 0x7FFFFFFF else a | (~0x100000000+1)