# アルゴリズムと設計技法
# https://algo-method.com/courses/27
# 5: 動的計画法 (1) イントロダクション
# Q6: すごろく
# https://algo-method.com/tasks/323

import io
import sys

_INPUT = """\
11 6
2 4 6 8 10 12
"""

sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())
D = list(map(int, input().split()))
DP = [False] * (N+1)
DP[0] = True
for i in range(1, N+1):
    for dice in D:
        if i - dice >= 0 and DP[i - dice]:
            DP[i] = True
print('Yes' if DP[N] else 'No')