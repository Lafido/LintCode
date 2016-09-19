class Solution:
    """
    @param A: sorted integer array A which has m elements,
              but size of A is m+n
    @param B: sorted integer array B which has n elements
    @return: void
    """

    def mergeSortedArray(self, A, m, B, n):
        last, i, j = m + n - 1, m - 1, n - 1
        while i >= 0 and j >= 0:
            if A[i] > B[j]:
                A[last] = A[i]
                last, i = last - 1, i - 1
            else:
                A[last] = B[j]
                last, j = last - 1, j - 1
        while j >= 0:
            A[last] = B[j]
            last, j = last - 1, j - 1
