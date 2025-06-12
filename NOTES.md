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
