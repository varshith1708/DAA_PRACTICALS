import time

# Heapify function
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Check left child
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check right child
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not the root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        # Recursively heapify the affected subtree
        heapify(arr, n, largest)


# Heap Sort function
def heap_sort(arr):
    n = len(arr)

    # Build Max Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


# User input
n = int(input("Enter the number of elements: "))

arr = list(map(int, input("Enter the elements: ").split()))

# Start execution time
start = time.perf_counter()

heap_sort(arr)

# End execution time
end = time.perf_counter()

# Output
print("Sorted array:", arr)

execution_time = end - start
print("Execution time:", execution_time, "seconds")

# Time Complexity:
# Best Case    : O(n log n)
# Average Case : O(n log n)
# Worst Case   : O(n log n)

# Space Complexity: O(log n)
