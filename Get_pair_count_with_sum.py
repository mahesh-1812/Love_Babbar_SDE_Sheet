#17.count pair with given sum


#Brute force approach1
def getpaircount(arr,n,k):
    count=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            sum=arr[i]+arr[j]
            if sum==k:
                count+=1
    return count

#Approach 2

def getpaircount1(arr,n,k):
    count=0
    seen={}      
    for i in arr:
        c=k-i
        if c in seen:
            count+=seen[c]
        seen[i]=seen.get(i,0)+1
                
    return count
arr=[1,1,1,1]
n=len(arr)
k=2
getpaircount1(arr,n,k)
