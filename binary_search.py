# 4. Binary Search: Problem Statement
# Use Binary Search, find 31 in: [8,12,31,46,57,214]
# Return the index.
# Expected Output: Found at index 2

def binary_search(arr, target):

    # These codes set the initial search boundaries
    left = 0
    right = len(arr) - 1

    # This while function continues searching while the search range is valid.
    while left <= right:

        # This code finds the middle index.
        mid = (left + right) // 2

        # The target is found if this code is triggered.
        if arr[mid] == target:
            return mid

        # The right half is searched if this code is triggered.
        elif arr[mid] < target:
            left = mid + 1

        # The left half is searched if this code is triggered.
        else:
            right = mid - 1

    # The target is not found if this code is triggered.
    return - 1

arr = [8,12,31,46,57,214]
result = binary_search(arr,31)

if result != -1:
    print(f"Target found at index", result)
else:
    print("Not found")