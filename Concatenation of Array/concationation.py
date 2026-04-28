from typing import List
nums=[1,2,3]
class Solution:
    def getconcatination(self,nums:list[int])->list[int]:
        return nums+nums

sol = Solution()
result = sol.getconcatination(nums)
print(result)