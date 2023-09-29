class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        is_increasing = False
        is_decreasing = False

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] > nums[i-1]:
                is_increasing = True
            if nums[i] < nums[i-1]:
                is_decreasing = True

            if is_increasing and is_decreasing:
                return False

        return True
