class Solution:
    def strStr(self, x: str, y: str) -> int:
        if y not in x:
            return -1
        else:
            return x.index(y)