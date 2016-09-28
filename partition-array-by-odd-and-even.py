class Solution:
    # @param nums: a list of integers
    # @return: nothing
    def partitionArray(self, nums):
        if nums:
            low, high = 0, len(nums) - 1
            while low < high:
                while nums[low] % 2 == 1:
                    low += 1
                while nums[high] % 2 == 0:
                    high -= 1
                if low < high:
                    nums[low], nums[high] = nums[high], nums[low]