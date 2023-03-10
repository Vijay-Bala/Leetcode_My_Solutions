class Solution:
    def isHappy(self, n: int) -> bool:
        while True:
            s=0
            while n!=0:
                s+=(n%10)**2
                n//=10
            if s==1:
                return True
            elif s==4:
                return False
            n=s