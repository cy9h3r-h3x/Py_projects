#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

#Print a welcome message

print("Are you confused when Tipping and Splitting your bills?, I can help you!\n\n")

#Recieving all the needed inputs, storing into variables and converting them into floats or int

total_bill = float(input("What's your total reciept amount?\n"))

total_num_ppl = int(input("How many of you are there?\n"))

tip_in_percentage = float(input("How much percent you wanna tip in?\n"))


#Calculating the tip amount

tip_amount = (tip_in_percentage / 100) * total_bill

#Adding tip amount to the total bill 

final_bill = tip_amount + total_bill

#Dividing the reciepts by number of persons and rounding

per_head_amount = "{:.2f}".format(final_bill / total_num_ppl)

#Printing the rounded per head amount of the reciept

print(f"Each one of you will have to pay  {per_head_amount} Rupees")
