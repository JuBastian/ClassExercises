cost_limit = 5000000.0
duration_limit_in_years = 3.0
print("Please input the cost of the project")
cost = float(input())
print("Please input the duration of the project in years")
duration_in_years = float(input())
if (cost <= cost_limit) and (duration_in_years <= duration_limit_in_years):
    print("Start the project")
else:
    print("Do not start the project")
print("Thanks for using our software")
