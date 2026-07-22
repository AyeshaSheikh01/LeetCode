# nums=[1]  
# max=nums[0]
# for i in range(len(nums)): 
#     list=[] 
#     list.append(nums[i])
#     for j in range(len(nums)-i-1): 
#         list.append(nums[j+i+1])  
#         if sum(list)>max: 
#             max=sum(list) 
# print(max)
class Solution:
    def maxSubArray(self, nums):
        current_sum = max_sum = nums[0]
        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)
        return max_sum

nums = [5,4,-1,7,8]
print(Solution().maxSubArray(nums))
 