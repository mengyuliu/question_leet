#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (31.59%)
# Total Accepted:    257K
# Total Submissions: 813.4K
# Testcase Example:  '[]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
# 
#
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''

        common = list(strs[0])
        for i in range(1, len(strs)):
            val = list(strs[i])
            index = 0
            if len(common) > len(val):
                while(index < len(val)):
                    if common[index] == val[index]:
                        index +=1
                    else:
                        break
            else:
                while (index < len(common)):
                    if common[index] == val[index]:
                        index += 1
                    else:
                        break
            common = common[:index]

        return ''.join(common)
