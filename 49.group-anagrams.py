#
# [49] Group Anagrams
#
# https://leetcode.com/problems/group-anagrams/description/
#
# algorithms
# Medium (38.11%)
# Total Accepted:    189.3K
# Total Submissions: 496.5K
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# Given an array of strings, group anagrams together.
# 
# 
# For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
# Return:
# 
# [
# ⁠ ["ate", "eat","tea"],
# ⁠ ["nat","tan"],
# ⁠ ["bat"]
# ]
# 
# Note: All inputs will be in lower-case.
#
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict_result = {}
        for item in strs:
            # str_sorted = ''.join(sorted(item))
            str_sorted = tuple(sorted(item))
            # if str_sorted in dict_result:
            #     temp_list = dict_result[str_sorted]
            #     temp_list.append(item)
            #     dict_result[str_sorted] = temp_list
            # else:
            #     dict_result[str_sorted] = [item]
            dict_result[str_sorted] = dict_result.get(str_sorted, []) + [item]

        # result = []
        # for _, val in dict_result.items():
        #     result.append(val)

        return dict_result.values()



