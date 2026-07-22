# Two Sum Problem: Find indices of the two numbers such that they add up to a specific target.
class Solution: 
    def twoSum(self, UniqueInteger, target):  
        found=False
        for i in range(len(UniqueInteger)): 
            for j in range(len(UniqueInteger)-1): 
                j=j+1
                if (i!=j):
                    res= UniqueInteger[i]+UniqueInteger[j] 
                    if (res==target):
                        finalList=[]
                        finalList.append(i)  
                        finalList.append(j)   
                        return finalList                 
integer=[2,2,8,12] 
target=10
print(Solution().twoSum(integer, target)) 
# This question satisfies all the test cases. 