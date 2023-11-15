# アルゴリズムと設計技法
# https://algo-method.com/courses/27
# 5: 動的計画法 (1) イントロダクション
# Q4: タイルの敷き詰め
# https://algo-method.com/tasks/305

import io
import sys

_INPUT = """\
10
"""

sys.stdin = io.StringIO(_INPUT)

N = int(input())
DP = [1, 1, 2]
DP[0], DP[1], DP[2] = 1, 1, 2
for i in range(3, N+1):
    DP.append(DP[i-3] + DP[i-2] + DP[i-1])
print(DP[N])

""" RE when N =1
N = int(input())
DP = [-1] * (N+1)
DP[0], DP[1], DP[2] = 1, 1, 2
for i in range(3, N+1):
    DP[i] = DP[i-3] + DP[i-2] + DP[i-1]
print(DP[N])
"""