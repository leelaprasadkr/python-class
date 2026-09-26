heading=359
turn=5
print("wrong:",heading+turn)
print("right:",(heading+turn) % 360)
print("negative:",(30) % 360)

distance=8.0
limit=10
print(distance<limit)
print(distance==limit)
print(0 <= distance<limit)


battery=45
print(distance>5 and battery>20)
print(distance>5 or battery>90)
print(not(distance>5))

distance=10
speed=5
print("time:",distance/speed)

#write a python program with a single expression that is true only when the robot is safe to move :distance>10,battery above 20 and not currently docked
safe_to_move = distance > 10 and battery > 20 and not docked
print("Safe to move:", safe_to_move)    
