class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        dct = {0:0,1:0}
        l=0
        maxlength = 0
        for r,n in enumerate(nums):
            dct[n]+=1
            while dct[0]>1:
                dct[nums[l]]-=1
                l+=1
            maxlength=max(maxlength,r-l+1)
        return maxlength