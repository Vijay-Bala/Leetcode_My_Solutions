class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        x=list(zip(*s))
        y=""
        for i in x:
            if len(set(i))==1:
                y=y+i[0]
            else:
                break
        return y