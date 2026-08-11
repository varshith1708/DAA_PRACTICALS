# Heap Sort

## Summary

Heap Sort is a **comparison-based sorting algorithm** that uses a **Binary Heap** data structure. For sorting elements in ascending order, a **Max Heap** is created.

The algorithm works in the following steps:

1. Build a Max Heap from the given array.
2. Swap the root element (maximum value) with the last element.
3. Reduce the heap size by one.
4. Apply **Heapify** to restore the Max Heap property.
5. Repeat the process until all elements are sorted.

### Time Complexity

* **Best Case:** O(n log n)
* **Average Case:** O(n log n)
* **Worst Case:** O(n log n)

### Space Complexity

* **O(1)** auxiliary space

### Key Features

* In-place sorting algorithm
* Not a stable sorting algorithm
* Uses a Binary Heap
* Provides guaranteed O(n log n) worst-case performance

## Conclusion

Heap Sort is an efficient sorting algorithm that provides **O(n log n)** time complexity in all cases. It does not require extra memory for another array, making it an **in-place sorting algorithm**. Although it is not stable and may be slower than some other algorithms in practical situations, its guaranteed worst-case performance makes it useful when predictable performance is required.
