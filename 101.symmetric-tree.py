#
# [101] Symmetric Tree
#
# https://leetcode.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (40.18%)
# Total Accepted:    235.7K
# Total Submissions: 586.7K
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric
# around its center).
# 
# 
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
# 
# 
# 
# But the following [1,2,2,null,3,null,3]  is not:
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
# 
# 
# 
# 
# Note:
# Bonus points if you could solve it both recursively and iteratively.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #res = []
        next_level = []
        if root != None:
            next_level.append([root])
            while (next_level):
                cur_level = next_level.pop(0)
                temp_list = []
                temp_data = []
                for node in cur_level:
                    if node != None:
                        left_node = node.left
                        right_node = node.right
                        temp_data.append(node.val)
                        temp_list.append(left_node)
                        temp_list.append(right_node)
                    else:
                        temp_data.append(None)
                if temp_list != []:
                    next_level.append(temp_list)
                #res.append(temp_data)
                #对每层的数据进行判断，是否对称
                #print temp_data
                for i in range(0, int(len(temp_data)/2)):
                    #print temp_data[i], temp_data[-(i+1)]
                    if temp_data[i] != temp_data[-(i+1)]:
                        return False
        #print res
        return True





