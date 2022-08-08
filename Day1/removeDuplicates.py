from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        for right in range(1, len(nums)):
            if nums[right] != nums[right - 1]:
                nums[left] = nums[right]
                left += 1
        return left

sol = Solution()
left = sol.removeDuplicates([1,1,2])
print(left)
