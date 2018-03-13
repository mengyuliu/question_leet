#
# [297] Serialize and Deserialize Binary Tree
#
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
#
# algorithms
# Hard (34.75%)
# Total Accepted:    96.7K
# Total Submissions: 278.2K
# Testcase Example:  '[1,2,3,null,null,4,5]'
#
# Serialization is the process of converting a data structure or object into a
# sequence of bits so that it can be stored in a file or memory buffer, or
# transmitted across a network connection link to be reconstructed later in the
# same or another computer environment.
# 
# Design an algorithm to serialize and deserialize a binary tree. There is no
# restriction on how your serialization/deserialization algorithm should work.
# You just need to ensure that a binary tree can be serialized to a string and
# this string can be deserialized to the original tree structure.
# 
# For example, you may serialize the following tree
# 
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   3
# ⁠    / \
# ⁠   4   5
# 
# 
# as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a
# binary tree. You do not necessarily need to follow this format, so please be
# creative and come up with different approaches yourself.
# 
# 
# 
# Note: Do not use class member/global/static variables to store states. Your
# serialize and deserialize algorithms should be stateless.
# 
# Credits:
# Special thanks to @Louis1992 for adding this problem and creating all test
# cases.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        result = []
        stack = [root]
        while(stack):
            node = stack.pop(0)
            if node == None:
                result.append('#')
            else:
                result.append(node.val)
                left = node.left
                right = node.right
                stack.append(left)
                stack.append(right)

        return ','.join([str(i) for i in result])



    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # print data
        tree_list = data.split(',')
        if not tree_list or data == '#':
            return None
        stack = []
        root = TreeNode(None)
        stack.append(root)
        while (tree_list):
            val = tree_list.pop(0)
            node = stack.pop(0)
            if val != '#':
                node.val = val

                left_node = TreeNode(None)
                right_node = TreeNode(None)
                stack_len = len(stack)
                # print tree_list[stack_len]
                if tree_list[stack_len] != '#':
                    node.left = left_node
                if tree_list[stack_len+1] != '#':
                    node.right = right_node
                stack.append(left_node)
                stack.append(right_node)

        return root

        # Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
