# Converting temp - leetcode 2469 
class Solution:
    def convertTemperature(self, celsius: float): 
        kel=round(celsius+273.15, 3)
        far=round((celsius*1.80)+32.00, 3)   
        ans=[kel,far] 
        return ans 
    
celsius=1000.00      
print(Solution().convertTemperature(celsius))