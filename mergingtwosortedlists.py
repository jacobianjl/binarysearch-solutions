class Solution:
    def solve(self, a, b):
        c = []
        i, j = 0, 0
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                c.append(a[i])
                i += 1
            else:
                c.append(b[j])
                j += 1
        return c + a[i:] + b[j:]
