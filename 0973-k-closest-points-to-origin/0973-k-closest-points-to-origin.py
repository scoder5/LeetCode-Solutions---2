class Solution:
    def kClosest(self, p: List[List[int]], k: int) -> List[List[int]]:
        return sorted(p, key=lambda p: p[0]**2 + p[1]**2)[:k]