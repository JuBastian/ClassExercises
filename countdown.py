import time

print("Continue?")
for countdown in range(10, -1, -1):
    print(countdown)
    time.sleep(1)
print("You Lose")
