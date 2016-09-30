class Solution:
    # @param s : A string
    # @return : A string
    def reverseWords(self, s):
        if s:
            new_s = s.strip(" ")
            if new_s:
                s_list = new_s.split(" ")
                s_list.reverse()
                return " ".join(s_list)
        return ""
