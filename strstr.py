class Solution:
    def strStr(self, source, target):
        # write your code here
        if source is None or target is None:
            return -1
        i, length, target_hash = 0, len(target), hash(target)
        while i <= len(source) - len(target):
            attempt = source[i:i + length]
            if hash(attempt) == target_hash and attempt == target:
                return i
            i += 1
        return -1