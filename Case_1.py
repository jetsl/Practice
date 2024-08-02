import random

A=[random.randint(-100, 100) for r in range(10)]
print(f'random list A = {A}')

def find_sum(A):
    b=A.index(min(A))
    c=A.index(max(A))
    if c<b:
        c,b=b,c
    print(f'extremum {A[b]} and {A[c]}')
    A=A[b+1:c]
    print(f'list between min and max {A}')
    total=0
    for i in A:
        if i<0:
            total+=i
    print(f'Sum of negative = {total}')

find_sum(A)