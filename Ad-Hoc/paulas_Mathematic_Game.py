# Solution for Ad-Hoc 1192.

def paulasMath(op):
    op = [int(op[0]), op[1], int(op[2])]

    if op[0] == op[2]:
        return op[0] * op[2]
    elif str.isupper(op[1]):
        return op[2] - op[0]
    elif str.islower(op[1]):
        return op[0] + op[2]

N = int(input())

for n in range(N):
    op = input() # receives operation
    print(paulasMath(op))
