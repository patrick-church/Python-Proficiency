import random
import string
from random import randint, shuffle, sample, choices
import pandas as pd

class PasswordManager:

    def __init__(self, name, master_pw):
        self.__passwords = pd.DataFrame(columns = ['Site','Username','Password'])
        self.__passwords.set_index(['Site'], inplace = True)                                
        self.__name = name
        self.__master_pw = master_pw

    
    
    def __password_specs(self, length = 14, min_spec = 0, max_spec = 0, min_num = 0, min_upper = 0):
        
        if max_spec > length-min_num-min_upper:
            max_spec = length - min_num - min_upper
        num_sc = randint(min_spec, max_spec)
        num_num = randint(min_num, length - num_sc  - min_upper)
        num_upper = randint(min_upper, length - num_sc - num_num)
        num_lower = length - (num_sc + num_num + num_upper)
        return [num_sc, num_num, num_upper, num_lower]
        
  
    def __password_gen(self, criteria = None, length = 14, spec_char = '@!&', repeat = True, min_spec = 0, max_spec = 0, min_num = 0, min_upper = 0):
        if criteria != None:
            keys = criteria.keys()
            if 'length' in keys:
                length = criteria['length']
            if 'spec_char' in keys:
                spec_char = criteria['spec_char']
            if 'repeat' in keys:
                repeat = criteria['repeat']
            if 'min_spec' in keys:
                min_spec = criteria['min_spec']
            if 'max_spec' in keys:
                max_spec = criteria['max_spec']
            if 'min_num' in keys:
                min_num = criteria['min_num']
            if 'min_upper' in keys:
                min_upper = criteria['min_upper']
            
        
        
        
        
            
        
        
        if(max_spec < min_spec): 
            max_spec = min_spec 
        
        required = sum([min_spec, min_num, min_upper]) 
        if required <= length and (repeat or len(spec_char)>=min_spec): 
            specs = self.__password_specs(length, min_spec, max_spec, min_num, min_upper)
            if(repeat): 
                password = random.choices(string.ascii_lowercase, k=specs[3]) + random.choices(string.ascii_uppercase,
                        k=specs[2]) + random.choices(string.digits, k=specs[1]) + random.choices(spec_char, k=specs[0])
            else:
                while specs[0] > len(spec_char) or specs[1] > len(string.digits) or specs[2] > len(string.ascii_uppercase) or specs[3] > len(string.ascii_lowercase):
                    specs = self.__password_specs(length, min_spec, max_spec, min_num, min_upper)
                password = random.sample(string.ascii_lowercase, k=specs[3]) + random.sample(string.ascii_uppercase, k=specs[2]) + random.sample(string.digits, k=specs[1]) + random.sample(spec_char, k=specs[0])
            shuffle(password)
            return ''.join(password)

    def add_password(self, site, username, criteria = None):
            
        password = self.__password_gen(criteria)    
        if site not in self.__passwords.index:
            if password != None:
                self.__passwords.loc[site] = [username, password]
            else: print('Invalid Specifications!')
                
                
        
        
       
            
        
        
        


    def validate(self, mp):
        return mp == self.__master_pw
        
        

    def change_password(self, site, master_pass, new_pass = None, criteria = None):
        if self.validate(master_pass) == False:
            print('Incorrect master password!')
            return False
        if site not in self.__passwords.index:
            print('Site does not exist')
            return False
        if new_pass != None:
            self.__passwords.loc[site, 'Password'] = new_pass
        if new_pass == None:
            self.__passwords.loc[site, 'Password'] = self.__password_gen(criteria = criteria)
        if new_pass in self.__passwords['Password']:
            print('Invalid criteria!')
            return False
        
        

    def remove_site(self, site):
        if site in self.__passwords.index:
            self.__passwords.drop([site], inplace = True)
        
        
        
        

    def get_site_info(self, site):
        
        if site in self.__passwords.index:
            return list(self.__passwords.loc[site])
        
        

    def get_name(self):
        return self.__name
        
        

    def get_site_list(self):
        return list(self.__passwords.index)
        
        
        

   
    def __str__(self):
        return 'Sites stored for '+self.__name +':\n' + ('\n'.join(self.get_site_list()))
