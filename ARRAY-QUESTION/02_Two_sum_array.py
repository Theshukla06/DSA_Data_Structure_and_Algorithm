#          ARRAY TWO SUM PROGRAM
#GIVEN NUMS = [2,7,11,15] , TARGET = 9
#BECAUSE NUMS[0] + NUMS[1] = 2 + 7 = 9
#RETURN [0,1]


def TwoSum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if target - nums[i]==nums[j]:
                return [i,j]
test=[2,7,11,15]
target=9
print(TwoSum(test,target))

#  d = {}
#         for i, n in enumerate(nums):
#             m = target - n
#             if m in d:
#                 return [d[m], i]
#             else:
#                 d[n] = i