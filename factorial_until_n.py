n = int(input("input n"))
factorial = 1
for current_number in range(n + 1):
    if current_number > 0:
        factorial = factorial * current_number
print("The factorial of the natural numbers from 1 to " + str(n) + " is " + str(factorial))

factorial = 1
for current_number in range(1, n + 1):
    factorial = factorial * current_number
print("The factorial of the natural numbers from 1 to " + str(n) + " is " + str(factorial))
