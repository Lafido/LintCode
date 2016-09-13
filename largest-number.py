class Solution:
    # @param num: A list of non negative integers
    # @return: A string
    def largestNumber(self, num):
        # write your code here
        from functools import cmp_to_key
        key = cmp_to_key(lambda x, y: int(y + x) - int(x + y))
        return ''.join(sorted(map(str, num), key=key)).lstrip('0') or '0'

if __name__ == "__main__":
    sol = Solution()
    print(sol.largestNumber([1, 20, 23, 4, 8]))
