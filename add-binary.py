class Solution:
    # @param {string} a a number
    # @param {string} b a number
    # @return {string} the result
    def addBinary(self, a, b):
        # Write your code here
        sum = int(a, 2) + int(b, 2)
        return str(bin(sum))[2:]

if __name__ == "__main__":
    sol = Solution()
    print(sol.addBinary('11', '1'))