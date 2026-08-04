# Merge strings alternately- 1768
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str: 
        word1=list(word1) # converting strings into list
        word2=list(word2) 
        result=[] 
        i=0 
        j=0  
        while(i<len(word1) or j<len(word2)): # to check if both works well
            if(i<len(word1)): #as long as elements are left in word 1 array
                result.append(word1[i])  
            if(j<len(word2)): #as long as elements are left in word 2 array
                result.append(word2[j]) 
            i+=1
            j+=1  
        result="".join(result)  # changing it back into a string
        return result 
word1="abcd" 
word2="pq"   
print(Solution().mergeAlternately(word1,word2))