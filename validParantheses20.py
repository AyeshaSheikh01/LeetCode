# Valid Parentheses - leetcode 20 
class Solution:
    def isValid(self, s: str):     
        stack=[]
        for ch in s:  
            if ch=="(" or ch=="{" or ch=="[": 
                stack.append(ch) 
            elif ch==")" or ch=="}" or ch=="]": 
                if len(stack)==0: 
                    return False    
                elif stack[-1]=="(" and ch==")" or stack[-1]=="{" and ch=="}" or stack[-1]=="[" and ch=="]": 
                    stack.pop() 
                else: 
                    stack.append(ch)
        if len(stack)==0: 
            return True
        else: 
            return False         
         
s="(){}[]" 
print(Solution().isValid(s))