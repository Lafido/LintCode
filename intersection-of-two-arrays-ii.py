class Solution:
    # @param {int[]} nums1 an integer array
    # @param {int[]} nums2 an integer array
    # @return {int[]} an integer array
    def intersection(self, nums1, nums2):
        result = []
        nums1.sort()
        nums2.sort()
        len1 = len(nums1)
        len2 = len(nums2)
        count1 = 0
        count2 = 0
        while count1 < len1 and count2 < len2:
            if nums1[count1] == nums2[count2]:
                result.append(nums1[count1])
                count1 += 1
                count2 += 1
            elif nums1[count1] < nums2[count2]:
                count1 += 1
            else:
                count2 += 1
        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.intersection([61,24,20,58,95,53,17,32,45,85,70,20,83,62,35,89,5,95,12,86,58,77,30,64,46,13,5,92,67,40,20,38,31,18,89,85,7,30,67,34,62,35,47,98,3,41,53,26,66,40,54,44,57,46,70,60,4,63,82,42,65,59,17,98,29,72,1,96,82,66,98,6,92,31,43,81,88,60,10,55,66,82,0,79,11,81], [5,25,4,39,57,49,93,79,7,8,49,89,2,7,73,88,45,15,34,92,84,38,85,34,16,6,99,0,2,36,68,52,73,50,77,44,61,48]))