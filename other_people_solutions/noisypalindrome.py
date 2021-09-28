class Solution:
    def solve(self, s):
        return (lambda s: s == s[::-1])([c for c in s if "a" <= c <= "z"])
