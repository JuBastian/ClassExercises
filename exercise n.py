print("Please input the 5 scores of your student:")
score_1 = float(input())
score_2 = float(input())
score_3 = float(input())
score_4 = float(input())
score_5 = float(input())
average = (score_1 + score_2 + score_3 + score_4 + score_5) / 5
print("The overall score of your student is: " + str(average))
if average >= 3.0:
    print("Passed")
    if average == 5.0:
        print("Best student")
else:
    print("Lost")
print("This code will be executed")
