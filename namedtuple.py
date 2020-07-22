from collections import namedtuple
n_records, keys = (int(input()), input().split())
record = namedtuple('record', keys)
records = list(map(lambda x: record(*x), [input().split() for i in range(n_records)]))
print(sum([int(r.MARKS) for r in records]) / n_records)
