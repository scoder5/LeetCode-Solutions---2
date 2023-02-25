class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            res += matrix.pop(0)
            if matrix and matrix[0]:
                for i in matrix:
                    res.append(i.pop())
            if matrix:
                res += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for i in matrix[::-1]:
                    res.append(i.pop(0))
        return res