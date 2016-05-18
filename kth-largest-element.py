class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self, k, A):
        low, high, curr_i, curr = 0, len(A) - 1, 0, A[0]
        arr_len = len(A)
        while low < high:
            while A[high] >= curr and high > low: high -= 1
            A[curr_i] = A[high]
            curr_i = high
            while A[low] <= curr and low < high: low += 1
            A[curr_i] = A[low]
            curr_i = low
        A[curr_i] = curr
        if arr_len - curr_i == k:
            return curr
        elif arr_len - curr_i > k:
            return self.kthLargestElement(k, A[curr_i + 1:arr_len])
        else:
            return self.kthLargestElement(k - arr_len + curr_i, A[0: curr_i])

if __name__ == "__main__":
    sol = Solution()
    print(sol.kthLargestElement(3, [1, 2, 3, 4, 5, 6, 7]))