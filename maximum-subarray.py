class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """
    def maxSubArray(self, nums):
        if nums:
            sum = 0
            max_sum = nums[0]
            for num in nums:
                sum += num
                if max_sum < sum:
                    max_sum = sum
                if sum < 0:
                    sum = 0
            return max_sum