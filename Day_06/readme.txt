# Happy Number Solution

## Problem:
A happy number is defined by the following process:  
1. Start with a number, replace the number by the sum of the squares of its digits.
2. Repeat the process until:
   - The number becomes 1, or
   - The number loops endlessly in a cycle that does not include 1.

If the number becomes 1, it is a happy number. Otherwise, it is not.

## Approach:
- We use a **set** to track numbers we've already seen.
- If a number repeats, it means we’re stuck in a cycle and the number is not happy.
- If we reach 1, the number is happy.

## Example:
### Input:
```python
n = 19
