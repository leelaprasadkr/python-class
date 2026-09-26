#position = (4.2, 7.8)
#print(position, type(position))
#x, y = position
#print(f"x = {x} and y = {y}")
#single = (5, )
#print(single, type(single))

#codes=["E2","E7","E2","E1","E7"]
#print("raw :",(codes))
#print("unique :", set(codes))
#print("unique count:", len(set(codes)))

#write a pogram to simulate a robot visiting grid cells.start with an empty set ,add 8 coordinates of which 3 repeats,then print how many distinct cells were visited and test whether (2,2) was among them

coords = set()
coords.add((0, 0))
coords.add((0, 1))
coords.add((0, 2))
coords.add((0, 3))
coords.add((0, 2))
coords.add((1, 2))
coords.add((1, 1))
coords.add((0, 1))

print(coords)
print(len(coords))
print((2, 2) in coords)