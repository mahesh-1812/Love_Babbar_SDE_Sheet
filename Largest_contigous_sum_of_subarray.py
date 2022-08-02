#8. Largest contigous sum subarray

def contigousum(arr):
    sum_end=arr[0]
    accumulated=arr[0]
    for i in range(0,len(arr)):
        cur=arr[i]
        sum_end=(max(sum_end+cur,cur))
        accumulated=max(sum_end,accumulated)
    return accumulated

arr=[-1,-2,-3,-4]
print(contigousum(arr))
