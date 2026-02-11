n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.
str_w_t = [s for s in str if s[:len(t)] == t]
print(sorted(str_w_t)[k-1])