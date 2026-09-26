#def stats(values):
     #sum(values) / len(values), min(values), max(values)
#readings=[22.5,23.1,21.8,24,22.9]
#mean, lo, hi =stats(readings)
#print(f"mean={mean:.2f}, min={lo}, max={hi}")

#packed=stats(readings)
#print("as tuple:",packed,type(packed))

#def greet(name):
  #print("Hello",name)
#result=greet("Alice")
#print("returned:",result)
#print("type:",type(result))

#def safe_divide(a,b):
    #if b==0:
        #return None
    #else:
        #return a/b
#print(safe_divide(10,2))
#print(safe_divide(10,0))

def add_reading(data,value):
    data.append(value)
readings=[10,20]
add_reading(readings,30)
print("caller list is now:", readings)

def rebind(data):
    data=[99]
    return data
readings2=[10,20]
rebind(readings2)
print("caller list unchanged:",readings2)

def total_distance(points):
    total=0
    for i in range(len(points)-1):
        x1,y1=points[i]
        x2,y2=points[i+1]
        total+= ((x2-x1) ** 2+ (y2-y1) ** 2)**0.5
    return total

d=total_distance([(0,0),(3,4)])
print(" distance:",d)
print("is it usable?",d+1 if d is not None else "cannot add to none")