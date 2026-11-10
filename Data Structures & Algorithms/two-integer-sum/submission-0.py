class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        look_up = {}
        for i, num in enumerate(nums):
            partner = target - num
            if partner in look_up:
                return [look_up[partner], i]
            look_up[num] = i