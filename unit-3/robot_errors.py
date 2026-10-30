# class LowBatteryError(Exception):
#     def start_mission(battery):
#         if battery<10:
#             raise LowBatteryError(f"battery at {battery}%")
#         print(f"mission started ({battery}%)")

# start_mission(85)
# try:
#     start_mission(7)
# except LowBatteryError as error:
#     print("aborted:",error)
class RobotError(Exception):
    pass
class LowBatteryError(RobotError):  
    pass
class ObstacleError(RobotError):
    pass
def step(battery,distance):
    if battery<10:
        raise LowBatteryError(f"battery at {battery}%")
    if distance<5:
        raise ObstacleError(f"obstacle at {distance}cm")
    return "moved"
for battery,distance in [(80,50),(5,50),(80,3)]:
    try:
       print(step(battery,distance))
    except RobotError as e:
        print(f"{type(e).__name__}: {e}")   