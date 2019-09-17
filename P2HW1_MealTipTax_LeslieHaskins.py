#Tip, Tax and Total Cost of Meal
#09/16/2019
#CTI-110 P2HW1- Meal Tip Tax Calculator
#Leslie Haskins

#1. Get the cost of the meal
#2. Get the tip amount
#3. Get the tax amount
#4. Multiply the cost of the meal by the tip amount
#5. Multiply the cost of the meal by the tax amount
#6. Display the result of the calculation that was performed in step 4
#7. Display the result of the calculation that was performed in step 5
#8. Display the total result by adding step 1, step 4 and step 5 together


#get cost for meal
meal = float (input("Enter amount of meal:$"))

#get tip amount 
tax = float (input("Enter tax amount:"))

#get tax amount
tip = float (input("Enter tip amount:"))

print ("The tip amount is", format(meal * tip, ".2f"))
print ("The tax amount is", format(meal * tax, ".2f"))

total = meal + meal *tip + meal *tax

print ("The total cost is of the meal is $", format(total, ".2f"))




                    
