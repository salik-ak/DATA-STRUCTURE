def mergesort(list):
    if len(list) > 1:
        mid = len(list)//2
        left = list[:mid]
        right = list[mid:]
        mergesort(left)
        mergesort(right)
        i=0
        j=0
        k=0
        while i<len(left) and j<len(right):
              
            if left[i]<right[j]:
                list[k] = left[i]
                i = i+1
                k = k+1
            else:
                list[k] = right[j]
                j = j+1
                k = k+1
        while i<len(left):
            list[k] = left[i]
            i=i+1
            k=k+1
        while j<len(right):
            list[k] = right[j]
            j=j+1
            k=k+1   
    
    return list




list = [2,9,7,6,4,8,1,3]
print(list)
print(mergesort(list))

def insertionsort(mylist):
    for i in range(1,len(mylist)):
        current_element = mylist[i]
        pos = i
        while current_element < mylist[pos-1] and pos>0:
            mylist[pos] = mylist[pos-1]
            pos = pos-1
        mylist[pos] = current_element
list1 = [2,5,8,9,3,2,1]
print(list1)
insertionsort(list1)
print(list1)