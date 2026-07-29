# Squares of sorted array-977 
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)): 
            nums[i]=nums[i]**2 
        return sorted(nums)

nums=[-7,-3,2,3,11] 
print(Solution().sortedSquares(nums))