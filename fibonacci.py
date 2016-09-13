class Solution:
    # @param n: an integer
    # @return an integer f(n)
    def fibonacci(self, n):
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            fib, last = 1, 0
            for i in range(2, n):
                fib = fib + last
                last = fib - last
            return fib

if __name__ == "__main__":
    sol = Solution()
    print(sol.fibonacci(3))