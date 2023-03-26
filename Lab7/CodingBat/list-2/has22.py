def has22(nums):
  answer = False
  for i in range(1, len(nums)):
    if nums[i] == 2 and nums[i - 1] == 2:
      answer = True
      
  return answer