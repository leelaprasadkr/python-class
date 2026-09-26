battery=100
minutes=0
while battery>20:
    minutes+=1
    print(f"minutes {minutes:2d}->battery {battery}%")
print("Alert")


while True:
    text=input("Enter battery%(0-100):")
    value=float(text)
    if 0<=value <=100:
        break
    print("out of range, try again")
print("accepted:",value)

#write a python program 
