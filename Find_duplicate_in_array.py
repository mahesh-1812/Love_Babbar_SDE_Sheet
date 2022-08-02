# 11. Find the duplicate number in the array
# Approach 1
def findup(arr,n):
    temp=[]
    for i in range(0,n):
        for j in range(i+1,n):
            if arr[i]==arr[j]:
                temp.append(arr[j])
    return temp

# After implementing we are getting run time error so we are going for another approach

# Approach 2
def findup1(nums,n):

for num in nums:
        print(num)
        if nums[abs(num)] < 0:
            return abs(num)
            
        nums[abs(num)] *= -1
    
nums=[3,1,3,4,2]
arr=[5,4,2,4,1]
n=len(nums)-1
findup1(nums,n)
findup(arr,n)

