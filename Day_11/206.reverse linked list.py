class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=list(set(nums))
        nums.sort()
        c=1
        m=1
        if nums==[]:
            return 0
        for i in range(len(nums)):
            if(i+1>=len(nums)):
                break
            if(nums[i+1]==(nums[i]+1)):
                c+=1
                if(c>=m):
                    m=c
            else:
                c=1
            
        return m
