# Valid Anagram - Leetcode 242 
class Solution:
    def isAnagram(self, s: str, t: str):
        s=sorted(s)  
        t=sorted(t) 
        if s==t: 
            return True 
        else:     
            return False
s="rat" 
t="car" 
print(Solution().isAnagram(s,t))

