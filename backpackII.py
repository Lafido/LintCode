class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A & V: Given n items with size A[i] and value V[i]
    # @return: The maximum value
    def backPackII(self, m, A, V):
        # write your code here
        capacity = [0] * (m + 1)
        for i in range(len(A)):
            for j in range(m, A[i] - 1, -1):
                capacity[j] = max(capacity[j - A[i]] + V[i], capacity[j])
        return capacity[-1]

if __name__ == "__main__":
    sol = Solution()
    print(sol.backPackII(10, [2, 3, 5, 7], [1, 5, 2, 4]))
