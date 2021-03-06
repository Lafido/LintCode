class Solution:
    """
    @param nums: A list of integers
    @return: The majority number
    """
    def majorityNumber(self, nums):
        # write your code here
        count, result = 1, nums[0]
        for num in nums[1:]:
            if num == result:
                count += 1
            else:
                count -= 1
                if count == 0:
                    count, result = 1, num
        return result