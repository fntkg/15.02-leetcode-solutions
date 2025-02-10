# 💻 LeetCode Solutions

This repository contains my solutions to LeetCode problems, organised by category.

## 📂 Structure

- `solutions/arrays/` → Array problems.

## 📊 Progress

- ✅ TwoSum (`arrays/two_sum.py`)

## 🚀 How to Use This Repo

### ✅ Automated Tests

> ⚠️ The solutions are developed following Test-Driven Development (TDD) practices.

Example of test for `two_sum.py` with `pytest`.

```python
from solutions.arrays.two_sum import twoSum


def test_two_sum():
    assert twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert twoSum([3, 2, 4], 6) == [1, 2]
    assert twoSum([3, 3], 6) == [0, 1]
```

To run tests:

```bash
pytest tests/
```