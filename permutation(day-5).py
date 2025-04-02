'arr=list(map(int,input("enter the array:").split()))'
def next_permutation(arr):
    #find the pivot
    pivot=-1
    for i in range(len(arr)-2,-1,-1):
        if arr[i] < arr[i+1]:
            pivot=i
            break

    #if pivot is not found, then reverse whole array
    if pivot==-1:
        arr.reverse()
        return

    #find the right element from right that is greater than pivot
    for i in range(len(arr)-1,pivot,-1):
        if arr[i] > arr[pivot]:
            arr[i],arr[pivot] = arr[pivot],arr[i]
            break
    #reverse the element from pivot +1 to the end in place
    l,r=pivot+1,len(arr)-1
    while l<r:
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
        r-=1

arr=[2,4,1,7,5,0]
next_permutation(arr)
print(" ".join(map(str,arr)))