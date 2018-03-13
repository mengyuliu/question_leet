#
# [33] Search in Rotated Sorted Array
#
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (31.95%)
# Total Accepted:    241.2K
# Total Submissions: 755.1K
# Testcase Example:  '[]\n5'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# 
# You are given a target value to search. If found in the array return its
# index, otherwise return -1.
# 
# You may assume no duplicate exists in the array.
#
class Solution(object):
    def search_first(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: inthuya
        """
        if len(nums)==0:
            return -1
        #遍历找到最小值
        length = len(nums)
        min_index = 0
        max_index = length-1
        for i in range(0, length-1):
            cur_val = nums[i]
            next_val = nums[i+1]
            if next_val < cur_val:
                min_index = i+1
                max_index = i
                break
        if max_index < min_index:
            sort_num = nums[min_index:] + nums[:max_index+1]
        else:
            sort_num = nums
        start = 0
        end = length-1
        # middle = 999
        # print sort_num, start, end
        while (start <=end):
            middle = (start+end)/2
            # print middle
            val = sort_num[middle]
            # print middle, val
            if val == target:
                if max_index < min_index:
                    real_index = middle - len(nums[min_index:])
                else:
                    real_index = middle

                if real_index < 0:
                    real_index = real_index + length
                return real_index
            elif val > target:
                end = middle-1
            elif val < target:
                start = middle+1

        return -1

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: inthuya
        """



