n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
sum_nums = [sorted(nums)[i] + sorted(nums, reverse=True)[i] for i in range(n)]
print(max(sum_nums))