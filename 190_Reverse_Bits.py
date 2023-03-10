class Solution:
    def reverseBits(self, n: int) -> int:
        x=n
        c=0
        s=""
        while c!=32:
            if x%2==0:
                s+="0"
            else:
                s+="1"
            x//=2
            c+=1
        v=0
        t=1
        for i in list(s)[::-1]:
            v+=int(i)*t
            t*=2
        return v