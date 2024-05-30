class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        # transpose the matrix
        for i in range(n):
            for j in range(i, n):
                # swap diagonally
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # reverse each row
        for i in range(n):
            matrix[i].reverse()
