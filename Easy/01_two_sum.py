class Solution:
    def twoSum(self, nums, target: int):
        hasmap = {}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in hasmap:
                return [hasmap[diff],i]
            hasmap[n]=i
if __name__=='__main__':
    nums = [2,5,7,11,15]
    target = 9
    ob = Solution()
    ans = ob.twoSum(nums,target)
    print(ans)