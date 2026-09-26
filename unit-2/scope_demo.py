count=0
def tick():
    count=0
    count+=1
    return count
print(tick(),tick(),count)

threshold = 70
def is_alert(value):
    return value>threshold
print(is_alert(85),is_alert(60))

#count=0
#def tick():
    #count= count +1
    #return count
#print(tick())

count=0
def tick():
    global count
    count+=1
    return count
print(tick(),tick(),tick())
print("global count is now:",count)

def tick(count):
    return count+1
count=0
count=tick(count)
count=tick(count)
print("count :",count)

def make_report():
    lines=["Header"]
    lines.append("Body")
    return len(lines)
print(make_report())
print(make_report())
print("lines" in dir())


