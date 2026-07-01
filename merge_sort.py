# 2. Merge Sort: Problem State
# Implement Merge Sort to sort: [214,12,46,57,31,8]
# Expected Output: [8,12,31,46,57,214]

def merge_sort(arr):
    # This code helps continue splitting the array until each sub-array has only one element.
    if len(arr) > 1:

        # These codes find the middle index and split the array into left and right halves.
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # These codes recursively sort both halves.
        merge_sort(left)
        merge_sort(right)

        # This code initialize pointers.
        i = j = k = 0

        # Compare the elements from both halves, then merge them.
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Copy any remaining element from the left half.
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        # Copy any remaining element from the right half.
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

# Original Array
arr = [214, 12, 46, 57, 31, 8]

# This function calls the Merge Sort function.
merge_sort(arr)

# This code displays the sorted array as an output.
print("Merge Sort:", arr)