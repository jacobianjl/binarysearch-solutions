class Solution:
    def solve(self, nums):
        if not nums:
            return False
        if len(nums) == 1:
            return True
        if nums[0] < nums[1]:
            for i in range(1, len(nums)-1):
                if nums[i] >= nums[i+1]:
                    return False
            return True
        if nums[0] > nums[1]:
            for i in range(1, len(nums)-1):
                if nums[i] <= nums[i+1]:
                    return False
            return True
        else:
            return False
