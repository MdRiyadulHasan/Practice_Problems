class Solution:
	def longestOnes(self, nums, k: int) -> int:
		dct = {0:0,1:0}
		l=0
		maxlength = 0
		for r,n in enumerate(nums):
			dct[n]+=1
			while dct[0]>k:
				dct[nums[l]]-=1
				l+=1
			maxlength=max(maxlength,r-l+1)
		return maxlength
if __name__ == '__main__':
    nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    k=3
    ob = Solution()
    ans = ob.longestOnes(nums,k)
    print(ans)
	