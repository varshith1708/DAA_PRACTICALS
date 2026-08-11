 Heap Sort – Summary

Heap Sort is a comparison-based sorting algorithm that uses a Binary Heap data structure. For ascending order, a Max Heap is created.

Working:

1. Build a Max Heap from the array.
2. Swap the root (largest element) with the last element.
3. Reduce the heap size.
4. Apply Heapify to restore the heap property.
5. Repeat until the array is completely sorted.

 Complexity:

* Best Case: O(n log n)
* Average Case: O(n log n)
* Worst Case: O(n log n)
  Space Complexity: O(1)

Conclusion

Heap Sort is an efficient and reliable sorting algorithm with **O(n log n)** time complexity in all cases. It is an **in-place algorithm** because it does not require an additional array. However, it is **not stable**. Its guaranteed worst-case performance makes it useful when predictable sorting performance is required.
