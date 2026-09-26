temp=45
if temp>40:
    print("cooling on")
print("check complete")

if temp<0:
    mode="heater on"
elif temp<=40:
    mode="normal"
elif temp<+60:
    mode="cooling"
else:
    mode="shutdown"
