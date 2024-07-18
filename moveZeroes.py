class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left=0
        right=0
        for right in range(len(nums)):
            if nums[right] != 0:
                # Swap elements if the current element is not zero
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
