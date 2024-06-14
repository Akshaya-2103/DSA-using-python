def merge_sort(arr):
    if len(arr) > 1:
        #Divide the array into two halves
        mid = len(arr)//2
        left_half = arr[:mid]
        right_half = arr[mid:]

        #Recursive call on each half
        merge_sort(left_half)
        merge_sort(right_half)

        #Merge the sorted halves
        merge(arr, left_half, right_half)

def merge(arr, left, right):
    i = j = k = 0

    #Compare and merge the elements from left and right halves
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1

        else:
            arr[k] = right[j]
            j += 1
        k += 1
    
    #If there are any remaining elements in left or right halves, add them to the merged array
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

li = list(map(int,input().split()))
print("Original list: ",li)
merge_sort(li)
print("Sorted list: ",li)