CURRENCY = ['AUD', 'ZAR', 'EUR', 'INR'] #Do not change
CURRENCY_BY_USD = [0.7278, 0.0669, 1.1765, 0.0135] #Do not change

Home_Currency = int(input('Select your home currency: 1 for AUD, 2 for ZAR, 3 for EUR, 4 for INR: '))
Destination_Currency = int(input('Select your destination currency: 1 for AUD, 2 for ZAR, 3 for EUR, 4 for INR: '))
Total_Home_Currency = input('Enter total amount in home currency: ')

Total_Home_Currency_1 = float(Total_Home_Currency[:-3])
Exchanged_Value = round(Total_Home_Currency_1*CURRENCY_BY_USD[Home_Currency -1]/CURRENCY_BY_USD[Destination_Currency -1])
print('The total amount in', CURRENCY[Destination_Currency -1], 'is about', str(Exchanged_Value)+'.')
