class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if len(s)<=k:
            return len(s)
        l=0
        count = 0
        maxwindow = 0
        count = 0
        dct = {}
        for r in range(len(s)):
            dct[s[r]]=dct.get(s[r],0)+1
            if dct[s[r]]==1:
                count+=1
            while count>k:
                dct[s[l]]-=1
                if dct[s[l]]==0:
                    count-=1
                l+=1
            maxwindow = max(maxwindow,r-l+1)
        return maxwindow