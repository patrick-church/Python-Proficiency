GBP_per_USD = 2.13
Dollars = input('Enter the total amount in USD: ')
Dollars_1 = float(Dollars[1:len(Dollars)]) 
Pounds = round(Dollars_1/GBP_per_USD)
print('The total amount in GBP is about', Pounds, 'pounds.')
