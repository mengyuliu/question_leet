#
# [278] First Bad Version
#
# https://leetcode.com/problems/first-bad-version/description/
#
# algorithms
# Easy (25.96%)
# Total Accepted:    138.4K
# Total Submissions: 533.3K
# Testcase Example:  '1 version\n1 is the first bad version.'
#
# 
# You are a product manager and currently leading a team to develop a new
# product. Unfortunately, the latest version of your product fails the quality
# check. Since each version is developed based on the previous version, all the
# versions after a bad version are also bad. 
# 
# 
# 
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first
# bad one, which causes all the following ones to be bad.
# 
# 
# 
# You are given an API bool isBadVersion(version) which will return whether
# version is bad. Implement a function to find the first bad version. You
# should minimize the number of calls to the API.
# 
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<2:
            return n

        start, end = 1, n
        while (start <= end):
            middle = (start+end)/2
            result = isBadVersion(middle)
            # print middle, result
            if result:
                if middle == 1:
                    return middle
                prev = isBadVersion(middle-1)
                if prev:
                    end = middle -1
                else:
                    return middle
            else:
                start = middle +1

        return middle

    #simple solution
    #只需要比较两个start 与 end的值，确定那个