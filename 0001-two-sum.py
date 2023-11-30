from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            hash_map[nums[i]] = i
        for i in range(len(nums)):
            try:
                j = hash_map[target - nums[i]]
                if i != j:
                    return [i, j]
            except KeyError:
                continue
