class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        current=head
        a=list()
        while current:
            a.append(current.val)
            current=current.next
        b=a[::-1]
        if(b==a):
            return True
        else:
            return False