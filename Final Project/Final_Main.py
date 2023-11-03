import random
import string
from random import randint, shuffle, sample, choices
import pandas as pd

Hello = PasswordManager('Student', 'FINAL')
Hello.add_password(site = 'www.gmail.com', username = 'a_student')
Hello.add_password('www.wm.edu', 'WMstudent', criteria = {'max_spec': 2, 'min_upper': 2})
Hello.change_password('www.gmail.com', 'FINAL', new_pass = 'update1235')
Hello.get_site_info('www.wm.edu')
print(Hello)
