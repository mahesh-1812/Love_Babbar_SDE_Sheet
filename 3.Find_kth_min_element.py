#3.Find the minimum kth element

#One more approach to be implemented (mean heap approach)


def findkmin(arr,k):
    arr.sort()
    min=arr[k-1]
    return min
  
def findkmax(arr,k):
    arr.sort()
    max=arr[k-1]
    return max


arr=[2,8,6,5,1,]
k=3
findkmin(arr,k)
findkmax(arr,k)


#In the above solution I have used the in built function of sort to sort the arrays and then use the [k-1] to find the kth  min and max element
#For finding the max element the similar method is used .
