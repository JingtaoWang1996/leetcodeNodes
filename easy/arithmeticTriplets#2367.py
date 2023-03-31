"""
2367. 算术三元组的数目
给你一个下标从 0 开始、严格递增 的整数数组 nums 和一个正整数 diff 。如果满足下述全部条件，则三元组 (i, j, k) 就是一个 算术三元组 ：
i < j < k ，
nums[j] - nums[i] == diff 且
nums[k] - nums[j] == diff
返回不同 算术三元组 的数目。
"""
"""
可能的思路： 
1、遍历到length-2个，看是否满足给定条件，【给定了严格递增，否则hash遍历一次O（n）存一遍】
   ---- 32 ms    94.79%    14.8 MB    78.63%
"""


class Solution:
    def arithmeticTriplets(self, nums, diff: int) -> int:
        res = 0
        for i in range(len(nums) - 2):
            if nums[i] + diff in nums and nums[i] + diff * 2 in nums:
                res += 1
        return res


s = Solution()
nums = [4, 5, 6, 7, 8, 9]
diff = 2
s.arithmeticTriplets(nums, diff)
