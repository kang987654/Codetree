n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
def part_sum(a1, a2):
    return sum(arr[a1-1:a2])

for q in queries:
    print(part_sum(q[0], q[1]))