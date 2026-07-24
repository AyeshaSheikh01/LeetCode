# Top k frequent element
class Solution:
    def topKFrequent(self, nums, k):  
        list=[]   
        #Initialize a hashmap 
        mapSave={}  
        #put all values in hashmap
        for n in nums: 
            if n in mapSave: 
                mapSave[n]+=1 
            else: 
                mapSave[n]=1    
        mapSave=sorted(mapSave, key=mapSave.get, reverse=True)  
        print(mapSave)
        if k > len(mapSave):  
            return mapSave 
        else: 
            for i in range(k):  
                list.append(mapSave[i])
        return list

nums=[1,1,1,2,2,2,2,2,3,3,3,3,3]   
k=1
print(Solution().topKFrequent(nums,k))  
        

        