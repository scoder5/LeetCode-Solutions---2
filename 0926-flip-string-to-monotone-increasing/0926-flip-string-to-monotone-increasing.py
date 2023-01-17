class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        m = 0
        for i in s:
            if i == '0':
                m += 1
        
        ans = m
        for j in s:
            if j == '0':
                m -= 1
                ans = min(ans, m)
            else:
                m += 1
        
        return ans