user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Please write your code here.
class NextLevel:
    def __init__(self, id='codetree', lv=10):
        self.id = id
        self.lv = lv

user1 = NextLevel()
user2 = NextLevel(user2_id, user2_level)

print(f'user {user1.id} lv {user1.lv}')
print(f'user {user2.id} lv {user2.lv}')
