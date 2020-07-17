n1 = int(input())
set1 = set([int(x) for x in input().split()])
assert n1 == len(set1)
n2 = int(input())
set2 = set([int(x) for x in input().split()])
assert n2 == len(set2)

symdiff = []

union = set1 | set2
for val in union:
    if not (val in set1 and val in set2):                         
        symdiff.append(val)

for val in sorted(symdiff):
    print(val)
