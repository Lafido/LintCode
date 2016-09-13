class Solution:
    # @param {int[]} A an integer array
    # @return nothing
    def sortIntegers(self, A):
        # Write your code here
        A.sort()

if __name__ == "__main__":
    sol = Solution()
    print(sol.sortIntegers([3,2,1,4,5]))