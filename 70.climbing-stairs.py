#
# [70] Climbing Stairs
#
# https://leetcode.com/problems/climbing-stairs/description/
#
# algorithms
# Easy (41.11%)
# Total Accepted:    237.8K
# Total Submissions: 578.4K
# Testcase Example:  '2'
#
# You are climbing a stair case. It takes n steps to reach to the top.
# 
# Each time you can either climb 1 or 2 steps. In how many distinct ways can
# you climb to the top?
# 
# 
# Note: Given n will be a positive integer.
# 
# 
# 
# 
# Example 1:
# 
# Input: 2
# Output:  2
# Explanation:  There are two ways to climb to the top.
# 
# 1. 1 step + 1 step
# 2. 2 steps
# 
# 
# 
# Example 2:
# 
# Input: 3
# Output:  3
# Explanation:  There are three ways to climb to the top.
# 
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
# 
# 
#
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #斐波那契数列问题
        prev = 1
        curr = 2
        if n ==1:
            return 1
        elif n ==2:
            return 2

        count = 2
        while (count < n):
            next = prev + curr
            count+=1
            if count == n:
                return next
            prev = curr
            curr = next

        return
