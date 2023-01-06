class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        l=0
        maxlength = 0
        for r,n in enumerate(nums):
            if n==1:
                maxlength=max(maxlength,r-l+1)
            else:
                l=r+1
        return maxlength
if __name__ =='__main__':
    nums=[1,1,0,1,1,1]
    ob= Solution()
    ans = ob.findMaxConsecutiveOnes(nums)
    print(ans)
