class Solution:
    # @param {string} s A string
    # @return {boolean} Whether the string is a valid palindrome
    def isPalindrome(self, s):
        # Write your code here
        i = 0
        j = len(s) - 1
        while i < j:
            while i < j and s[i].isalnum() is False:
                i += 1
            while i < j and s[j].isalnum() is False:
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
