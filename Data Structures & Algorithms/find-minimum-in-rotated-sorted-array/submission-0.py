class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = nums[l]
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                return res
            
            mid = (l + r) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1 #search right side
            else:
                r = mid - 1 #search left side

        return res                