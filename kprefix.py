class Solution:
    def solve(self, nums, k):
        if not nums:
            return -1
        sums = sum(nums)
        for i in range(0, len(nums)):
            if sums > k:
                sums -= nums[len(nums) - 1 - i]
            else:
                return len(nums) - 1 - i
        return -1

# Another solution
class Solution:
    def solve(self, nums, k):
        sum = 0
        position = -1
        for index, value in enumerate(nums):
            sum += value
            if sum <= k:
                position = index
        return position

