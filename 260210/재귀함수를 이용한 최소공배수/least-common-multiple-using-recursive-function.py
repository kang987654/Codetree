n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def my_lcm(i, n_list):
    if i == -1:
        answer = 1
        for n in n_list:
            answer *= n
        return answer

    if arr[i] in prime and arr[i] not in n_list:
        n_list.append(arr[i])
    if arr[i] == 4:
        for _ in range(2 - n_list.count(2)):
            n_list.append(2)
    if arr[i] == 6:
        for _ in range(1 - n_list.count(2)):
            n_list.append(2)
        for _ in range(1 - n_list.count(3)):
            n_list.append(3)
    if arr[i] == 8:
        for _ in range(3 - n_list.count(2)):
            n_list.append(2)
    if arr[i] == 9:
        for _ in range(2 - n_list.count(3)):
            n_list.append(3)
    if arr[i] == 10:
        for _ in range(1 - n_list.count(2)):
            n_list.append(2)
        for _ in range(1 - n_list.count(5)):
            n_list.append(5)
    
    return my_lcm(i-1, n_list)


    
    
prime = [1, 2, 3, 5, 7]
n_list = []

print(my_lcm(n-1, n_list))