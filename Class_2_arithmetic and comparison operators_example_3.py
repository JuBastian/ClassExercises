print("Please input the number of present students in the room ")
number_of_present_students = int(input())
print("Please input the number of groups for the activity ")
number_of_groups = int(input())
possible_number_of_groups = number_of_present_students//number_of_groups
print("The number of the possible groups is " + str(possible_number_of_groups))
students_without_group = number_of_present_students % number_of_groups
print("The number of the students without a group is " + str(students_without_group))

