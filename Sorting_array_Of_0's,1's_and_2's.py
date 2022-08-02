#4. Given an array consisting of 0's ,1's and 2's sort the array

def sortarray(arr):
    low =0
    mid=0
    high=len(arr)-1
    while high>=mid:
        if arr[mid]==0:
            arr[low],arr[mid]=arr[mid],arr[low]
            low+=1
            mid+=1
        elif arr[mid]==1:
            mid+=1
        else:
            arr[high],arr[mid]=arr[mid],arr[high]
            high-=1
    return arr

arr=[2,1,0,2,0,1]
print(sortarray(arr))

