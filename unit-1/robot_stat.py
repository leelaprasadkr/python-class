robot_name="Alpha"
battery_pct=80
is_docked=True
waypoints=16
print(robot_name,battery_pct,is_docked,waypoints)
print(type(robot_name),type(battery_pct),type(is_docked),type(waypoints))

battery=100
print("start: ",battery)
battery=battery-15
print("after: ",battery)
battery-=15
print("again: ",battery)

battery=55
if battery<50:
    print("Charging recommended")
    print("docking now")
print("status check done")
