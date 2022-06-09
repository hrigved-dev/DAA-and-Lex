# Python3 implementation of QuickSort
# Function to find the partition position
def partition(array, low, high):
    pivot = array[high]
# Pointer for greater element
    i = low - 1
# Traverse through all elements
# compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

# Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

# Return the position from where partition is done
    return i + 1

# Function to perform quicksort
def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)


		
# Driver code
array = [ 10, 7, 8, 9, 1, 5]
quick_sort(array, 0, len(array) - 1)

print(f'Sorted array: {array}')
	
# This code is contributed by Adnan Aliakbar
