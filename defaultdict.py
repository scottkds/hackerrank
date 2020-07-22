from collections import defaultdict

n, m = list(map(int, input().split()))

A = defaultdict(list)
for i in range(n):
    word = input()
    A[word].append(i +1)

for i in range(m):
    word = input()
    if word in A:
        print(*A[word])
    else:
        print(-1)
