class Solution:
    # @param {int} n the nth
    # @return {string} the nth sequence
    def countAndSay(self, n):
        # Write your code here
        result = "1"
        while n > 1:
            temp = ""
            list_len = len(result)
            count = 1
            for i in range(1, list_len):
                if result[i] == result[i - 1]:
                    count += 1
                else:
                    temp += str(count)
                    temp += str(result[i - 1])
                    count = 1
            temp += str(count)
            temp += str(result[-1])
            result = temp
            n -= 1
        return result