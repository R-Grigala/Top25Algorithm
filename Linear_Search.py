# Linear search is a sequential searching algorithm where we start from one end and check 
# every element of the list until the desired element is found. 
# It is the simplest searching algorithm.

# How Linear Search Works?
# The following steps are followed to search for an element k = 1 in the list below.


# 1. Start from the first element, compare k with each element x.

# 2. If x == k, return the index.

# 3. Else, return not found.

# Linear Search Algorithm
# LinearSearch(array, key)
#   for each item in the array
#     if item == value
#       return its index


# Linear Search in Python

def linearSearch(array, n, x):

    # Going through array sequencially
    for i in range(0, n):
        if (array[i] == x):
            return i
    return -1

array = [2, 4, 0, 1, 9]
x = 1
n = len(array)
result = linearSearch(array, n, x)
if(result == -1):
    print("Element not found")
else:
    print("Element found at index: ", result)


# Linear Search Complexities
# Time Complexity: O(n)

# Space Complexity: O(1)