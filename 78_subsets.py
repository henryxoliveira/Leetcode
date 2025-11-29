from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res: List[List[int]] = []
        subset: List[int] = []

        def backtrack(i: int) -> None:
            # If we've considered all elements, add a copy of the current subset
            if i == len(nums):
                res.append(subset.copy())
                return

            # Decision 1: include nums[i]
            subset.append(nums[i])
            backtrack(i + 1)

            # Decision 2: exclude nums[i]
            subset.pop()
            backtrack(i + 1)

        backtrack(0)
        return res
