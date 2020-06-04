def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    low = 0
    middle_index = 0
    high = len(arr) - 1
    # Your code here
    while low <= high:
        middle_index = (high + low)//2

        if arr[middle_index] < target:
            low = middle_index + 1
        elif arr[middle_index] > target:
            high = middle_index - 1
        else:
            return middle_index

    return -1  # not found
