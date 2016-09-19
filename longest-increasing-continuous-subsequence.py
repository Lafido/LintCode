class Solution:
    # @param {int[]} A an array of Integer
    # @return {int}  an integer
    def longestIncreasingContinuousSubsequence(self, A):
        if A:
            max_increasing_len = 1
            max_len = 1
            max_len_2 = 1
            for i in range(1, len(A)):
                if A[i] >= A[i - 1]:
                    max_len += 1
                    if A[i] != A[i - 1]:
                        max_len_2 = 1
                    if max_increasing_len < max_len:
                        max_increasing_len = max_len
                if A[i] <= A[i - 1]:

                    max_len_2 += 1
                    if A[i] != A[i - 1]:
                        max_len = 1
                    if max_increasing_len < max_len_2:
                        max_increasing_len = max_len_2
            return max_increasing_len
        else:
            return 0
