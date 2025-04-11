class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        a=[]
        for i in range(len(arr)):
            a.append(bin(arr[i])[2:])
        return sorted(arr,key=lambda x:(bin(x).count('1'),x))
