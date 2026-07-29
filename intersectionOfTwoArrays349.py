# Intersection of two arrays
class Solution:
    def intersection(self, nums1, nums2): 
        listArray=[]
        set1=set(nums1) # making both lists as sets to remove duplicates
        set2=set(nums2) 
        newSet=set1.intersection(set2) # finding the common
        listArray=list(newSet)  # changing into list to return
        return listArray

nums1=[4,9,5]
nums2=[9,4,9,8,4]  
print(Solution().intersection(nums1,nums2))