TRANSACTION_FEE = '5%' #Do not change
Credit_Limit = input('Enter the credit limit amount: ') #Do not change, will be in format $100
Money_Spent = input('Enter money spent per transaction: ') #Do not change, will be in format $100
Money_Deduc = float(Money_Spent[1:len(Money_Spent)]) + float(Money_Spent[1:len(Money_Spent)]) * int(TRANSACTION_FEE[0])/100 #money deducted from the credit limit per transaction
No_Of_Transaction = int(float(Credit_Limit[1:len(Credit_Limit)])//(Money_Deduc)) #calculating total number of transaction
print('The total number of transactions possible are', str(No_Of_Transaction)+'.')
