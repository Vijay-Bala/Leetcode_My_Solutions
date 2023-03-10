class Solution:
    def generate(self, n: int) -> List[List[int]]:
        x=[]
        for i in range(n):
            t=[]
            for j in range(i+1):
                if j==0 or j==i:
                    t.append(1)
                else:
                    t.append(x[i-1][j]+x[i-1][j-1])
            x.append(t)
        return x