# Most Common word  
import re
 
class Solution:
    def mostCommonWord(self, paragraph, bannedword):    
        cleaned_text = re.sub(r'[^\w\s]', ' ', paragraph)          
        banned_set = {word.lower() for word in bannedword} 
        paragraph=cleaned_text.lower().split()
        mapSave={}   
        # for word in paragraph:  
        for word in paragraph:  
            if word not in banned_set: 
                if word in mapSave:  #if number already there, increase its value
                    mapSave[word]+=1      
                else: 
                    mapSave[word]=1  # if not alreday there, make it equal to 1  
        most_frequent = max(mapSave, key=mapSave.get) 
        return most_frequent  


paragraph="Bob hit a ball, the hit BALL flew far after it was hit."   
bannedword=["hIt"]
print(Solution().mostCommonWord(paragraph, bannedword))


