class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if i==j:
                    continue
                if (nums[i]+nums[j])==target:
                    return [i,j]

solution=Solution()
nums1=input().strip("[]")
nums=list(map(int,nums1.split(',')))
target=int(input())
result=solution.twoSum(nums,target)
print(result)
        
# Using hashmap to reduce time complexity from O(n^2) to O(n)
# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         num_and_index = {}
        
#         for i, value in enumerate(nums):
#             complement = target - value
#             if complement in num_and_index:
#                 return [num_and_index[complement], i]
#             num_and_index[value] = i
        
#         return [] 