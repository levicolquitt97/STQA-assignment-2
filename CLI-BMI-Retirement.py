#LEVI COLQUITT
#Assignment 2 STQA
#3/15/2020
#The following code will calculate the BMI or retirement savings as dictated by the user

#Get the users calculation choice then compute

print("Select an option to compute")
option = int(input("(1) Calculate BMI \n(2) Calculate retirement age \n(0) EXIT\n :"))
print(option)






#BMI class that will calculate our BMI given input in feet, inches, and pounds
def BMI(option):
    #user input of desired body characteristics
    feet = int(input("Enter your height in feet:"))
    inches = int(input("Enter your height in inches:"))
    weight = int(input("Enter your weight in pounds:"))

    #Math to convert to metric
    feet_in_inches = (feet * 12)
    height = (feet_in_inches + inches)
    metric_height = (height * .025)
    print(metric_height)
    metric_weight = (weight * .45)
    print(metric_weight)
    height_squared = float(metric_height * metric_height)
    BMI = (metric_weight/height_squared)

    #Determines "health" category based upon BMI
    if BMI <= 18.5:
        weight_category = ("Underweight")
    if BMI >= 18.5 and BMI <= 24.9:
        weight_category = ("Normal weight")
    if BMI >= 25 and BMI <= 29.9:
        weight_category = ("Overweight")
    if BMI >= 30:
        weight_category = ("Obese")

    #Print results to user
    print("results:")
    print("BMI:")
    print(BMI)
    print("Category:")
    print(weight_category)

def Retirement(option):
    e = 1




#Determines what user wants to calcuate and calls said function (or exits)
if option == 1:
    print("Lets Calculate BMI!")
    BMI(option)
elif option == 2:
    print("Lets Calculate Retirement savings!")
    Retirement(option)
elif option == 0:
    print("Goodbye!")
    exit()
else:
    print("try again with a valid option")








