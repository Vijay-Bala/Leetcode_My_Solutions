class Solution:
    def getRow(self, n: int) -> List[int]:
        x=[]
        for i in range(n+1):
            t=[]
            for j in range(i+1):
                if j==0 or j==i:
                    t.append(1)
                else:
                    t.append(x[i-1][j]+x[i-1][j-1])
            x.append(t)
        return x[n]