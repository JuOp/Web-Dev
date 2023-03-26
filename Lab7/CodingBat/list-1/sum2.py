def sum2(nums):
    if len(nums) == 0:
        return 0
        
    return nums[0] if len(nums) == 1 else nums[0] + nums[1]