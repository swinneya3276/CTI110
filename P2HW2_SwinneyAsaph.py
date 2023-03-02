grade_one= float(input("Enter grade for Module 1: "))
grade_two= float(input("Enter grade for Module 2: "))
grade_three = float(input("Enter grade for Module 3: "))
grade_four = float(input("Enter grade for Module 4: "))
grade_five = float(input("Enter grade for Module 5: "))
grade_six = float(input("Enter grade for Module 6: "))


num_list = [grade_one, grade_two, grade_three, grade_four, grade_five, grade_six]

length = len(num_list)
total = sum(num_list)
average = total/length
highest = max(num_list)
lowest = min(num_list)
print()
print("------------Results------------")
print("Lowest Grade: ", lowest)
print("Highest Grade: ", highest)
print("Sum of Grades: ", total)
print("Average: ", average)
print("----------------------------------------------")
