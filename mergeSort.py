# Merge Sort
def mergeSort(array):
    if len(array) > 1:
        mid = len(array)//2
        left = array[:mid]
        right = array[mid:]
        mergeSort(left)
        mergeSort(right)

        i=j=k=0

        while i<len(left) and j<len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i = i + 1
            else:
                array[k] = right[j]
                j = j + 1
            k = k + 1

        while i < len(left):
            array[k] = left[i]
            i = i + 1
            k = k + 1
        
        while j < len(right):
            array[k] = right[j]
            j = j + 1
            k = k + 1

array = [12, 11, 13, 5, 6, 7]
mergeSort(array)
print(f"Sorted array is: {array}")