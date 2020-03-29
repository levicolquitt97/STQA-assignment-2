#LEVI COLQUITT
#Assignment 2 STQA
#3/15/2020
#The following code will calculate the BMI or retirement savings as dictated by the user

#BEGIN
def main():
    option = 0
    #Loop to handle error of out of range choice and continuous running
    while option < 3:
        # Get the users calculation choice then compute
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

            #Getting user input to calculate retiremenet savings
            age = int(input("Enter your current age, (greater than 0 and less than 100):"))
            while (age > 100 or age <= 0):
                age = int(input("\nINPUT IN THE VALID RANGE: Enter your current age, (more than 0 and less than 100):"))

            salary = int(input("Enter annual salary, (in dollars and greater than 0):"))
            while (salary <= 0):
                salary = int(input("\nINPUT IN THE VALID RANGE: Enter annual salary, (in dollars and greater than 0):"))

            percent_saved = float(input("Enter annual percent of salary saved, (enter whole number less than 100):"))
            while (percent_saved >= float(100)):
                percent_saved = float(input("\nINPUT IN THE VALID RANGE: Enter annual percent of salary saved, (enter whole number):"))

            desired_savings_goal = int(input("Enter your desired savings goal, (lump sum amount in dollars): "))

            #variables needed for the loop and to count up savings plus employer match
            i = int(0)
            savings = int(0)
            employer_match = .35
            while i <= (100-age):
                if i == (100-age):
                    print("We are sorry but your savings goal was not met with in life expectancy (100 years).\n You managed to save:", savings, "by age 100")
                savings = float((salary * (percent_saved/100)) + savings)
                bonus = ((salary*(percent_saved/100)) *.35)
                savings = savings + bonus
                age += 1
                if savings >= desired_savings_goal:
                    savings = int(savings)
                    print("You will have saved: $",savings, "By age:", age, "Which meets your savings goal of: $",desired_savings_goal)
                    i = int(101)


        #Determines what user wants to calcuate and calls said function (or exits)
        if option == 1:
            print("\nLets Calculate BMI!\n")
            BMI(option)
        elif option == 2:
            print("\nLets Calculate Retirement savings!\n")
            Retirement(option)
        elif option == 0:
            print("\nGoodbye!\n")
            exit()
        else:
            print("\nTry again with a valid option\n")
            option = 0


main()







