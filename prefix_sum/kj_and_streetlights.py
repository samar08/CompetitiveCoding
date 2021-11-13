n, p = list(map(int, input().split(" ")))
x = []
ra = []
for i in range(n):
    xi, ri = list(map(int, input().split(" ")))
    x.append(xi)
    ra.append(ri)
prefix = []
for i in range(p + 2):
    prefix.append(0)
l = []
r = []
for i in range(n):
    if (x[i] - ra[i] < 0):
        l.append(0)
    else:
        l.append(x[i] - ra[i])
    if (x[i] + ra[i] > p):
        r.append(p)
    else:
        r.append(x[i] + ra[i])
for i in range(n):
    prefix[l[i]] += 1
    prefix[r[i] + 1] -= 1
cost = 0
for i in range(p + 2):
    cost += prefix[i]
    prefix[i] = cost
# print(prefix)
count = 0
maxcount = 0
for i in range(p + 1):
    if (prefix[i] == 0 or prefix[i] > 1):
        count += 1
        maxcount = max(maxcount, count)
    else:

        count = 0
print(maxcount)