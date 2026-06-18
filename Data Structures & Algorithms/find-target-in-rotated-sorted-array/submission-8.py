class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
 
        while low <= high:
            mid = (low + high) // 2
    
            # Target found
            if target == nums[mid]:
                return mid
            
            # Left half is sorted (no rotation in this half)
            if nums[low] <= nums[mid]:
                # Target is outside the sorted left half — search right
                if target > nums[mid] or target < nums[low]:
                    low = mid + 1
                # Target is within the sorted left half — search left
                else:
                    high = mid - 1
            
            # Right half is sorted (rotation point is in left half)
            else:
                # Target is outside the sorted right half — search left
                if target < nums[mid] or target > nums[high]:
                    high = mid - 1
                # Target is within the sorted right half — search right
                else:
                    low = mid + 1
    
        # Target not found
        return -1