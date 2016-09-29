class Solution:
    """
    @param A: A list of integers
    @param elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        if A:
            length = len(A)
            idx = 0
            for i in range(0, length):
                if A[i] != elem:
                    A[idx] = A[i]
                    idx += 1
            A[idx:] = []
            return idx