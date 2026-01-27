def max_n(nums: list):
    if len(nums) == 1:
        return nums[0]
    else:
        return nums[0] if nums[0] > max_n(nums[1:]) else max_n(nums[1:])