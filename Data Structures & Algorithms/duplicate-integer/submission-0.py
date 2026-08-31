class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setFromList = set(nums)
        if len(setFromList) != len(nums):
            return True
        return False