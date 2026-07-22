# Inorder traversal - 94 leetcode 
class Solution:
    def inorderTraversal(self, root, res=None):  
        if res is None: 
            res=[] 
        if not root: # means root is empty so return NULL
            return res 
        else:  
            self.inorderTraversal(root.left, res)  
            res.append(root.val)
            self.inorderTraversal(root.right, res)  
            return res

            
