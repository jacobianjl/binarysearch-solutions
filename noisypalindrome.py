class Solution:
    def solve(self, s):
        s = "".join([a for a in s if not a.isdigit()])
        s = "".join([b for b in s if not b.isupper()])
        for i in range(0, int(len(s) / 2)):
            if s[i] != s[len(s) - i - 1]:
                return False
        return True
