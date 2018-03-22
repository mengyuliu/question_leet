#
# [347] Top K Frequent Elements
#
# https://leetcode.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (49.55%)
# Total Accepted:    98.2K
# Total Submissions: 198.2K
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# 
# Given a non-empty array of integers, return the k most frequent elements.
# 
# For example,
# Given [1,1,1,2,2,3] and k = 2, return [1,2].
# 
# 
# Note: 
# 
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is
# the array's size.
# 
#
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        val_count = {}
        for val in nums:
            val_count[val] = val_count.get(val, 0)+1

        # print val_count.items()
        # count_val = {}
        # for k, v in val_count.items():
        #     count_val[v] = count_val.get(v,[])+[k]
        #     print count_val
        #     # print k, v

        sort_list = sorted(val_count.items(), key = lambda item:item[1],reverse= True)
        # print sort_list
        return  [v for v, _ in sort_list][:k]
        # print count_val
        # return count_val[k]
