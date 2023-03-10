class Solution:
    def addDigits(self, n: int) -> int:
        while True:
            s=0
            while n!=0:
                s+=n%10
                n//=10
            if s<10:
                return s
            n=s