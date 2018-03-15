#
# [98] Validate Binary Search Tree
#
# https://leetcode.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (24.03%)
# Total Accepted:    227.3K
# Total Submissions: 945.8K
# Testcase Example:  '[2,1,3]'
#
# 
# Given a binary tree, determine if it is a valid binary search tree (BST).
# 
# 
# 
# Assume a BST is defined as follows:
# 
# The left subtree of a node contains only nodes with keys less than the node's
# key.
# The right subtree of a node contains only nodes with keys greater than the
# node's key.
# Both the left and right subtrees must also be binary search trees.
# 
# 
# 
# Example 1:
# 
# ⁠   2
# ⁠  / \
# ⁠ 1   3
# 
# Binary tree [2,1,3], return true.
# 
# 
# Example 2:
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   3
# 
# Binary tree [1,2,3], return false.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree_elem(self, root):
        result = []
        if not root:
            return result
        val = root.val
        left_list = self.tree_elem(root.left)
        right_list = self.tree_elem(root.right)
        result.append(val)
        result.extend(left_list)
        result.extend(right_list)

        return result


    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # result = True
        if not root:
            return True
        val = root.val
        #左边的节点
        left_list = self.tree_elem(root.left)
        left_result = [True if val>left_val else False for left_val in left_list]
        for result in left_result:
            if not result:
                return False
        #右边的节点
        right_list = self.tree_elem(root.right)
        right_result = [True if val < right_val else False for right_val in right_list]
        for result in right_result:
            if not result:
                return False

        left_com = self.isValidBST(root.left)
        right_com = self.isValidBST(root.right)
        if left_com and right_com:
            return True
        else:
            return False



