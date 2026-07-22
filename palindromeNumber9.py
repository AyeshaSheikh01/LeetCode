# Palindrome Number - leetcode 9 

class Solution:
    def isPalindrome(self, x: int): 
        string=str(x)
        if string == string[::-1]:
            return True  
        else: 
            return False
 
x=101 
print(Solution().isPalindrome(x))