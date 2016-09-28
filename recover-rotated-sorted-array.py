class Solution:
    """
    @param nums: The rotated sorted array
    @return: nothing
    """

    def recoverRotatedSortedArray(self, nums):
        if nums:
            nums_len = len(nums)
            idx = 0
            for i in range(1, nums_len):
                if nums[i] < nums[i - 1]:
                    idx = i
            if idx != 0:
                nums[idx:] = nums[:idx - 1:-1]
                nums[:idx] = nums[idx - 1::-1]
                nums.reverse()


if __name__ == "__main__":
    sol = Solution()
    m_list = [4, 5, 1, 2, 3]
    sol.recoverRotatedSortedArray(m_list)
    print(m_list)
