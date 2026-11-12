unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)


class bomb :
    def __init__(self, a, b, c) :
        self.code = a
        self.color = b
        self.second = c


info = bomb(unlock_code, wire_color, seconds)

print(f"""code : {info.code}
color : {info.color}
second : {info.second}""")