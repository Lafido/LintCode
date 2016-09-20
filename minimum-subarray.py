class Solution:
    """
    @param nums: a list of integers
    @return: A integer denote the sum of minimum subarray
    """
    def minSubArray(self, nums):
        if nums:
            sum = 0
            min_sum = nums[0]
            for num in nums:
                sum += num
                if min_sum > sum:
                    min_sum = sum
                if sum > 0:
                    sum = 0
            return min_sum