class Solution:
    def numJewelsInStones(self, x: str, y: str) -> int:
        c=0
        for i in list(x):
            c+=y.count(i)
        return c