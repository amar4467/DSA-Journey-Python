class Solution:
    def maxProfit(self, p: List[int]) -> int:
        ma=0
        k=float('inf')
        for i in (p):
            k=min(k,i)
            x=i-k
            ma=max(x,ma)
        return ma