class Solution:
    """
    @param A: An integer array.
    @param B: An integer array.
    @return: Cosine similarity.
    """
    def cosineSimilarity(self, A, B):
        # write your code here
        from math import sqrt
        if not A or not B:
            return 2.0
        dvd = sum(map(lambda x: x[0] * x[1], zip(A, B)))
        dvs_a, dvs_b = sqrt(sum(map(lambda x: x ** 2, A))), sqrt(sum(map(lambda x: x ** 2, B)))
        if dvs_a == 0 or dvs_b == 0:
            return 2.0
        return dvd / (float(dvs_a) * float(dvs_b))