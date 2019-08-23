# 

from math import sqrt
from pprint import pprint

def cholesky(A):
    n = len(A)

    L = [[0.0] * n for i in xrange(n)]

    for i in xrange(n):
        for k in xrange(i+1):
            tmp_sum = sum(L[i][j] * L[k][j] for j in xrange(k))

            if (i == k):
                L[i][k] = sqrt(A[i][i] - tmp_sum)
            else:
                L[i][k] = (1.0 / L[k][k] * (A[i][k] - tmp_sum))
    return L

A = [[6, 9, 5, 6], [8, 1, 4, 9], [1, 12, 1, 2], [9, 2, 7, 11]]
L = cholesky(A)

print "A:"
pprint(A)

print "L:"
pprint(L)
