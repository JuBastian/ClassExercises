import time

print("Please input a number")
number = input()
print("Please wait a moment")
time.sleep(0.5)
print(".")
time.sleep(0.5)
print(".")
time.sleep(0.5)
print(".")
time.sleep(0.5)
print(".")
time.sleep(0.5)
print(".")
if number == "1":
    print("Communicating you with the salaries dependency")
elif number == "2":
    print("Communicating you with the boss")
elif number == "3":
    print("Communicating you with firings :)")
elif number == "4":
    print("Communicating you with your mom ._.")
elif number == "5":
    print("You are fired")
elif number == "6":
    print("Thanks for using our fantastic software")
else:
    print("I can’t recognize that option, please input a different number")

while(number != "5" and number != "6"):
    print("Please input a number")
    number = input()
    print("Please wait a moment")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    if number == "1":
        print("Communicating you with the salaries dependency")
    elif number == "2":
        print("Communicating you with the boss")
    elif number == "3":
        print("Communicating you with firings :)")
    elif number == "4":
        print("Communicating you with your mom ._.")
    elif number == "5":
        print("You are fired")
    elif number == "6":
        print("Thanks for using our fantastic software")
    else:
        print("I can’t recognize that option, please input a different number")
