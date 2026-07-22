# Find the index of the first occurrence in a string - leetcode 28 
class Solution:
    def strStr(self, x: str, y: str) -> int:   
        x=x.lower() 
        y=y.lower()
        if y in x: 
            return x.index(y)
        else: 
            return -1
x="abc" 
y="" 
print(Solution().strStr(x, y))