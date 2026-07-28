# Product of array except self 
nums=[6,4,2,1] 
left=[1]*len(nums) 
right=[1]*len(nums) 
left[0]=1 
right[len(nums)-1]=1 
print(left) 
print(right) 
for i in range(1,len(nums)-1):  
    print("i:", i) 
    print("left[i-1]: ", left[i-1]) 
    print("nums[i-1]:", nums[i-1]) 
    left[i]=left[i-1]*nums[i-1] 
    print("left[i]:", left)  
    print("\n")  
for i in range(right[len(nums)-1], 1, -1):
    print("right[i+1]: ", right[i+1]) 
    print("nums[i+1]:", nums[i+1])
    right[i]=right[i+1]*nums[i+1] 
    print("right[i]:", right) 
    print("\n") 
