secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.
class Bond:
    def __init__(self, code, place, time):
        self.code = code
        self.place = place
        self.time = time

james = Bond(secret_code, meeting_point, time)
print(f'secret code : {james.code}')
print(f'meeting point : {james.place}')
print(f'time : {james.time}')