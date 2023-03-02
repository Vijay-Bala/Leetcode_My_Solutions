class Solution:
    def twoSum(self, x: List[int], a: int) -> List[int]:
        l=[]
        f=0
        for i in range(len(x)-1):
            t=x[i]
            for j in range(i+1,len(x)):
                if t+x[j]==a:
                    l.append(i)
                    l.append(j)
                    f=1
                if f==1:
                    break
            if f==1:
                break
        return l
