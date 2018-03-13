#
# [102] Binary Tree Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (42.18%)
# Total Accepted:    225.1K
# Total Submissions: 533.5K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the level order traversal of its nodes' values.
# (ie, from left to right, level by level).
# 
# 
# For example:
# Given binary tree [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 
# return its level order traversal as:
# 
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
# ]
# 
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        stack = []
        #咱们利用循环，还有一个队列去做
        if root != None:
            stack.append([root])
            while(stack):
                current_node_list = stack.pop(0)
                next_level_list = []
                this_level_result = []
                for node in current_node_list:
                    left_node = node.left
                    right_node = node.right
                    if left_node != None:
                        next_level_list.append(left_node)
                    if right_node != None:
                        next_level_list.append(right_node)
                    this_level_result.append(node.val)
                    #print node.val
                if next_level_list != []:
                    stack.append(next_level_list)
                #print next_level_list
                result.append(this_level_result)
        return result
