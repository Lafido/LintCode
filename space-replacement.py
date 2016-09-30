class Solution:
    # @param {char[]} string: An array of Char
    # @param {int} length: The true length of the string
    # @return {int} The true length of new string
    def replaceBlank(self, string, length):
        # Write your code here
        if not string:
            return 0
        count = 0
        for i in range(length):
            if string[i] == ' ':
                count += 1
        new_length = length + 2 * count
        string += [''] * 2 * count
        j = 1
        for i in reversed(range(length)):
            if string[i] != ' ':
                string[new_length - j] = string[i]
                j += 1
            else:
                string[new_length - j ] = '0'
                j += 1
                string[new_length - j ] = '2'
                j += 1
                string[new_length - j ] = '%'
                j += 1
        return new_length