# 3. Quick Sort: Problem State
# Implement Quick Sort to sort: [214,12,46,57,31,8]
# Expected Output: [8,12,31,46,57,214]

# This class continue sorting if there's more than one element.
def quick_sort(arr, low, high):
    if low < high:
        # First code partition the array and get the pivot position.
        pivot_index = partition(arr, low, high)

        # Second code recursively sort the left sub-array.
        quick_sort(arr, low, pivot_index-1)

        # Third code recursively sort the right sub array.
        quick_sort(arr, pivot_index+1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low-1
    # First code chooses the last element as the pivot.

    # This function compares each element with the pivot.
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            # This code swap elements of arr[i] and arr[j].

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1
    # These codes place the pivot in its correct sorted position before returning the index.

# Original array
arr = [214, 12, 46, 57, 31, 8]

# This function calls the Quick Sort function.
quick_sort(arr, 0, len(arr)-1)

# This code displays the sorted array.
print("Quick Sort:", arr)