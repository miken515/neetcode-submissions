class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        most = count.most_common(1)
        return most[0][0]