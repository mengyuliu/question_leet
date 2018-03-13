#
# [145] Binary Tree Postorder Traversal
#
# https://leetcode.com/problems/binary-tree-postorder-traversal/description/
#
# algorithms
# Hard (41.78%)
# Total Accepted:    170.7K
# Total Submissions: 408.5K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the postorder traversal of its nodes' values.
# 
# For example:
# Given binary tree [1,null,2,3],
# 
# 
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# 
# 
# 
# return [3,2,1].
# 
# Note: Recursive solution is trivial, could you do it iteratively?
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result_list = []
        left_list = []
        right_list = []
        if root != None:
            left_node = root.left
            right_node = root.right
            if left_list != None:
                left_list = self.postorderTraversal(left_node)
            result_list.extend(left_list)
            if right_list != None:
                right_list = self.postorderTraversal(right_node)
            result_list.extend(right_list)
            result_list.append(root.val)
        return result_list



