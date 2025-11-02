from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Binary search approach to find the insert position.
        O(log n) time complexity, O(1) space complexity.
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        # If target is not found, left will point to the insertion position
        return left


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1: Target found
    nums1 = [1, 3, 5, 6]
    target1 = 5
    print(f"nums = {nums1}, target = {target1}")
    print(f"Output: {solution.searchInsert(nums1, target1)}")  # Expected: 2
    print()
    
    # Example 2: Insert at position 1
    nums2 = [1, 3, 5, 6]
    target2 = 2
    print(f"nums = {nums2}, target = {target2}")
    print(f"Output: {solution.searchInsert(nums2, target2)}")  # Expected: 1
    print()
    
    # Example 3: Insert at the end
    nums3 = [1, 3, 5, 6]
    target3 = 7
    print(f"nums = {nums3}, target = {target3}")
    print(f"Output: {solution.searchInsert(nums3, target3)}")  # Expected: 4
    print()
    
    # Additional test: Insert at the beginning
    nums4 = [1, 3, 5, 6]
    target4 = 0
    print(f"nums = {nums4}, target = {target4}")
    print(f"Output: {solution.searchInsert(nums4, target4)}")  # Expected: 0

