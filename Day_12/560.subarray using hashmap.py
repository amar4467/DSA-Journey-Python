class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        s=0
        total=0
        d=defaultdict(int)
        d[0]=1
        for i in nums:
            s+=i
            total+=d[s-k]
            d[s]+=1
        return s
