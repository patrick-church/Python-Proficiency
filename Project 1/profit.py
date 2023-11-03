Market_Rate = float(input('Enter the CAD/USD Market exchange rate: '))
Bank_Rate = float(input('Enter the CAD/USD Bank exchange rate: '))
Difference =  Bank_Rate - Market_Rate
Percentage_Markup = round((Difference / Market_Rate) * 100)
print('Percentage markup is', str(Percentage_Markup)+'%.')
