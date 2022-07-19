#6.Find the union and intersection of two sorted arrays

def unionarray(arr1,arr2):
    #with the use of built in extend method we have combined both the arrays
    # alternatively we can append each element into another array 
    print("Before extension")
    print('Array1: ',arr1)
    arr1.extend(arr2)
    print("After extension")
    print(arr1)
    #After combining both the array now the task is to sort the array
    for i in range(0,len(arr1)):
        for j in range(i+1,len(arr1)):
            if arr1[i]>arr1[j]:
                arr1[i],arr1[j]=arr1[j],arr1[i]
    #After sorting the arr1 we have return the array
    print("The union of two array")
    return arr1

def intersectionarray(arr1,arr2):
    #For sorting the array1
    for i in range(0,len(arr1)):
        for j in range(i+1,len(arr1)):
            if arr1[i]>arr1[j]:
                arr1[i],arr1[j]=arr1[j],arr1[i]
    #For sorting the array2
    for i in range(0,len(arr2)):
        for j in range(i+1,len(arr2)):
            if arr2[i]>arr2[j]:
                arr2[i],arr2[j]=arr2[j],arr2[i]

    #Now finding the intersecition(common elements between the two arrays)
    # We'll be creating a emplty array for appending the comment elements of two arrays into new array 
    temp=[]
    for i in range(0,len(arr1)):
        for j in range(0,len(arr2)):
            if arr1[i]==arr2[j]:
                print(arr1[i],arr2[j])
                temp.append(i)
    #Returning the intersected elements from both array
    return list(temp)
    

arr1=[0,8,1,3,4,7,2]
arr2=[11,0,4,54,6]
unionarray(arr1,arr2)
intersectionarray(arr1,arr2)
