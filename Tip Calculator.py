principal = 0.0
tipPercentage = 0


#Get User Input

principal = float(input("Welcome to the Tip Calculator! Please input your total price: "))

while principal == 0.:
        if principal < 0.:
            print ("Please enter a value greater than 0. Please enter a value greater than 0")
            principal = float(input("Welcome to the Tip Calculator! Please input your total price: "))
        else:
            principal = principal
    
print("\nHere are the 3 most common tip amounts that we will use in our program. Please select a percentage by entering the number next to the percentage.\n1: 15%\n2: 18%\n3: 20%")
tipAmount = float(input("\nNow enter your desired tip amount from the choices above:"))

#Determine Which TIp Amount to Use
while tipPercentage == 0:
    if tipAmount == 1:
        tipPercentage = 0.15
    elif tipAmount == 2:
        tipPercentage = 0.18
    elif tipAmount == 3:
        tipPercentage = 0.20
    else:
        print("Please enter a value given from the displayed values.")
        tipAmount = float(input("\nNow enter your desired tip amount from the choices above: "))


#Calculate Tip Amount
finalTip = principal * tipPercentage
finalAmount = finalTip + principal

displayedTip = tipPercentage*100


#Output Final Tip and Price
print(f"\nYour final price is ${finalAmount:.2f}, with ${finalTip:.2f} being the tip at {displayedTip}%")

#End Program
endProgram = input("\nThank you for using my program!Please press 'Enter' to exit the program.")
