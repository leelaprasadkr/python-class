# reading="abc"
# value=int(reading)
# print("this line never runs")
# text=input("Enter a reading: ")
# try:
#     value=int(text)
#     print("doubled:",value*2)
# except ValueError:
#     print("that was a whole number")
# print("program continues")
# print("1. before try")
# try:
#     print("2. inside try, before the risky line")
#     x=10/0
#     print("3. inside try, after the risky line")
# except ZeroDivisionError:
#     print("4. inside except")
# print("5. after the whole try except statement")
# try:
#     v_min=float(input("v_min:"))
#     v_max=float(input("v_max:"))
#     gain=5.0/(v_max-v_min)
#     print("gain=",gain)
# except ZeroDivisionError:
#     print("flt sensor:v_max equals v_min")
# except ValueError:
#     print("numeric input required ")
# try:
#     speed=float(input("speed:"))
#     eta = 120/speed
#     print("eta:",eta)
# except Exception:
#     print("something went wrong")
# except ZeroDivisionError:
#     print("speed cannot be zero") 
# try:
#     value =float(input("reading:"))
#     print("scaled:",value*2)
# except:
#     print("please enter a number")
#write a program that reads two numbers and prints their quotient . handle value error and zero divisionn error with different messages
# try:
#     num1=float(input("Enter number:"))
#     num2=float(input("Enter number:"))
#     quotient=num1//num2
# except ZeroDivisionError:
#     print("Invalid")
# except ValueError:
#     print(" Value Error")
# print("Quotient :",quotient)
# def average_speed(distance_text,time_text):
#     try:
#         speed=float(distance_text)/float(time_text)
#     except ValueError:
#         print("invalid number")
#     except ZeroDivisionError:
#         print("time cannot be zero")
#     else:
#         print("speed=",speed,"m/s")
#     finally:
#         print("[sensor released]")
# print("case 1:"); average_speed("100","20")
# print("case 2:"); average_speed("100","20")
# print("case 3:"); average_speed("abc","20")
# def parse(text):
#     return int(text)
# def load_reading(text):
#     return parse(text)*2
# def main():
#     print(load_reading("21"))
#     print(load_reading("x"))

# main()
# def parse(text):
#     return int(text)
# def load_reading(text):
#     return parse(text)*2
# def main():
#     for text in ["21","x","5"]:
#         try:
#             print(text)