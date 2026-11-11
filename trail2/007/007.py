secret_code, meeting_point, time = input().split()
time = int(time)


class Secret :
    def __init__(self, a, b, c) :
        self.code = a
        self.point = b
        self.time = c


secret_section = Secret(secret_code, meeting_point, time)

print(f"secret code : {secret_section.code}")
print(f"meeting point : {secret_section.point}")
print(f"time : {secret_section.time}")