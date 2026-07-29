# Find the difference between two strings s and t.  
class Solution:
    def findTheDifference(self, s: str, t: str) -> str: 
        s=sorted(s) 
        t=sorted(t) 
        for i in range(len(s)):  
            if (s[i]!=t[i]): 
                return t[i] # return the value of the character that is different
        return t[-1] # if not, return the last character of t as per index

s="" 
t="y"   
print(Solution().findTheDifference(s,t))  

