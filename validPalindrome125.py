# Valid palindrom - LeetCode 125  
import re
class Solution:
    def isPalindrome(self, s): 
        s=s.lower().replace(" ","")
        print(s)
        res=re.sub(r'[^a-zA-Z0-9]','',s) 
        print(res) 
        reverse=res[::-1]
        print(reverse) 
        if res==reverse:
            return True  
        else: 
            return False 
s="Aisha Sheikh" 
print(Solution().isPalindrome(s)) 

# it satisfies all the test cases. 
