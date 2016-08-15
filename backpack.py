class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A: Given n items with size A[i]
    # @return: The maximum size
    def backPack(self, m, A):
        # write your code here
        capacities = [0] * (m + 1)
        for i in range(len(A)):
            for j in range(m, A[i] - 1, -1):
                capacities[j] = max(capacities[j - A[i]] + A[i], capacities[j])
        return capacities[-1]

if __name__ == "__main__":
    sol = Solution()
    print(sol.backPack(12, [2, 3, 5, 7]))