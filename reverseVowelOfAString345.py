# Reverse vowel of a string 
class Solution:
    def reverseVowels(self, wordstr: str) -> str:
        vowelList=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'] 
        word=list(wordstr) # string immutable so changed into a list
        i=0 
        j=len(word)-1  
        while (i<j):  # both pointers move toward each other
            if word[i] in vowelList:  # if value of i is vowel check the condition on j
                if word[j] in vowelList: # if value of j is vowel, swap  otherwise decrease j by 1
                    word[i], word[j] = word[j],word[i]  
                    j-=1 
                    i+=1
                else: 
                    j-=1 
            else: # else increase of i by 1
                i+=1  
        finalWord = "".join(word) # changing the list into a string again
        return finalWord  

wordstr="leetcode"   
print(Solution().reverseVowels(wordstr))