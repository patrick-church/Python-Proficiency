passwords = []    
counter = 0
while counter < 4:
    passwords += [password_gen()]
    counter += 1
print(passwords)
criteria = True
for x in passwords:
    if check_password(x) != True:
        criteria = False 
print(criteria)
