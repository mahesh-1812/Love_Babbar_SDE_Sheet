#Chocolate distribution problem
import sys 

def findMindiff(A,N,M):
    A.sort()
    i,j = 0,M-1
    ans = sys.maxsize
    while j<N:
        ans = min(ans,A[j]-A[i])
        i+= 1
        j+= 1
    return ans

A=[3,4,1,9,56,7,9,12]
N=len(A)
M=5
findMindiff(A,N,M)
