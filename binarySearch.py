# Used when array is sorted 
# and we need to find the position of a target value efficiently.

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5

result = binary_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in array")



# Used in:

# Searching in Sorted Arrays

# Finding Insertion Points

# Efficient Lookups in Databases

# Print the result of the search

