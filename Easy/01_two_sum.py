class Solution:
    def twoSum(self, nums, target: int):
        hasmap = {}
        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in hasmap:
                return[hasmap[diff],i]
            hasmap[nums[i]]=i
if __name__=='__main__':
    nums = [2,5,7,11,15]
    target = 9
    ob = Solution()
    ans = ob.twoSum(nums,target)