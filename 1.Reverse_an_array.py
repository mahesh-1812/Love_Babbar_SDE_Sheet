#First problem of the sde sheet
#Reverse array

def reverse(arr):
    temp=0
    start=0
    end=len(arr)-1
    while (start < end):
        temp=arr[start]
        arr[start]=arr[end]
        arr[end]=temp
        start+=1
        end-=1
    return arr

arr=[1,5,6,8,12,45,18,36,27,81,54,72,7,10]
reverse(arr)
