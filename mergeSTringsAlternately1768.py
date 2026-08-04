# Merge strings alternately- 1768
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str: 
        word1=list(word1) 
        word2=list(word2) 
        result=[] 
        i=0 
        j=0  
        while(i<len(word1) or j<len(word2)): 
            if(i<len(word1)):
                result.append(word1[i])  
            if(j<len(word2)):
                result.append(word2[j])
            i+=1
            j+=1  
        result="".join(result) 
        return result 
word1="abcd" 
word2="pq"   
print(Solution().mergeAlternately(word1,word2))