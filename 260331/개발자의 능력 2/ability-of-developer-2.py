ability = list(map(int, input().split()))

# Please write your code here.
ability.sort()

ability[1], ability[-1] = ability[-1], ability[1]
s1, s2, s3 = sum(ability[0:2]), sum(ability[2:4]), sum(ability[4:6])

answer = max(s1, s2, s3) - min(s1, s2, s3)
print(answer)
