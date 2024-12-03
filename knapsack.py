import itertools
import sys

lines = [list(map(int, line.strip().split())) for line in sys.stdin.readlines()]
p = [x[0] for x in lines[1:]]
v = [x[1] for x in lines[1:]]
S, N = lines[0]
opt = [[0] * (S + 1) for _ in range(N)]
for cap in range(p[0], S + 1):
    opt[0][cap] = v[0]
for i, cap in itertools.product(range(1, N), range(S + 1)):
    if cap >= p[i]:
        opt[i][cap] = max(opt[i - 1][cap], opt[i - 1][cap - p[i]] + v[i])
    else:
        opt[i][cap] = opt[i - 1][cap]

print(opt[N - 1][S])
