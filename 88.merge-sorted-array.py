#
# [88] Merge Sorted Array
#
# https://leetcode.com/problems/merge-sorted-array/description/
#
# algorithms
# Easy (32.14%)
# Total Accepted:    224.2K
# Total Submissions: 697.4K
# Testcase Example:  '[1]\n1\n[]\n0'
#
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as
# one sorted array.
# 
# 
# Note:
# You may assume that nums1 has enough space (size that is greater or equal to
# m + n) to hold additional elements from nums2. The number of elements
# initialized in nums1 and nums2 are m and n respectively.
#
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        all_index = m + n-1
        l1_index = m - 1
        l2_index = n - 1
        while l1_index >= 0 and l2_index >= 0:
            if nums1[l1_index] >= nums2[l2_index]:
                nums1[all_index] = nums1[l1_index]
                all_index -= 1
                l1_index -= 1
            else:
                nums1[all_index] = nums2[l2_index]
                all_index -= 1
                l2_index -= 1
        if l2_index >= 0:
            # print "here"
            nums1[:l2_index+1] = nums2[:l2_index+1]


    def merge_new(self, nums1, m, nums2, n):
        while m > 0 and n > 0:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]

