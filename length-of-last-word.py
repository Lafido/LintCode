class Solution:
    # @param {string} s A string
    # @return {int} the length of last word
    def lengthOfLastWord(self, s):
        if s:
            s = s.rstrip(' ')
            s_list = s.split(" ")
            last = s_list[-1]
            if not self.hasNumbers(last):
                return len(last)
            else:
                return 0
        else:
            return 0

    def hasNumbers(self, s):
        return any(ch.isdigit() for ch in s)