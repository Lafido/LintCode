class Solution:
    # @param dictionary: a list of strings
    # @return: a list of strings
    def longestWords(self, dictionary):
        if dictionary:
            max_len = 0
            result = []
            for word in dictionary:
                word_len = len(word)
                if word_len > max_len:
                    result = [word]
                    max_len = word_len
                elif word_len == max_len:
                    result.append(word)
        return result