#
# [350] Intersection of Two Arrays II
#
# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
#
# algorithms
# Easy (44.45%)
# Total Accepted:    100.2K
# Total Submissions: 225.4K
# Testcase Example:  '[]\n[]'
#
# 
# Given two arrays, write a function to compute their intersection.
# 
# 
# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].
# 
# 
# Note:
# 
# Each element in the result should appear as many times as it shows in both
# arrays.
# The result can be in any order.
# 
# 
# 
# Follow up:
# 
# What if the given array is already sorted? How would you optimize your
# algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is
# better?
# What if elements of nums2 are stored on disk, and the memory is limited such
# that you cannot load all elements into the memory at once?
# 
# 
#
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s1 = set(nums1)
        s2 = set(nums2)
        comm_s = s1 & s2
        comm_s1_count = {}
        comm_s2_count = {}
        if not comm_s:
            return []
        # print comm_s
        for val in nums1:
            if val in comm_s:
                if comm_s1_count.has_key(val):
                    temp = comm_s1_count[val]
                    temp+=1
                    comm_s1_count[val]= temp
                else:
                    comm_s1_count[val] = 1


        for val in nums2:
            if val in comm_s:
                if comm_s2_count.has_key(val):
                    temp = comm_s2_count[val]
                    temp+=1
                    comm_s2_count[val]= temp
                else:
                    comm_s2_count[val] = 1
        result = []
        for key in comm_s:
            c1 = comm_s1_count[key]
            c2 = comm_s2_count[key]
            if c1 > c2:
                for _ in range(c2):
                    result.append(key)
            else:
                for _ in range(c1):
                    result.append(key)

        return result