class Solution:
    def findMedianSortedArrays(self, x: List[int], y: List[int]) -> float:
        t=len(x)+len(y)
        z=[]
        a=0.0
        z=x+y
        z=sorted(z)
        t=len(z)
        if t%2!=0:
            a=z[t//2]*1.0
        else:
            a=(z[t//2]+z[t//2-1])/2*1.0
        return a