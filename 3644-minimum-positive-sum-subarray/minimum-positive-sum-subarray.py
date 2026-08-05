from typing import List

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        ans = float('inf')
        n = len(nums)

        for k in range(l, r + 1):          # Try every window size
            if k > n:
                break

            window_sum = sum(nums[:k])

            if window_sum > 0:
                ans = min(ans, window_sum)

            for i in range(k, n):
                window_sum += nums[i]
                window_sum -= nums[i - k]

                if window_sum > 0:
                    ans = min(ans, window_sum)

        return ans if ans != float('inf') else -1
        