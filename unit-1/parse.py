raw="Alpha Rover"
print(f"[{raw}]")
print(raw.strip().lower())
print(raw.strip().upper())
print(raw.strip().replace("",""))
print("Rover in Raw")

#Write a python program to parse the following packet and print the values of temperature, humidity and pressure into labelled values.

packet="T:25.4;H:40.2;P:1013.25"
fields=packet.split(";")
print(fields)
for field in fields:
    key, value = field.split(":")
    print(f"{key} = {value}")

packet="T:25.4;H:40.2;P:1013.25"
fields=packet.split(";")
temp=fields[0].split(":")[1]
humidity=fields[1].split(":")[1]
pressure=fields[2].split(":")[1]
print(f"Temperature: {temp}, Humidity: {humidity}, Pressure: {pressure}")