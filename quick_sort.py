# Quicksort is a sorting algorithm based on the divide and conquer approach where

# An array is divided into subarrays by selecting a pivot element (element selected from the array).

# While dividing the array, the pivot element should be positioned in such a way 
# that elements less than pivot are kept on the left side and elements greater than pivot are on the right side of the pivot.

# The left and right subarrays are also divided using the same approach. 
# This process continues until each subarray contains a single element.

# At this point, elements are already sorted. Finally, 
# elements are combined to form a sorted array.



# Quick Sort Algorithm

# quickSort(array, leftmostIndex, rightmostIndex)
#   if (leftmostIndex < rightmostIndex)
#     pivotIndex <- partition(array,leftmostIndex, rightmostIndex)
#     quickSort(array, leftmostIndex, pivotIndex - 1)
#     quickSort(array, pivotIndex, rightmostIndex)

# partition(array, leftmostIndex, rightmostIndex)
#   set rightmostIndex as pivotIndex
#   storeIndex <- leftmostIndex - 1
#   for i <- leftmostIndex + 1 to rightmostIndex
#   if element[i] < pivotElement
#     swap element[i] and element[storeIndex]
#     storeIndex++
#   swap pivotElement and element[storeIndex+1]
# return storeIndex + 1


def quick_sort(sequence):
    length = len(sequence)
    # Base case: if the sequence has 1 or fewer elements, it's already sorted
    if length <= 1:
        return sequence
    else:
        # Choose the last element as the pivot
        pivot = sequence.pop()

    # Initialize lists to hold elements greater than and less than the pivot
    items_greater = []
    items_lower = []

    # Iterate through the sequence, comparing each element to the pivot
    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    # Recursively apply quick sort to the elements less than the pivot
    # Concatenate the sorted lower elements, pivot, and sorted greater elements
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

# Example usage:
print(quick_sort([5,6,3,0,9,7,5,2,4,2,1,6,7,8,2]))


# Time Complexity
# Best          O(n*log n)
# Worst         O(n^2)
# Average       O(n*log n)

# Space Complexity  O(log n)