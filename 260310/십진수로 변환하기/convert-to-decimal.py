binary = input()

# Please write your code here.
dec = 0
i = 0
for b in binary[::-1]:
    dec += int(b) * 2**i
    i += 1

print(dec)
