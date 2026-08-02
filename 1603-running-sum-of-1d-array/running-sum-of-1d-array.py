class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        pre=[0 for i in range (len(nums))]
        sum = 0 
        for i in range(len(nums)):
            sum = sum + nums[i]
            pre[i]=sum
        return pre
