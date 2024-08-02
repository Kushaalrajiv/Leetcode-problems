nums=list(map(int,input().split()))
i=1
while i < len(nums):
    if nums[i]==nums[i-1]:
        nums.pop(i)
    else:
        i+=1
print(nums)
print(len(nums))
