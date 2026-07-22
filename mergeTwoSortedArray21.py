# list=[1,3,4] 
# list2=[1,2,4]  
# for i in list2: 
#     list.append(i) 
# print(list) 
# print(sorted(list)) 

class Solution:
    def mergeTwoLists(self, list1, list2):  
        for i in list2: 
            list1.append(i) 
            result=sorted(list1)  
        return result
list1=[1,3,4] 
list2=[1,2,4] 
print(Solution().mergeTwoLists(list1, list2))  