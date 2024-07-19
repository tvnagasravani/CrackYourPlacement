class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ans =set()
        for i in nums:
            if i in ans:
                return i
            ans.add(i)
