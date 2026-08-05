class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        a=max(nums)
        b=min(nums)
        missing = []
        for i in range(b,a+1):
            if i not in nums:
                missing.append(i)
        return missing