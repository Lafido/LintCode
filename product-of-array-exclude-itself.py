class Solution:
    """
    @param A: Given an integers array A
    @return: An integer array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """
    def productExcludeItself(self, A):
        # write your code here
        left = [1 for _ in range(len(A))]
        right = [1 for _ in range(len(A))]
        for i in range(1, len(A)):
            left[i] = left[i - 1] * A[i - 1]
        for i in reversed(range(len(A) - 1)):
            right[i] = right[i + 1] * A[i + 1]
        result = [left[i] * right[i] for i in range(len(A))]
        return result