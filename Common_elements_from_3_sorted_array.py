18.Common elements from 3 sorted array

#Approach1
def commonelements(a,b,c,n1,n2,n3):
    temp=[]
    i=0
    j=0
    k=0
    while (i<n1 and j<n2 and k<n3):
        if a[i]==b[j] and b[j]==c[k]:
            temp.append(a[i])
            i+=1
            j+=1
            k+=1
        elif(a[i]<b[j]):
            i+=1
        elif (b[j]<c[k]):
            j+=1
        else:
            k+=1
    return temp

#Approach 2
def commonelements(a,b,c,n1,n2,n3):
    s = set(a)
    st = set(b)
    sr = set(c)
    a = s.intersection(st)
    c = sr.intersection(a)
    return sorted(list(c))

a=[1,5,10,20,40,80]
b=[6,7,20,80,100]
c=[3,4,15,20,30,70,80,120]
n1=len(a)
n2=len(b)
n3=len(c)
commonelements(a,b,c,n1,n2,n3)
