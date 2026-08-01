# Squares of sorted array-977 
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)): #checking the each element one by one
            nums[i]=nums[i]**2 # taking square of each element
        return sorted(nums) # returning the sorted array after taking square of each element

nums=[-7,-3,2,3,11] 
print(Solution().sortedSquares(nums))