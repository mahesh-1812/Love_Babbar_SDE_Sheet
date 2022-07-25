#12.Merge two sorted array without using any extra spaces

#Approach 1
#With the use of built in function we have attempted this one
def sort1(arr1,n,arr2,m):
    arr1.extend(arr2)
    s=arr1.sort()
    arr2.clear()
    return s

# #Approach2
# #Without using builtin function 
def mergesort(arr1,n,arr2,m):
    #We have appended the arr2 into arr1
    for i in range(0,m):
        arr1.append(arr2[i])

    #After merging arrays we are sorting the array here 
    for j in range(0,len(arr1)-1):
        for k in range(j+1,len(arr1)-1):
            if arr1[j]>arr1[k]:
                arr1[j],arr1[k]=arr1[k],arr1[j]
    return arr1
    
arr1=[1,3,5,7]
n=len(arr1)-1
arr2=[0,2,6,8,9]
m=len(arr2)-1
mergesort(arr1,n,arr2,m)
