#13.Merge intervals
#Approach1
def mergeintervals(arr):
    for i in range(0,len(arr)-1):
        for j in range(i+1,len(arr)-1):
            if arr[i][-1]<arr[j][-1]:
                arr[i][-1]=arr[j][-1]
                arr.remove(arr[j])
                break
    return arr

#Approach2
def mergeinter(intervals):
    intervals.sort()
    res = []
    start = intervals[0][0]
    stop = intervals[0][1]
    
    for i in range(len(intervals)):
        if intervals[i][0] <= stop:
            stop = max(intervals[i][1], stop)
        else:
            res.append([start, stop])
            start = intervals[i][0]
            stop = intervals[i][1]
    
    res.append([start, stop])
    return res

arr=[[1,3],[2,6],[8,10],[15,18]]
arr=[[1,4],[4,5]]
print(mergeintervals(arr))
