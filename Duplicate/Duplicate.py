class Solution:
    def findDuplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))


sol = Solution()

print(sol.findDuplicate([1, 2, 3, 4, 5, 6, 6, 8, 9, 10]))  # Output: False