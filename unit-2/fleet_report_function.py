def battery_band(pct):
    if pct < 15:
        return "Critical"
    elif pct < 30:
        return "Low"
    else:
        return "OK"
print(f"alpha: {battery_band(8)}")
print(f"beta: {battery_band(22)}")   