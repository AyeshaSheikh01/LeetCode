# Postorder trevarsal - leetcode 145 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root, res=None):  
        if res is None: 
            res=[] 
        if not root: # means root is empty so return NULL
            return res 
        else:    
            self.postorderTraversal(root.left, res)  
            self.postorderTraversal(root.right, res)
            res.append(root.val)  
            return res   