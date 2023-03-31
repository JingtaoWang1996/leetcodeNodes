"""
Given a string, find the length of the longest substring without repeating characters
"""
"""
可能的方法
1、滑动窗口：没有重复的字符串==扩大右边界；出现重复字符串==缩小左边界
           使用hashmap辅助记录重复的坐标位置，出现重复且在当前窗口范围内则更新窗口左边界，否则更新窗口最大值
           ---56 ms  87.22%   15.1 MB   54.74%
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        if length <= 1:
            return length
        res, p1, p2, aid = 1, 0, 1, {s[0]: 0}
        while p2 < length:
            if aid.__contains__(s[p2]) and aid[s[p2]] >= p1:
                p1 = aid[s[p2]] + 1  # 重复值的下一个
            res = max(res, p2 - p1 + 1)
            aid.update({s[p2]: p2})
            p2 += 1

        return res


if __name__ == '__main__':
    s = Solution()
    s.lengthOfLongestSubstring("pwkeww")
