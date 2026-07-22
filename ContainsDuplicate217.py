#to check if there are any duplicates in the list
class Solution:
    def containsDuplicate(self, nums):  
        set1=set(nums)  
        for i in range(len(nums)):  
            if len(set1)!=len(nums): 
                return True 
        return False
nums=[1,2,3,4] 
print(Solution().containsDuplicate(nums))              
# This question satisfies all the test cases.