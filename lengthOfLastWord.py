# Length of last word in a string - leetcode 58
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        str=s.split()  
        return len(str[-1]) 
s="luffy is still joyboy" 
print(Solution().lengthOfLastWord(s)) 
 
# this satisfies all the test cases. 