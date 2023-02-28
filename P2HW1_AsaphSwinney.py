#This program calculates and displays travel expenses
#2/16/2023
#CTI-110 P1HW2
#Asaph Swinney
print("This progran calculates and displays travel expenses")
print()
#Declare variable and datatype 
#Display ("Enter Budget: ")
budget = float(input("Enter Budget: "))
print()
#Declare variable and datatype
#Display ("Enter your travel destination: ")
travelDestination = str(input("Enter your travel destination: "))
print()
#Declare variable and datatype
#Display ("How much do you think you will spend on gas? ")
gas = float(input("How much do you think you will spend on gas? "))
print()

hotel = float(input("Appoximately, how much will you need for accomodation/hotel? "))
print()

food = float(input("Last, how much do you need for food? "))
print()

print("------------Travel Expenses------------")

print("Location:            ", travelDestination)
print("Initial Budget:     $", budget)
print()
print("Fuel:               $",  gas)
print("Accomodation:       $", hotel)
print("Food:               $", food)
print()
print("----------------------------------------")
balance =  budget - (gas + hotel + food)
print("Remaining Balance:  $", balance )
