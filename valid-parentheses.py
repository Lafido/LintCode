class Solution:
    # @param {string} s A string
    # @return {boolean} whether the string is a valid parentheses
    def isValidParentheses(self, s):
        # Write your code here
        dic = {'(':')', '[':']', '{':'}'}
        stack = []
        for c in s:
            if c in dic:
                stack.append(c)
            else:
                if not stack:
                    return False
                if dic[stack[-1]] != c:
                    return False
                stack.pop()
        return not stack