"""My name is Dora, and I am the author of this code.
   The name of this program is the taxes and tips calculator.
   Its function is to calculate the total amount a person would pay based on the price of the meal, the tax percentage, and the tip percentage.
"""

#The print command will produce the first line of the output. It's in quote because it's a string.
print "Welcome to the taxes and tip calculator!"

#The raw_input function takes the input of the user and stores it in the assigned variable. The first is meal. Wrapping raw_input in float ensures the value the user inputs will be stored as a float, which is necessary to do math with it.
meal = float(raw_input("What is the price befor tax? "))

#The second variable the program needs is the tax. 
tax = float(raw_input("What are the taxes? (in %) "))

#The third variable the program needs is the tip.
tip = float(raw_input("What do you want to tip? (in %) "))

#Because the program asked for the tax in a percentage, it needs to be converted to a decimal.
tax = tax / 100

#Because the program asked for the tip in a percentage, it needs to be converted to a decimal.
tip = tip / 100

#Now we can reassign meal to include the tax cost.
meal = meal + meal * tax

#Now we can calculate the total, including the tip.
total = meal + meal * tip

#Now the program prints the total using the % operand
print "The price you need to pay is: $%.6f." % (total)
