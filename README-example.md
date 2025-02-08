# LeetCode Solutions

This repository contains my solutions to LeetCode problems, organised by category.

## 📂 Structure

- `arrays/` → Array problems.
- `linked_lists/` → Linked list problems.
- `dynamic_programming/` → PD and optimisation problems.
- `graphs/` → Graph search problems.

## 📌 Progress

- ✅ Two Sum (`arrays/two_sum.py`)
- ⏳ Longest Palindromic Substring (`dynamic_programming/longest_palindromic_substring.py`)

## 🚀 How to use this repo

You can clone the repository and test the solutions:

```bash
git clone https://github.com/fnt/leetcode-solutions.git
cd leetcode-solutions
python arrays/two_sum.py
```

### 📌 Automated tests

Example of test for `two_sum.py` with `pytest`.

```python
from arrays.two_sum import twoSum

def test_two_sum():
    assert twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert twoSum([3, 2, 4], 6) == [1, 2]
    assert twoSum([3, 3], 6) == [0, 1]
```

To run tests:

```bash
pytest tests/
```