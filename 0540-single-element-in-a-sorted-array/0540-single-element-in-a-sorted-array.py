class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        counts = {}
        for i in range(len(nums)):
            counts[nums[i]] = 1 + counts.get(nums[i], 0)
        for i in counts:
            if counts[i] == 1:
                return i
        return