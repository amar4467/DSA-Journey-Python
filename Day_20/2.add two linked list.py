class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a=0
        b=0
        current=l1
        multiplier = 1
        while current:
            a += current.val * multiplier
            multiplier *= 10
            current = current.next
        current=l2
        multiplier = 1
        while current:
            b += current.val * multiplier
            multiplier *= 10
            current = current.next
        a+=b
        d=ListNode(0)
        current=d
        for i in str(a)[::-1]:
            current.next=ListNode(int(i))
            current=current.next
        return d.next