#
# [112] Path Sum
#
# https://leetcode.com/problems/path-sum/description/
#
# algorithms
# Easy (34.76%)
# Total Accepted:    205.9K
# Total Submissions: 592.4K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,null,1]\n22'
#
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path
# such that adding up all the values along the path equals the given sum.
# 
# For example:
# Given the below binary tree and sum = 22,
# 
# 
# ⁠             5
# ⁠            / \
# ⁠           4   8
# ⁠          /   / \
# ⁠         11  13  4
# ⁠        /  \      \
# ⁠       7    2      1
# 
# 
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum, path_val = 0):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        node_val = root.val
        left_node = root.left
        right_node = root.right
        if left_node == None and right_node == None:
            if path_val + node_val == sum:
                return True
            else:
                return False
        left_result = self.hasPathSum(left_node, sum, path_val+node_val)
        right_result = self.hasPathSum(right_node, sum, path_val+node_val)
        if left_result or right_result:
            return True
        else:
            return False


