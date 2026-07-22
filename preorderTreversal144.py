# Preorder traversal - leetcode 144 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root, res=None):  
        if res is None: 
            res=[] 
        if not root: # means root is empty so return NULL
            return res 
        else:   
            res.append(root.val)
            self.preorderTraversal(root.left, res)  
            self.preorderTraversal(root.right, res)  
            return res
