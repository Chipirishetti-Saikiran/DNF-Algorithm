# DNF-Algorithm

The **DNF (Dutch National Flag) Algorithm** is a popular algorithmic technique used to sort arrays containing three distinct elements, such as 0s, 1s, and 2s, in linear time and constant space. It was proposed by **Edsger Dijkstra** to solve the problem of sorting an array into three groups, analogous to the Dutch national flag's three color bands.

---

### Problem Statement
Given an array of \( n \) elements containing only three distinct elements (e.g., 0, 1, and 2), sort the array so that:
- All 0s come first,
- All 1s come next,
- All 2s come last.

The solution must be:
1. **In-place** (constant space).
2. **Linear time** (\( O(n) \)).

---

### Approach
The DNF algorithm uses three pointers:
1. **low**: Tracks the position where the next 0 should be placed.
2. **mid**: Traverses the array to examine elements.
3. **high**: Tracks the position where the next 2 should be placed.

The algorithm iterates through the array, partitioning it into three sections:
- Elements from index `0` to `low-1` are 0s.
- Elements from index `low` to `mid-1` are 1s.
- Elements from index `high+1` to `n-1` are 2s.

#### Steps:
1. Initialize `low = 0`, `mid = 0`, and `high = n-1`.
2. Traverse the array while `mid <= high`:
   - If the current element is 0: Swap it with the element at `low`, then increment both `low` and `mid`.
   - If the current element is 1: Just increment `mid`.
   - If the current element is 2: Swap it with the element at `high` and decrement `high`.

---

### Implementation (Python)
```python
def dutch_national_flag(arr):
    low, mid, high = 0, 0, len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr

# Example
arr = [2, 0, 2, 1, 1, 0]
sorted_arr = dutch_national_flag(arr)
print(sorted_arr)  # Output: [0, 0, 1, 1, 2, 2]
```

---

### Dry Run Example
For \( arr = [2, 0, 2, 1, 1, 0] \):

| Step | low | mid | high | Array State          | Action         |
|------|-----|-----|------|----------------------|----------------|
| 1    | 0   | 0   | 5    | [2, 0, 2, 1, 1, 0]   | Swap `2` and `0` |
| 2    | 0   | 0   | 4    | [0, 0, 2, 1, 1, 2]   | Swap `0` and `0` |
| 3    | 1   | 1   | 4    | [0, 0, 2, 1, 1, 2]   | Increment `low` and `mid` |
| 4    | 2   | 2   | 4    | [0, 0, 2, 1, 1, 2]   | Swap `2` and `1` |
| 5    | 2   | 2   | 3    | [0, 0, 1, 1, 2, 2]   | Increment `mid` |
| 6    | 2   | 3   | 3    | [0, 0, 1, 1, 2, 2]   | Done           |

---

### Time and Space Complexity
- **Time Complexity:** \( O(n) \)
  - Each element is processed at most once.
- **Space Complexity:** \( O(1) \)
  - No additional space is used beyond the pointers.

---

### Applications
1. Sorting colors in an array (e.g., red, white, blue as 0, 1, 2).
2. Segregating binary arrays (0s and 1s).
3. Partitioning arrays based on conditions (e.g., negatives, zeros, positives).
4. Quick Sort's partitioning step.

Let me know if you'd like more examples or variations of this algorithm!
