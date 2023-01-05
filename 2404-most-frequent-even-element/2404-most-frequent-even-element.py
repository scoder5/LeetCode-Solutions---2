class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        hmap = {}
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                hmap[nums[i]] = 1 + hmap.get(nums[i], 0)
        
        res, maxx = -1, 0
        for num, count in hmap.items():
            if count > maxx:
                maxx = count
                res = num
            elif count == maxx:
                res = min(res, num)
        return res