# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        current1=head
        l=0
        while current:
            l+=1
            current=current.next
        for i in range(l//2):
            current1=current1.next
        return current1