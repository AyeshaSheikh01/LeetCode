# reverse words of a string 151 
class Solution:
    def reverseWords(self, string: str) -> str:
        newStr=string.split()  # to make it a list and separate it using white spaces
        arr=list(newStr) 
        i=0  # two pointers
        j=len(arr)-1 
        while(i<j): # changing the values of i and j till i is smaller than j
            arr[i],arr[j]=arr[j],arr[i] 
            i+=1 
            j-=1   
        result = " ".join(arr) 
        return result 

string="a good  example"  
print(Solution().reverseWords(string))