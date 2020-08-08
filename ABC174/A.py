import io
import sys
_INPUT="""\
    40
"""
sys.stdin=io.StringIO(_INPUT)


N=int(input())
print("Yes" if N>=30 else "No")