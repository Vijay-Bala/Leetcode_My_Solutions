class Solution:
    def removeDuplicates(self, x: List[int]) -> int:
        x[:] = sorted(set(x))
        return len(x)