class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """
    def anagram(self, s, t):
        # write your code here
        if len(s) != len(t):
            return False
        count = [0 for _ in range(256)]
        for i in range(len(s)):
            count[ord(s[i])] += 1
            count[ord(t[i])] -= 1
        return all([count[i] == 0 for i in range(256)])