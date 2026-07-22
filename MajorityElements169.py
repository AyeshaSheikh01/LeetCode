# Majority Elements 
class Solution:
    def majorityElement(self, nums): 
        map={} #initializing a map  
        frequency=len(nums)/2 # to check the frequency of the number in the array
        for i in range(len(nums)):   
            if nums[i] in map:  #if number already there, increase its value
                map[nums[i]]+=1    
            else: 
                map[nums[i]]=1  # if not alreday there, make it equal to 1
            if(map[nums[i]]>frequency):   
                return nums[i]    

nums=[3,2,3] 
print(Solution().majorityElement(nums))