#
# [69] Sqrt(x)
#
# https://leetcode.com/problems/sqrtx/description/
#
# algorithms
# Easy (28.76%)
# Total Accepted:    216.5K
# Total Submissions: 752.4K
# Testcase Example:  '4'
#
# Implement int sqrt(int x).
# 
# Compute and return the square root of x.
# 
# x is guaranteed to be a non-negative integer.
# 
# 
# 
# Example 1:
# 
# Input: 4
# Output: 2
# 
# 
# 
# Example 2:
# 
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we want to return
# an integer, the decimal part will be truncated.
# 
# 
#
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1 :
            return 1
        start = 0
        end = x
        middle = int((start+end)/2)
        while middle > start:
            val = middle * middle
            if val == x:
                break
            elif val > x:
                end = middle
            elif val < x:
                start = middle
            middle = int((start + end) / 2)
        return middle