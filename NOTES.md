# Circular Array - Quick Reference

## Core Concept
- Last element connects to first element
- Use `(i + 1) % n` for circular wrapping
- Always track array length `n`

## Common Solutions

### 1. Max Absolute Difference
```python
def max_abs_diff(nums):
    n = len(nums)
    return max(abs(nums[i] - nums[(i + 1) % n]) for i in range(n))
```

### 2. Circular Traversal
```python
def circular_traverse(nums, start):
    n = len(nums)
    for i in range(n):
        idx = (start + i) % n
        # Process nums[idx]
```

## Key Tips
1. Use modulo for wrapping: `(i ± k) % n`
2. Handle negative indices: `((i - k) % n + n) % n`
3. Check edge cases: empty array, single element
4. Test with small arrays first

# Sorting Lists of Lists in Python

## Basic Sorting
```python
# Sort by first element (index 0)
arr = [[1,5], [1,4], [1,2]]
arr.sort(key=lambda x: x[0])  # [[1,5], [1,4], [1,2]] (stable sort)

# Sort by second element (index 1)
arr.sort(key=lambda x: x[1])  # [[1,2], [1,4], [1,5]]
```

## Multiple Keys
```python
# Sort by first element, then second element
arr.sort(key=lambda x: (x[0], x[1]))  # [[1,2], [1,4], [1,5]]

# Sort by first element descending, then second element ascending
arr.sort(key=lambda x: (-x[0], x[1]))  # [[1,2], [1,4], [1,5]]
```

## Descending Order Sorting
```python
# Sort by first element in descending order
arr = [[5, 0], [1, 1], [3, 2]]
arr.sort(key=lambda x: -x[0])  # [[5, 0], [3, 2], [1, 1]]
```

### Why `-x[0]` works for descending order:
- Python's `sort()` sorts in **ascending** order by default
- `-x[0]` negates the value for sorting, making larger numbers appear first
- The **original values in `arr` remain unchanged**
- This is a common trick to sort in descending order

### Example:
```python
nums = [5, 1, 3]
arr = [[5, 0], [1, 1], [3, 2]]

# Sorting with -x[0]:
arr.sort(key=lambda x: -x[0])
# Result: [[5, 0], [3, 2], [1, 1]]
# Original values unchanged, just sorted differently
```

## Key Points
1. `sort()` modifies list in-place
2. `sorted()` returns new sorted list
3. Stable sort preserves original order for equal elements
4. Use negative values for descending order
5. Multiple keys can be combined in tuple
6. `-x[0]` is a trick for descending order - doesn't change original values
