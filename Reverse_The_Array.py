def reverseArray(nums, m):
    n=len(nums)
    nums=nums[0:m+1]+nums[n:m:-1]
    return nums
