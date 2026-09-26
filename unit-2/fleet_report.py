r1_battery = 8

if r1_battery < 15:
    print("alpha: Critical")

elif r1_battery < 30:
    print("alpha: Low")

else:
    print("alpha: OK")


r2_battery1 = 22

if r2_battery1 < 15:
    print("beta: Critical")

elif r2_battery1 < 30:
    print("beta: Low")

else:
    print("beta: OK")


r3_battery = 76

if r3_battery < 15:
    print("gamma: Critical")

elif r3_battery < 30:
    print("gamma: Low")

else:
    print("gamma: OK")




def battery_band(pct):
    if pct < 15:
        return "Critical"
    elif pct < 30:
        return "Low"
    else:
        return "OK"

fleet = {"Alpha": 8, "Beta": 22, "Gamma": 76,"Delta": 45}
for name, pct in fleet.items():
    print(f"{name:<7} {pct:>3}% {battery_band(pct)}")



def battery_band(pct):
    if pct < 15:
        return "Critical"
    elif pct < 30:
        return "Low"
    else:
        return "OK"

print(battery_band.__doc__)
help(battery_band)