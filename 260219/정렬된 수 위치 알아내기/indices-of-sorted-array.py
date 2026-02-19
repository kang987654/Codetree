n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.
seq_w_originindex = [[i+1, sequence[i]] for i in range(n)]
seq_w_sortedindex = sorted(seq_w_originindex, key=lambda seq: seq[1])
for i in range(n):
    seq_w_sortedindex[i].append(i+1)

for i, n, s in sorted(seq_w_sortedindex, key=lambda seq: seq[0]):
    print(s, end=' ')
