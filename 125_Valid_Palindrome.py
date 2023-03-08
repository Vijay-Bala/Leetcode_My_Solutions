class Solution:
    def isPalindrome(self, s: str) -> bool:
        x=[]
        for i in s.lower():
            if i.isalnum():
                x.append(i)
        if x==x[::-1]:
            return True
        else:
            return False
