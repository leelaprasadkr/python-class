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
# def read_sensor():
#     try:
#         print("reading sensor")
#         return 42
#     finally:
#         print("finally runs before the value is handed back")
# print("got:",read_sensor())
# for text in ["42","abc",""]:
#     try:
#         print(int(text))
#     except ValueError as e:
#         print(type(e).__name__,"->",e)
# for pair in [("10","2"),("10","0"),("ten","2")]:
#     try:
#         print(int(pair[0])/int(pair[1]))
#     except (ValueError,ZeroDivisionError) as e:
#         print("bad input:",type(e).__name__,e)
# def set_heading(degrees):
#     if not 0<=degrees<360:
#         raise ValueError(f"heading must be 0-359, got {degrees}")
#     print("heading set to 0",degrees)
# set_heading(90)
# try:
#     set_heading(400)
# except ValueError as e:
#     print("rejected:",e)
#Write get percentage(prompt) that keeps asking until the user enters a number between 0 and 100, using try/except inside a while True loop, and returns the value.
# while True:
#     try:
#         percentage = float(input("Enter a percentage (0-100): "))
#         if 0 <= percentage <= 100:
#             break
#         else:
#             print("Please enter a number between 0 and 100.")
#     except ValueError:
#         print("Invalid input. Please enter a numeric value.")
