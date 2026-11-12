user2_id, user2_level = input().split()
user2_level = int(user2_level)


class info :
    def __init__(self, a = 'codetree', b = 10) :
        self.user_id = a
        self.user_level = b

user1 = info()
user2 = info(user2_id, user2_level)

print(f"user {user1.user_id} lv {user1.user_level}")

print(f"user {user2.user_id} lv {user2.user_level}")
