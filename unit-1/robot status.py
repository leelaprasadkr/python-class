#from turtle import speed
#robot = {"name" : "Alpha", "battery" : 78, "mode" : "auto"}
#print(robot)
#print(robot["name"])
#robot["battery"] -= 5
#robot["speed"] = 0.4
#print(robot)
#print(f"list : {list(robot.keys())}")
#print(f"values : {list(robot.values())}")


#robot={"name":"Alpha","battery":78}
#print(robot.get("speed"))
#print(robot.get("speed", 0.0))
#print ("speed" in robot)

#log=["E2","E7","E2","E1","E7","E2"]
#freq={}
#for code in log:
    #freq[code] = freq.get(code,0) + 1
#print(freq)
#for code in sorted(freq, key=freq.get,reverse=True):
    #print(f"{code} occurred {freq[code]} time(s)")

#write a program that counts the frequency of characters in your name , prints each letter with its count and then prints the most frequently occurring letter in your name
name = "LEELA PRASAD KR"
char_freq = {}
for char in name:
    char_freq[char] = char_freq.get(char, 0) + 1
for char in sorted(char_freq, key=char_freq.get, reverse=True):
    print(f"{char} occurred {char_freq[char]} time(s)")
print(f"Most frequent letter: {max(char_freq, key=char_freq.get)}")


errors=["E2","E7"]
print(errors)
errors.append("E2")
print(errors)

a=[1,2,3]
b=a
c=a[:]
b.append(4)
c.append(5)
print("a =", a)
print("b =", b)
print("c =", c)
print("b is a:", b is a, "c is a:", c is a)

readings=[10,-1,-1,20,30]
for r in readings:
    if r==-1:
        readings.remove(r)
print(readings)

readings=[12,45,7,61,33]
doubled=[r*2 for r in readings]
big=[r for r in readings if r>30]
print(doubled)
print(big)
