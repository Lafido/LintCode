class Solution:
    # @param s: a list of char
    # @param offset: an integer
    # @return: nothing
    def rotateString(self, s, offset):
        if not s:
            return
        len_str = len(s)
        offset %= len_str
        if offset == 0:
            return
        s.reverse()
        s[offset:] = s[:offset - 1:-1]
        s[:offset] = s[offset - 1::-1]
