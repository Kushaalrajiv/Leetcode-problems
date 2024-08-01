# nums=list(map(int,input().split(',')))
# target=(int(input()))
# start=0
# end=len(nums)-1
# while start<=end:
#     mid=(start+end)//2
#     if target==nums[mid]:
#         print("found",mid)
#         break
#     elif target>nums[mid]:
#         start=mid+1
#         if target not in nums:
#             nums.append(target)
#             print(nums)
#             nums.sort()
#             print(nums)
            
#     elif target<nums[mid]:
#         end=mid-1
#         if target not in nums:
#             nums.append(target)
#             nums.sort()


##if element not present, return position where it could be added
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = (start + end) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
        return start
    
