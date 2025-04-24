class Solution:
    def minFlips(self, s: str) -> int:
        n=len(s)
        d=s+s
        k=""
        j=""
        for i in range(1,(2*n)+1):
            j+=str(i%2)
        for i in range(0,n*2):
            k+=str(i%2)
        dk=dj=0
        result=float('inf')
        l=0
        for i in range(0,2*n):
            if(d[i]!=k[i]):
                dk+=1
            if(d[i]!=j[i]):
                dj+=1
            if((i-l+1)>n):
                if(d[l]!=k[l]):
                    dk-=1
                if(d[l]!=j[l]):
                    dj-=1
                l+=1
            if(i-l+1==n):
                result=min(result,dj,dk)
        return result