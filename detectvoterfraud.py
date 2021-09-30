class Solution:
    def solve(self, votes):
        a = []
        for i in votes:
            a.append(i[1])
        if len(set(a)) < len(a):
            return True
        else:
            return False
