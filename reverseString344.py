# reverse the string
class Solution:
    def reverseString(self, s: List[str]) -> None:
        i=0  
        j=len(s)-1 
        while i<j:  
            if (i!=j):  
                s[i],s[j]=s[j],s[i]  # reversing the string by swapping the first and last element of the string
                i=i+1 
                j=j-1
s=["h","e","l","l","o"]
print(Solution().reverseString(s))  

