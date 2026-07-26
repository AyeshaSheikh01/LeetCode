# Group Anagrams
class Solution:
    def groupAnagrams(self, strs): 
        strs=[s.lower() for s in strs] # for the edge case, make all the strings small
        mapSave={}  
        for index,s in enumerate(strs):  
            sortedS="".join(sorted(s))  # sorting makes a string as list so using join to let it stay as a string
            if sortedS in mapSave:     
                mapSave[sortedS].append(strs[index]) # appending the indexes if the sorted s is same
            else:  
                mapSave[sortedS]=[strs[index]]   #saving the strs values at certain index in a mapSave
        finalResult=list(mapSave.values())  
        return finalResult # only extractingg the values from the mapSave
strs=["Eat", "tea", "ate"]  
print(Solution().groupAnagrams(strs))


