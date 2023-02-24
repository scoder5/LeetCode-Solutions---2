class Solution:
    def findRotation(self, mat: List[List[int]], tar: List[List[int]]) -> bool:
        def rotate(mat):
            return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0])-1,-1,-1)]

        c = 0
        while True:
            if  c > 3:
                break
            elif mat == tar:
                return True
            else:
                mat = rotate(mat)
            c += 1
        return False