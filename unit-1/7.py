packet = "T:25.4;H:60;B:78"

data = {}

parts = packet.split(";")

for part in parts:
    key, value = part.split(":")
    data[key] = float(value)

print(data)

for key, value in data.items():
    print(key, value)