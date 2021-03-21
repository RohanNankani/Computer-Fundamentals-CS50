# Author: Rohan Nankani
# Date: October 13, 2020
# Name of Program: Receipt Assignment
# Purpose: Making a shopping receipt

# Name of the shop
print("Fresh Co".center(40))

# Seperates the shop name from the rest
print ("".center(40, "-"))

# Address of the shop and phone number
print("Leslie & Lakeshore".center(40))
print("731 Eastern Ave, Toronto, ON M4M 3H6".center(40))
print("416-465-7360\n".center(40))

# Name of the person who served and date/time
print(f'{"Served by: Rohan":<21}{"08/10/2020 11:26:09":>0}')

# Seperates the address/name section from items/prices section
print ("".center(40, "-"))

# Item number 1 and price
numberOfItem1 = 6
priceOfItem1 = 0.76
totalItemPrice1 = numberOfItem1 * priceOfItem1
print(f'{"Chicken Noodle Soup":<35}{"$" + str(round(totalItemPrice1, 2))}')
print(f'{str(numberOfItem1) + " @ $" + str(priceOfItem1) + " ea" :>15}')

# Item number 2 and price
numberOfItem2 = 1
priceOfItem2 = 5.99
totalItemPrice2 = numberOfItem2 * priceOfItem2
print(f'{"Khudri Dates":<35}{"$" + str(round(totalItemPrice2, 2))}')

# Item number 3 and price
numberOfItem3 = 4
priceOfItem3 = 4.99
totalItemPrice3 = numberOfItem3 * priceOfItem3
print(f'{"Mina Halal Chicken Leg Quarters":<34}{"$" + str(round(totalItemPrice3, 2))}')
print(f'{str(numberOfItem3) + " @ $" + str(priceOfItem3) + " ea" :>15}')

# Item number 4 and price
numberOfItem4 = 1
priceOfItem4 = 9.99
totalItemPrice4 = numberOfItem4 * priceOfItem4
print(f'{"Nestle Favourites":<35}{"$" + str(totalItemPrice4)}')

# Item number 5 and price
numberOfItem5 = 3
priceOfItem5 = 6.99
totalItemPrice5 = numberOfItem5 * priceOfItem5
print(f'{"Frito-Lay Halloween Chips":<34}{"$" + str(totalItemPrice5)}')
print(f'{str(numberOfItem5) + " @ $" + str(priceOfItem5) + " ea" :>15}')

# Item number 6 and price
numberOfItem6 = 1
priceOfItem6 = 1.49
totalItemPrice6 = numberOfItem6 * priceOfItem6
print(f'{"Large Pumpkin":<35}{"$" + str(totalItemPrice6)}')

# Seperates the items section from the total price section
print ("".center(40, "-"))

# Total price of items purchased without tax
subtotal = totalItemPrice1 + totalItemPrice2 + totalItemPrice3 + totalItemPrice4 +totalItemPrice5 + totalItemPrice6
print(f'{"Subtotal:":>25}{"$" + str(round(subtotal, 2)):>15}')

# Total tax of 13% on the subtotal
totalTax = subtotal * 0.13
print(f'{"Total Tax:":>25}{"$" + str(round(totalTax, 2)):>15}')

# Total price of the items including tax
totalPrice = subtotal + totalTax
print(f'{"TOTAL:":>25}{"$" + str(round(totalPrice, 2)):>15}\n')

# Money given by the customer
amountPaid = 100
print(f'{"Cash:":>0}{"Tender":>19}{"$" + str(round(amountPaid, 2)):>16}')

# Money the customer gets back
cashDue = amountPaid - totalPrice
print(f'{"Cash:":>0}{"Change":>19}{"$" + str(round(cashDue, 2)):>16}\n')

# Number of total items purchased by the customer
totalNumberOfItems = numberOfItem1 + numberOfItem2 + numberOfItem3 + numberOfItem4 + numberOfItem5 + numberOfItem6
print(f'{"Number of Items:":>25}{totalNumberOfItems:>15}\n')

# Information regarding return policy and customer appreciation
print("REFUND POLICY: Please retain receipt for")
print("refund within 14 days of purchase.")
print("CUSTOMER COPY".center(40, "-") + "\n")
print("Thank You for Shopping at Fresh Co!".center(40))