# アルゴリズムと設計技法
# https://algo-method.com/courses/27
# 5: 動的計画法 (1) イントロダクション
# Q2: マスの移動 (1)
# https://algo-method.com/tasks/303

import io
import sys

_INPUT = """\
8
3 1 4 1 5 9 2 6
"""

sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int, input().split()))
DP = [0] * N
DP[1] = A[1]
for i in range(2, N):
    step1 = DP[i-1] + A[i]
    step2 = DP[i-2] + A[i]*2
    if step1 <= step2: DP[i] = step1
    else:              DP[i] = step2
print(DP[N-1])