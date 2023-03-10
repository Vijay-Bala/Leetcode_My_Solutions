class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            t=x
            s=0
            while t!=0:
                s*=10
                s+=t%10
                t//=10
            if s==x:
                return True
            else:
                return False