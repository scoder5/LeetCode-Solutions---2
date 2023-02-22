class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        string = ""
        for n in num:
            string += str(n)
        res = int(string) + k
        return [int(i) for i in str(res)]