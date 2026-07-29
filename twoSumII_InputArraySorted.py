# Two sum II where input array is sorted.
class Solution: # where both pointers move towards each other (converging pointers)
    def twoSum(self, nums: List[int], target: int) -> List[int]:  
        j=len(nums)-1   
        i=0
        while(i<j):
            if (nums[i]+nums[j]==target):  # if target found, return the list with 1-indexed
                ans=list([i+1,j+1])
                return ans
            elif (nums[i]+nums[j]<target): # if less than target, then we will increment i
                i+=1 
            else:  # if more than target, decrement j
                j-=1

nums=[5,25]
target=30
print(Solution().twoSum(nums,target))