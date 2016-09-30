class Solution:
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left <= right:
            mid = left + (right - left) / 2
            x, y = mid / n, mid % n
            if matrix[x][y] > target:
                right = mid - 1
            elif matrix[x][y] < target:
                left = mid + 1
            else:
                return True
        return False