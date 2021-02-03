n = int(input("input n"))
summation = 0
for current_number in range(2, n + 1, 2):
    summation = summation + current_number
print("The summation of the natural numbers from 1 to " + str(n) + " is " + str(summation))
