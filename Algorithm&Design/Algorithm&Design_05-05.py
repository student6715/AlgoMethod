# アルゴリズムと設計技法
# https://algo-method.com/courses/27
# 5: 動的計画法 (1) イントロダクション
# Q5: マスの移動 (2)
# https://algo-method.com/tasks/306

import io
import sys

_INPUT = """\
8 4
3 1 4 1 5 9 2 6
"""

sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())
A = list(map(int, input().split()))
INF = 10**18
DP = [INF] * N
DP[0] = 0
for i in range(1, N):
    for j in range(1, M+1):
        if i - j >=0 and DP[i-j] + j*A[i] < DP[i]:
            DP[i] = DP[i-j] + j*A[i]
print(DP[N-1])