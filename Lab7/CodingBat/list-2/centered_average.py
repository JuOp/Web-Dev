def centered_average(nums):
    max_value = nums[0]
    min_value = nums[0]
    sum = 0
    for x in nums:
        max_value = max(max_value, x)
        min_value = min(min_value, x)
        sum += x

    return (sum - max_value - min_value) / (len(nums) - 2)