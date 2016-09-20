class Solution:
    # @param {int[]} nums an integer array
    # @return nothing, do this in-place
    def moveZeroes(self, nums):
        if nums:
            j = 0
            for i in range(0, len(nums)):
                if nums[i] != 0:
                    nums[j] = nums[i]
                    j += 1
            for i in range(j, len(nums)):
                nums[i] = 0
