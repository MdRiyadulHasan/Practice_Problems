class Solution:
	def characterReplacement(self, s: str, k: int) -> int:
		dct = {}
		res = 0
		l = 0
		freq = 0
		for r,c in enumerate(s):
			dct[c] = dct.get(c, 0)+1
			freq = max(freq, dct[c])
			while (r - l + 1) - freq> k:
				dct[s[l]] -= 1
				l += 1
			res = max(res, r - l + 1)
		return res
if __name__=='__main__': 
    s = 'AABBBAABA'
    k=2
    ob = Solution()
    ans = ob.characterReplacement(s,k)
    print(ans)