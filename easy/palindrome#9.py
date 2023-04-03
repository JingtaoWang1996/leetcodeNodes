"""
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
"""
"""
# 注意点：1）负数 不是回文数
# 可能方法：
1、转成字符串判断 
64 ms  58.20%
15 MB  19.52%
2、取整取余判断
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)[::-1] == str(x)

s = Solution()
print(s.isPalindrome(10))
