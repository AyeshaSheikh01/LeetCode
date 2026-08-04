# contain most water 11 
height=[1,1]  
ans=0
i=0 # pointing to the left of the array 
j=len(height)-1 # pointing to the right of the array 
print(i, j) 
# while i<j :  # it will work till i gets smaller than j 
while i<j:
    distance=j-i
    print("distance:",distance) 
    h=min(height[i],height[j]) 
    print("width", h) 
    # finding it all to find the area that contain the max water 
    area=distance*h 
    print(area) 
    if area>ans: 
        ans=area  
        print("using if:", ans) 
    if height[i]<height[j]: 
            i+=1 
    else: 
            j-=1
print(ans) 


