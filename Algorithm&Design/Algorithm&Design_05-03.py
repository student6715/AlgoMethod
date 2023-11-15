# アルゴリズムと設計技法
# https://algo-method.com/courses/27
# 5: 動的計画法 (1) イントロダクション
# Q3: 階段ののぼり方
# https://algo-method.com/tasks/304

import io
import sys

_INPUT = """\
10
"""

sys.stdin = io.StringIO(_INPUT)

N = int(input())
DP = [-1] * (N+1)
DP[0], DP[1] = 1, 1
for i in range(2, N+1):
    DP[i] = DP[i-2] + DP[i-1]
print(DP[N])