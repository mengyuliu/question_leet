#
# [34] Search for a Range
#
# https://leetcode.com/problems/search-for-a-range/description/
#
# algorithms
# Medium (31.59%)
# Total Accepted:    180.5K
# Total Submissions: 571.3K
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# Given an array of integers sorted in ascending order, find the starting and
# ending position of a given target value.
# 
# Your algorithm's runtime complexity must be in the order of O(log n).
# 
# If the target is not found in the array, return [-1, -1].
# 
# 
# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4].
# 
#
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) ==0:
            return [-1, -1]
        left, right = 0 , len(nums)-1
        while (left<=right):
            middle = (left+right)/2
            val = nums[middle]
            if val == target:

                if middle == 0:
                    start =0
                    end = start
                    while end+1 <= len(nums)-1 and nums[end+1] == target:
                        end+=1
                    return [start, end]
                else:
                    prev_val = nums[middle-1]
                    if prev_val < val:
                        start = middle
                        end = start
                        while end + 1 <= len(nums) - 1 and nums[end + 1] == target:
                            end += 1
                        return [start, end]
                    else:
                        right = middle -1


            elif val > target:
                right = middle -1
            else:
                left = middle +1


        return [-1, -1]
