#
# [73] Set Matrix Zeroes
#
# https://leetcode.com/problems/set-matrix-zeroes/description/
#
# algorithms
# Medium (36.48%)
# Total Accepted:    133.8K
# Total Submissions: 366.7K
# Testcase Example:  '[[0]]'
#
# 
# Given a m x n matrix, if an element is 0, set its entire row and column to 0.
# Do it in place.
# 
# 
# click to show follow up.
# 
# Follow up:
# 
# 
# Did you use extra space?
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?
# 
# 
#
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row_set = set()
        col_set = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0 :
                    row_set.add(i)
                    col_set.add(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in row_set or j in col_set:
                    matrix[i][j] = 0




