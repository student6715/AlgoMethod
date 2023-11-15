# アルゴリズムと設計技法
# https://algo-method.com/courses/27
# 5: 動的計画法 (1) イントロダクション
# Q1: 数字の列
# https://algo-method.com/tasks/302

import io
import sys

_INPUT = """\
31 41 59
"""

sys.stdin = io.StringIO(_INPUT)

N, X, Y = map(int, input().split())
A = [0] * N
A[0], A[1] = X, Y
for i in range(2, N):
    A[i] = (A[i-2] + A[i-1]) % 100
print(A[N-1])