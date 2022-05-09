def sort(nums):
  for i in range(5):
    minpos=i
    for  j in range(i,6):
      if nums[j]<nums[minpos]:
        minpos=j
    temp=nums[i]
    nums[i]=nums[minpos]
    nums[minpos]=temp
nums=[2,8,4,3,6,1]
sort(nums)
print("after selection sort:",nums)
