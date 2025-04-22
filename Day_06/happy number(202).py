class Solution:
    def isHappy(self, n: int) -> bool:
        a=set()
        s=int(0)
        while(1):
            s=0
            while(n>0):
                s=s+(n%10)**2
                n//=10
            n=s
            if s in a:
                return False
            a.add(s)
            if(s==1):
                return True

        