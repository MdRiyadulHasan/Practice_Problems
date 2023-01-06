class Solution:
    def maxPower(self, s: str) -> int:
        maxlength =1
        l=0
        for r in range(1,len(s)):
            if s[r]==s[r-1]:
                maxlength= max(maxlength,r-l+1)
            else:
                l=r
        return maxlength