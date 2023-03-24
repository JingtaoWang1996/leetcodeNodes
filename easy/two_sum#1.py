"""
Given an array of integers,
return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.
"""
"""
可能的方法
注意可能存在两个完全相同的值但下标不同
1、暴力遍历：每次从当前位置往后走找是否有满足条件的值，直接保证数据肯定不一致： O（n2）
2、dict {值：对应的所有下标}， 1）两个不同值  2）两个相同值且下标数量为2 O(n)
   --- 44ms 16.8MB
   2.1、顺序便利一遍数组构建字典，如果新元素在字典中有，则直接返回，否则继续存入,最坏情况才是遍历完
"""

import collections


class Solution:
    # 20230324 44ms  16.8MB
    def twoSum(self, nums, target):
        # create collection.defaultDict() to save {data:[index]}
        mapper = collections.defaultdict()
        for i in range(len(nums)):
            if mapper.__contains__(nums[i]):
                mapper[nums[i]].append(i)
            else:
                mapper.update({nums[i]: [i]})
        # check mapper
        for key in mapper:
            if target - key not in mapper:
                continue
            elif target - key in mapper:
                if key != target - key:
                    return mapper[key] + mapper[target - key]
                elif key == target - key and len(mapper[key]) == 2:
                    return mapper[key]
                else:
                    continue

    # 20230324  40ms 16.3MB
    def twoSum1(self, nums, target):
        mapper = collections.defaultdict()
        for i in range(len(nums)):
            if not target - nums[i] in mapper:
                mapper.update({nums[i]: i})
            else:
                return [mapper[target - nums[i]], i]


if __name__ == '__main__':
    nums = [3, 3]
    target = 6
    solution = Solution()
    print(solution.twoSum1(nums, target))
