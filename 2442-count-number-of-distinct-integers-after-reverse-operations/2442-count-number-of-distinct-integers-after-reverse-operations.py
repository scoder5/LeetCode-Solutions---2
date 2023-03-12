class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        def reverse(n):
            rev = 0
            while n != 0:
                rev = rev * 10 + (n % 10)
                n //= 10
            return rev
        for i in range(len(nums)):
            nums.append(reverse(nums[i]))
        return len(set(nums))