# 3Sum - 15
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]: 
        nums.sort() # first sort the list
        listResult=[] # will store all the triplets group
        for i in range(len(nums)-2): 
            j=i+1 
            k=len(nums)-1 
            if i > 0 and nums[i] == nums[i-1]: # if its same, it must skip to avoid the duplicate triplets
                continue 
            while(j<k): 
                if nums[i]+nums[j]+nums[k]==0: # if found, append to the list and increment j by 1 and decrement k by 1
                    listResult.append(list([nums[i],nums[j], nums[k]]))   
                    j+=1 
                    k-=1
                    # Skip duplicates for j
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    # Skip duplicates for k
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                elif nums[i]+nums[j]+nums[k]>0: # as list is sorted, if sum greater than zero, we decrease the k
                    k-=1 
                else: # if smaller than zero, we increase the j 
                    j+=1  
                # because i remains same while j and k is on very left and right of nums and moves toward each other. 
        return listResult
    


nums=[1,2,0,1,0,0,0,0]  
print(Solution().threeSum(nums))