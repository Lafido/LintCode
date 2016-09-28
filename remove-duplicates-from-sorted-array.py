class Solution:
    """
    @param A: a list of integers
    @return an integer
    """

    def removeDuplicates(self, A):
        if A:
            idx = 1
            for i in range(1, len(A)):
                if A[i] != A[i - 1]:
                    A[idx] = A[i]
                    idx += 1
            A[idx:] = []
            return len(A)
