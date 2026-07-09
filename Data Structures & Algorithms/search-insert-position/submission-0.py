class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums) - 1
        res = len(nums)
        while l <= h:
            mid = (l + h) // 2

            if nums[mid] == target:
                return mid
            
            if target < nums[mid]:
                res = mid
                h = mid - 1
            else:
                l = mid + 1
        return res
            