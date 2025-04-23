## `hasCycle` Function

### Purpose:
This function checks if a singly linked list has a cycle.

### Parameters:
- **head**: The head of the linked list (or `None` if the list is empty).

### Returns:
- `True` if there is a cycle.
- `False` if there is no cycle.

### How it Works:
- It uses two pointers, `slow` and `fast`. 
- `slow` moves one step at a time, while `fast` moves two steps at a time.
- If there's a cycle, the two pointers will meet. If not, `fast` will reach the end of the list.

### Example:

```python
# Example usage
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = head.next  # Creates a cycle

solution = Solution()
print(solution.hasCycle(head))  # Output: True
