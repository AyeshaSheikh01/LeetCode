# Longest Common Prefix - leetcode 387 
class Solution:
    def firstUniqChar(self, s: str):
        s = s.lower()
        copy = s          
        unique = 0
        for i in range(len(s)): 
            if copy[i] == " ":
                continue
            char = copy[i]
            rem = copy[i+1:] 
            if char in rem:
                copy = copy.replace(char, " ") 
                continue 
            elif char not in rem:  
                unique = 1
                return i

        if unique == 0: 
            return -1 

s = "aabb" 
print(Solution().firstUniqChar(s))