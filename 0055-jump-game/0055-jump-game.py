class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True
        maxReach = nums[0]
        for i in range(1, len(nums)):
            if i > maxReach:
                return False
            maxReach = max(maxReach, i+nums[i])
            if maxReach >= len(nums)-1:
                return True
        return False