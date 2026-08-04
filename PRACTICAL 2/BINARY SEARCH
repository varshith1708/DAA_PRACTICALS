import time

n = int(input("Enter the number of elements: "))

arr = []
print("Enter the elements in sorted order:")
for i in range(n):
    arr.append(int(input()))

key = int(input("Enter the element to search: "))

start_time = time.perf_counter()

low = 0
high = n - 1
position = -1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == key:
        position = mid
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

end_time = time.perf_counter()

if position != -1:
    print(f"Element found at index: {position}")
else:
    print("Element not found.")

print(f"Execution Time: {(end_time - start_time):.10f} seconds")
print("\nTime Complexity:")
print("Best Case    : O(1)")
print("Average Case : O(log n)")
print("Worst Case   : O(log n)")

print("\nSpace Complexity: O(1)")
