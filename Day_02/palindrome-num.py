class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        og=x
        rev=0
        while x>0:
            r=int(x%10)
            rev=(rev*10)+r
            x//=10
        return og==rev