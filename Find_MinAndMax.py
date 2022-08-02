#Minimum and maximum of array
def findMin(arr):
    min=arr[0]
    max=arr[0]
    for i in range (len(arr)-1):
        # for j in range(i+1,len(arr)-1): 
        if arr[i]<min:
            min=arr[i]
        if arr[i]>max:
            max=arr[i]
    return min,max
   
arr=[3,2,1,167,56,1000]
print(findMin(arr))




#In the above solution I have used a linear search method for finding the min and max of array.For the optimised solution of this problem I would recommen to first sort the 
#array and then  find the min and max
#Another operation we could perform is by using the  math function 
