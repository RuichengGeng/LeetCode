class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        pos = 0
        for i in range(len(nums)):
            element = nums[i]
            if element != val:
                nums[pos], nums[i] = nums[i], nums[pos]
                k += 1
                pos += 1
        nums = nums[:k]
        return pos