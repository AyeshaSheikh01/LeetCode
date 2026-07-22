class Solution:
    def findDisappearedNumbers(self, nums):  
        set1=set(range(1, len(nums)+1)) # makes a list of unique numbers from 1 to n where n is the length of the array 
        set2=set(nums) #distinct numbers
        return list(set1-set2) # returns the difference between the two sets which is the missing numbers
 

nums=[4,3,2,7,8,2,3,1]
print(Solution().findDisappearedNumbers(nums)) 
# passed all the test cases