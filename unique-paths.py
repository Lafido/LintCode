class Solution:
    """
    @param n and m: positive integer(1 <= n , m <= 100)
    @return an integer
    """
    def uniquePaths(self, m, n):
        if m == 0 and n == 0:
            return 0
        ways = [[0 for i in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    ways[i][j] = 1
                elif i == 0:
                    ways[i][j] = ways[i][j - 1]
                elif j == 0:
                    ways[i][j] = ways[i - 1][j]
                else:
                    ways[i][j] = ways[i - 1][j] + ways[i][j - 1]
        return ways[m - 1][n - 1]