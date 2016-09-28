class Solution:
    # @param {int[]} digits a number represented as an array of digits
    # @return {int[]} the result
    def plusOne(self, digits):
        if digits and len(digits) > 0:
            length = len(digits)
            carry = 1
            for i in range(1, length + 1):
                if carry == 0:
                    break
                digits[-i] += carry
                carry = digits[-i] / 10
                digits[-i] %= 10
            if carry > 0:
                digits.insert(0, carry)
            return digits
