import time

n = int(input("Enter the number of elements: "))

arr = []
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

key = int(input("Enter the element to search: "))

start_time = time.perf_counter()

position = -1
for i in range(n):
    if arr[i] == key:
        position = i
        break

end_time = time.perf_counter()
if position != -1:
    print(f"Element found at index: {position}")
else:
    print("Element not found.")

print(f"Execution Time: {(end_time - start_time):.10f} seconds")
print("\nTime Complexity:")
print("Best Case    : O(1)")
print("Average Case : O(n)")
print("Worst Case   : O(n)")

print("\nSpace Complexity: O(1)")
