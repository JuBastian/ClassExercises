n = int(input("input n"))
summation = 0
for current_number in range(n + 1):
    summation = summation + current_number
print("The summation of the natural numbers from 1 to " + str(n) + " is " + str(summation))
