class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -1
        mad = math.inf
        currPsum = 0
        totalSum = 0
        
        for i in range(n):
            totalSum += nums[i]
            
        for i in range(n):
            currPsum += nums[i]
            leftPartAverage = currPsum
            leftPartAverage //= (i + 1)
            rightPartAverage = totalSum - currPsum
            
            if i != n-1:
                rightPartAverage //= (n-i-1)
            cd = abs(leftPartAverage - rightPartAverage)
            
            if cd < mad:
                mad = cd
                ans = i
        
        return ans