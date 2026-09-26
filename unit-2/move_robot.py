def move_robot(x,y,speed=1.0):
    print(f"Moving robot to {x}, {y} at speed {speed}m/s")
move_robot(3,4)
move_robot(3,4,0.5)
move_robot(y=3,x=4)
move_robot(3,speed=2,y=4)

def move(x,y,speed=1.0):
    print(x,y,speed)

move(3,4)

def log(*values,**options):
    print("values:", values)
    print("options:", options)

log("start")
log("waypoint",3,4.5)
log("alert",level="high",retries=2)
log()


def add_waypoint(wp, route=None):
    if route is None:
        route=[]
    route.append(wp)
    return route
r1=add_waypoint((0,0))
r2=add_waypoint((5,5))
print("r1 =",r1)
print("r2 =",r2)
print("same objects?",r1 is r2)