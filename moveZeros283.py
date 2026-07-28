# Move zeros  
class Solution:
    def moveZeroes(self, arr): 
        j=0
        for i in range(len(arr)):      
            if(arr[i]!=0 and arr[j]==0):   
                arr[j],arr[i]=arr[i],arr[j] 
                j+=1  
            else: 
                if(arr[j]!=0): 
                    j+=1 
        print(arr)
arr=[0,1,0,3,12]
print(Solution().moveZeroes(arr))