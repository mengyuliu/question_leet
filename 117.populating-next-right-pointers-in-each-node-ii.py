#
# [117] Populating Next Right Pointers in Each Node II
#
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/
#
# algorithms
# Medium (33.93%)
# Total Accepted:    124K
# Total Submissions: 365.5K
# Testcase Example:  '{}'
#
# Follow up for problem "Populating Next Right Pointers in Each Node".
# What if the given tree could be any binary tree? Would your previous solution
# still work?
# 
# Note:
# You may only use constant extra space.
# 
# 
# For example,
# Given the following binary tree,
# 
# ⁠        1
# ⁠      /  \
# ⁠     2    3
# ⁠    / \    \
# ⁠   4   5    7
# 
# 
# 
# After calling your function, the tree should look like:
# 
# ⁠        1 -> NULL
# ⁠      /  \
# ⁠     2 -> 3 -> NULL
# ⁠    / \    \
# ⁠   4-> 5 -> 7 -> NULL
# 
# 
#
# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        levelstart = root

        while levelstart:
            pre = None
            cur = levelstart
            levelstart = None
            while cur:
                "note: first pre is the next level start node, it maybe in left or in right"
                if cur.left:
                    if pre:
                        pre.next = cur.left
                    else:
                        levelstart = cur.left
                    pre = cur.left
                if cur.right:
                    if pre:
                        pre.next = cur.right
                    else:
                        levelstart = cur.right
                    pre = cur.right
                cur = cur.next