class Solution:
    """
    @param A : A string includes Upper Case letters
    @param B : A string includes Upper Case letters
    @return :  if string A contains all of the characters in B return True else return False
    """
    def compareStrings(self, A, B):
        # write your code here
        counter = [0 for _ in range(26)]
        for i in range(len(A)):
            if ord('A') <= ord(A[i]) <= ord('Z'):
                counter[ord(A[i]) - ord('A')] += 1
        for i in range(len(B)):
            if ord('A') <= ord(B[i]) <= ord('Z'):
                counter[ord(B[i]) - ord('A')] -= 1
                if counter[ord(B[i]) - ord('A')] < 0:
                    return False
        return True