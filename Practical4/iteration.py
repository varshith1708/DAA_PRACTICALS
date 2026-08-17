import time

n = int(input("Enter number of elements: "))

arr = []

print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

start = time.time()

# Iteration
for i in range(n - 1):
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

end = time.time()

print("Sorted array:", arr)

execution_time = end - start
print("Execution Time:", execution_time, "seconds")

print("Time Complexity: O(n^2)")
