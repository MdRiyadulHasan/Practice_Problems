class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dct = {}
        l=0
        maxlength=0
        for r,c in enumerate(s):
            if c in dct and l<=dct[c]:
                l=dct[c]+1  
            else:
                maxlength=max(maxlength,r-l+1)
            dct[c]=r
        return maxlength

if __name__ == '__main__':
    s='abcabcdefdbacag'
    ob = Solution()
    ans = ob.lengthOfLongestSubstring(s)
    print(ans)