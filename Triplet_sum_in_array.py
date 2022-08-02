#Triplet sum in an array

#Brute force
def find3sum(A,n,X):
    for i in range(0,n):
        res=A[i]+A[i+1]
        for j in range(i+2,n):
            res=res+A[j]
            if res==X:
                return 1
            else:
                return 0

              
#Approach 2
def find3Numbers(A, n, X):
    arr=A
    arr.sort()
    for i in range(n):
        l=i+1
        r=n-1
        while l<r:
            if arr[i]+arr[l]+arr[r]==X:
                return True
            elif arr[i]+arr[l]+arr[r]<X:
                l=l+1
            else:
                r=r-1
        return False


A=[1,4,45,6,10,8]
n=len(A)-1
X=13
find3Numbers(A,n,X)
