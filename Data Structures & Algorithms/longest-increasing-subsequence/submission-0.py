class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ls = [1] * len(nums)


        for i in range(len(nums) -1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    ls[i] = max(ls[i], 1 + ls[j])
        
        return max(ls)
