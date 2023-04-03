"""
#11. 盛最多水的容器
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
返回容器可以储存的最大水量。
说明：你不能倾斜容器。
"""
"""
可能的思路
1、双指针：从两边开始向中间走，左右两边数量较小的往中间优化[底更小了,那么高就应该尽可能更大]
   PS:80 ms   63.28%   25.3 MB   84.24%
"""


class Solution:
    def maxArea(self, height) -> int:
        left, right = 0, len(height) - 1
        cur_area = (right - left) * min(height[left], height[right])
        while left < right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            cur_area = max(cur_area, (right - left) * min(height[left], height[right]))
        return cur_area


s = Solution()
print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
