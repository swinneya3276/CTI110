#Debuging P3HW1
# Swinney


# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list
print()
print("------------Results------------")
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades
length = len(grades)
lowest = min(grades)
highest = max(grades)
total = sum(grades)
average = total/length

print("Lowest Grade:", lowest)
print("Highest Grade:", highest)
print("Sum of Grades:", total)
print("Average:", average)
print()
print("-----------------------------------------------")

# determine letter grade for average


if average >= 90:
    print("Your grade is: A")
elif average >= 80:
    print("Your grade is: B")
elif average >= 70:
    print("Your grade is: C")
elif average >= 60:
    print("Your grade is: D")
else:
    print("Your grade is: F")





