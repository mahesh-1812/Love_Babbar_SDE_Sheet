#7. Write a program to cyclically rotate an array

def cyclicrotate(arr,n):
    end=arr[n-1]
    for i in range(n-1,0,-1):
        arr[i]=arr[i-1]
    arr[0]=end
    return arr

arr=[9,8,7,6,4,3,2,1]
n=len(arr)
print(cyclicrotate(arr,n))
