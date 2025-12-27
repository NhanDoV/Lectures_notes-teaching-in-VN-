# All of Sorting Algorithms

This document summarizes common sorting algorithms, their core ideas,
time/space complexity, and key properties.
Implementation scripts will be discussed separately.

---

## 1. Quick Sort
[x] Comparison-based  
[x] Divide and Conquer  
[x] In-place (typical implementation)  
[x] Not stable  

**Idea**  
- Choose a pivot
- Partition the array into elements smaller and larger than the pivot
- Recursively sort subarrays

**Time Complexity**
- Best / Average: O(n log n)
- Worst: O(n²) (bad pivot choice)

**Space Complexity**
- O(log n) (recursion stack)

---

## 2. Merge Sort
[x] Comparison-based  
[x] Divide and Conquer  
[x] Stable  
[x] Not in-place  

**Idea**  
- Split array into halves
- Recursively sort each half
- Merge sorted halves

**Time Complexity**
- Best / Average / Worst: O(n log n)

**Space Complexity**
- O(n)

---

## 3. Tim Sort
[x] Comparison-based  
[x] Hybrid (Merge Sort + Insertion Sort)  
[x] Stable  
[x] Adaptive  

**Idea**  
- Detect natural runs in data
- Use insertion sort for small runs
- Merge runs efficiently

**Used in**
- Python `sorted()`
- Python `list.sort()`
- Java `Arrays.sort()` (objects)

**Time Complexity**
- Best: O(n)
- Average / Worst: O(n log n)

**Space Complexity**
- O(n)

---

## 4. Swap Sort (Exchange Sort)
[x] Comparison-based  
[x] In-place  
[x] Not stable  
[x] Simple / Naive  

**Idea**  
- Compare every pair `(i, j)` where `j > i`
- Swap immediately if elements are out of order
- No minimum index tracking

**Characteristics**
- Swaps happen frequently
- Simple but inefficient
- Often used for learning purposes

**Time Complexity**
- Best / Average / Worst: O(n²)

**Space Complexity**
- O(1)

**Note**  
- Similar to Selection Sort but differs in that swaps happen immediately
- Sometimes called *Exchange Sort* in older textbooks

---

## 5. Selection Sort
[x] Comparison-based  
[x] In-place  
[x] Not stable  

**Idea**  
- Find the minimum element
- Swap it with the first unsorted position
- Repeat for the rest of the array

**Time Complexity**
- Best / Average / Worst: O(n²)

**Space Complexity**
- O(1)

---

## 6. Bubble Sort
[x] Comparison-based  
[x] In-place  
[x] Stable  

**Idea**  
- Repeatedly swap adjacent elements if they are in wrong order
- Largest elements "bubble" to the end

**Time Complexity**
- Best: O(n) (already sorted with optimization)
- Average / Worst: O(n²)

**Space Complexity**
- O(1)

---

## 7. Insertion Sort
[x] Comparison-based  
[x] In-place  
[x] Stable  

**Idea**  
- Build sorted array one element at a time
- Insert each element into its correct position

**Time Complexity**
- Best: O(n)
- Average / Worst: O(n²)

**Space Complexity**
- O(1)

---

## 8. Heap Sort
[x] Comparison-based  
[x] In-place  
[x] Not stable  

**Idea**  
- Build a max heap
- Repeatedly extract the maximum element

**Time Complexity**
- Best / Average / Worst: O(n log n)

**Space Complexity**
- O(1)

---

## 9. Counting Sort
[x] Non-comparison-based  
[x] Stable (if implemented properly)  

**Idea**  
- Count frequency of each value
- Compute prefix sums
- Place elements into correct position

**Time Complexity**
- O(n + k), where k = range of values

**Space Complexity**
- O(n + k)

---

## 10. Radix Sort
[x] Non-comparison-based  
[x] Stable  

**Idea**  
- Sort numbers digit by digit
- Uses a stable sub-sorting algorithm (often Counting Sort)

**Time Complexity**
- O(d × (n + k))

**Space Complexity**
- O(n + k)

---

## Notes
- Comparison-based sorting has a lower bound of O(n log n)
- Non-comparison-based sorting breaks this bound using assumptions on data
- Real-world systems usually use hybrid algorithms (e.g., Tim Sort)