def quicksort(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for i in range (1,len(arr)):
            if arr[i]<pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        return quicksort(left)+[pivot]+quicksort(right)
    
arr =[12,43,54,11,34,56]
sortedarray=quicksort(arr)
print(sortedarray)
