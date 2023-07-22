n, l = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

max_gap = 0
for i in range(1, n):
    max_gap = max(max_gap, a[i] - a[i - 1])

d = max(max_gap / 2, max(a[0], l - a[-1]))
print("{:.10f}".format(d))