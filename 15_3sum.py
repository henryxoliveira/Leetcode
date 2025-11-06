from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Find all unique triplets that sum to zero.
        
        Approach:
        1. Sort the array to make it easier to avoid duplicates
        2. Fix the first element and use two pointers for the remaining two
        3. Skip duplicates to ensure unique triplets
        
        Time Complexity: O(n^2)
        Space Complexity: O(1) excluding output array
        """
        nums.sort()
        result = []
        n = len(nums)
        
        for i in range(n - 2):
            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # If the smallest element is already > 0, no triplet can sum to 0
            if nums[i] > 0:
                break
            
            # Two pointers approach
            left, right = i + 1, n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    # Found a valid triplet
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    
                    # Skip duplicates for right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Move both pointers l
                    left += 1
                    right -= 1
                    
                elif current_sum < 0:
                    # Need a larger sum, move left pointer
                    left += 1
                else:
                    # Need a smaller sum, move right pointer
                    right -= 1
        
        return result


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    nums1 = [-1, 0, 1, 2, -1, -4]
    print(f"Input: {nums1}")
    print(f"Output: {solution.threeSum(nums1)}")
    print(f"Expected: [[-1, -1, 2], [-1, 0, 1]]\n")
    
    # Example 2
    nums2 = [0, 1, 1]
    print(f"Input: {nums2}")
    print(f"Output: {solution.threeSum(nums2)}")
    print(f"Expected: []\n")
    
    # Example 3
    nums3 = [0, 0, 0]
    print(f"Input: {nums3}")
    print(f"Output: {solution.threeSum(nums3)}")
    print(f"Expected: [[0, 0, 0]]\n")

