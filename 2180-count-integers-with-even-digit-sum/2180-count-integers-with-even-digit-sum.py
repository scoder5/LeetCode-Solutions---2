class Solution:
    def countEven(self, num: int) -> int:
        
        def digitSum(n):
            return sum(int(i) for i in str(n))

        count = 0
        for i in range(1, num+1):
            if digitSum(i) % 2 == 0:
                count += 1
                
        return count