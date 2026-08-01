# Merge sorted arrays - 88 
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None: 
        i=m-1 
        j=n-1  
        k=m+n-1 
        while(j>=0 and i>=0):
            if nums1[i] > nums2[j]:  
                nums1[k] = nums1[i]  # Take the larger number from nums1
                i -= 1               # Move the nums1 pointer down
                k -= 1
            else:  
                nums1[k] = nums2[j]  # Take the larger number from nums2
                j -= 1               # Move the nums2 pointer down
                k -= 1  
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
nums1=[1,2,3,0,0,0] 
nums2=[2,5,6] 
m=3 
n=2  
print(Solution().merge(nums1, m, nums2, n)) 