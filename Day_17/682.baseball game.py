class Solution:
    def calPoints(self, operations: List[str]) -> int:
        a=list()
        for i in operations:
            if i=='C':
                a.pop(-1)
                continue
            if i=='D':
                 a.append(2*a[-1])
                 continue
            if i=='+':
              a.append(a[-1]+a[-2])
              continue
            else:
                a.append(int(i))
        return sum(a)


