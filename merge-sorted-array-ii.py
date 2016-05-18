class Solution:
    #@param A and B: sorted integer array A and B.
    #@return: A new sorted integer array
    def mergeSortedArray(self, A, B):
        if not A or not B:
            return A or B
        idx_a, idx_b, result = 0, 0, []
        len_a, len_b = len(A), len(B)
        while idx_a < len_a and idx_b < len_b:
            if A[idx_a] < B[idx_b]:
                result.append(A[idx_a])
                idx_a += 1
            else:
                result.append(B[idx_b])
                idx_b += 1

        if idx_a < len_a:
            result.extend(A[idx_a:])
        if idx_b < len_b:
            result.extend(B[idx_b:])

        return result