# sort colors - leetcode 75
class Solution:
    def sortColors(self, nums):   
        s=sorted(nums) 
        while nums!=s: # check if nums is not empty
            pop=nums.pop()  
            if pop < nums[0]: # check for empty ans, and if pop is grater or equal to last ele of ans
                nums.insert(0, pop)  
            elif pop >= nums[0]: # check for empty ans, and if pop is less than last ele of ans
                nums.append(pop)  
        return nums
nums=[2,0,1]  
print(Solution().sortColors(nums))
