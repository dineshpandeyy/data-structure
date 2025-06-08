---
## 🧠 What is the **Difference Array Technique**?

The **Difference Array Technique** is a powerful method to **efficiently perform multiple range update operations** on an array.

Instead of updating every element in a range one by one (which takes O(n) per operation), we update the difference array, which takes **O(1)** time per operation.
---

## 📚 How It Works

### Original Array:

Let’s say you have an array `A` of size `n`.

Create a **difference array** `D` of size `n`:

- `D[0] = A[0]`
- `D[i] = A[i] - A[i-1]` for all `i` from 1 to `n-1`

To perform a **range update** (i.e., add `val` to all elements in range `[l, r]`):

```python
D[l] += val
if r + 1 < n:
    D[r + 1] -= val
```

After all updates, to get the final array, compute the **prefix sum** of `D`.

---

## 🧪 Example

Let `A = [0, 0, 0, 0, 0]`

### Update: add 10 to range [1, 3]

```python
D[1] += 10
D[4] -= 10
```

### Final step: prefix sum of D gives the updated array

Result: `A = [0, 10, 10, 10, 0]`

---

## ✅ When to Use Difference Array Technique

Use it when:

1. ✅ You have to do **multiple range updates** (e.g., +val to subarrays).
2. ✅ Your array is **large** (e.g., up to 1e5 or more), and you want **fast updates**.
3. ✅ You want to reduce time complexity from **O(n) per update** to **O(1) per update**.

---

## ⏱️ Time Complexity

| Operation         | Time              |
| ----------------- | ----------------- |
| One range update  | O(1)              |
| Final array build | O(n) (prefix sum) |

---

## 🧩 Bonus: Works for Subtraction and Multiple Queries Too!

You can subtract by just using negative values, and you can do many queries before building the final array once.

---
