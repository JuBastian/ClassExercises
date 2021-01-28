expected_side = current_side = input("What is the side of your coin after tossing it? ")
toss_number = 0
while(expected_side == current_side):
    toss_number = toss_number + 1
    current_side = input("What is the side of your coin after tossing it? ")
print("You got '" + expected_side + "' " + str(toss_number) + " times in a row!")
