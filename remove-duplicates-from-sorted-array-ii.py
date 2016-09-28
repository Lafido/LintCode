class Solution:
    """
    @param A: a list of integers
    @return an integer
    """

    def removeDuplicates(self, A):
        start, end, state = 0, 1, 0
        while end < len(A):
            if A[start] == A[end]:
                if state == 0:
                    state = 1
                    start += 1
                    A[start] = A[end]
            else:
                state = 0
                start += 1
                A[start] = A[end]
            end += 1
        return start + 1
