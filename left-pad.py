class StringUtils:
    # @param {string} originalStr the string we want to append to
    # @param {int} size the target length of the string
    # @param {string} padChar the character to pad to the left side of the string
    # @return {string} a string
    @classmethod
    def leftPad(self, originalStr, size, padChar=' '):
        orig_len = len(originalStr)
        if orig_len >= size:
            return originalStr
        pad_len = size - orig_len
        return pad_len * str(padChar) + originalStr

