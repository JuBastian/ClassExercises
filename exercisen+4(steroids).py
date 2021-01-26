import time

options = {
    "1": "Communicating you with the salaries dependency",
    "2": "Communicating you with the boss",
    "3": "Communicating you with firings :)",
    "4": "Communicating you with your mom ._.",
    "5": "I can’t recognize that option, please restart the program",
}

number = input("Please input a number\n")
number = number if number in options.keys() else "5"

print("Please wait a moment")

for _ in range(5):
    time.sleep(0.5)
    print(".")


print(options[number])
