#
# [104] Maximum Depth of Binary Tree
#
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
#
# algorithms
# Easy (54.44%)
# Total Accepted:    313.2K
# Total Submissions: 575.3K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, find its maximum depth.
# 
# The maximum depth is the number of nodes along the longest path from the root
# node down to the farthest leaf node.
# 
# For example:
# Given binary tree [3,9,20,null,null,15,7],
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# return its depth = 3.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root, depth = 0, max_depth = 0):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root != None:
            left_node = root.left
            right_node = root.right
            max_depth = max(max_depth+1, depth)
            left_max = self.maxDepth(left_node, depth +1, max_depth)
            right_max = self.maxDepth(right_node, depth +1, max_depth)
            max_depth = max(max_depth, left_max, right_max)
        return max_depth
