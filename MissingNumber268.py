# Missing numbers 
class Solution:
    def missingNumber(self, nums):
        set1=set(range(0, len(nums)+1)) 
        set2=set(nums)  
        ans=list(set1-set2) 
        result=ans[0]
        return result
 

nums=[0,1,2,3,5]
print(Solution().missingNumber(nums))