import time

print("Please input a number")
number = input()
print("Please wait a moment")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
if number == "1":
    print("Communicating you with the salaries dependency")
elif number == "2":
    print("Communicating you with the boss")
elif number == "3":
    print("Communicating you with firings :)")
elif number == "4":
    print("Communicating you with your mom ._.")
else:
    print("I can’t recognize that option, please restart the program")
