import string
import random
from random import choices, sample, choice, shuffle, randint


def password_specs(length = 14, min_spec = 0, min_num = 0, min_upper = 0):
    a = min_spec
    b = min_num
    c = min_upper
    spec = random.randint(a, (length-b-c))
    num = random.randint(b, (length -spec-c))
    upper = random.randint(c, (length-spec-num))
    lower = length-spec-num-upper
    return [spec, num, upper, lower]



def password_gen(length = 14, spec_char = '*&@', repeat = False, min_spec = 2, min_num = 0, min_upper = 1):
    required = min_upper + min_num + min_spec
    if required <= length and (repeat or len(spec_char) >= min_spec):
        specs = password_specs(length, min_spec, min_num, min_upper)
        if repeat:
            password = random.choices(string.ascii_lowercase, k=specs[3]) + random.choices(string.ascii_uppercase, k=specs[2]) + random.choices(string.digits, k=specs[1]) + random.choices(spec_char, k=specs[0])
        else:
            ok = False #DO NOT CHANGE THIS LINE
            while (not ok): #DO NOT CHANGE THIS LINE
                if specs[0] > len(spec_char) or specs[1] > len(string.digits) or specs[2] > len(string.ascii_uppercase): #or specs[3] > len(string.ascii_lowercase):
                    specs = password_specs(length, min_spec, min_num, min_upper)
                else:
                    ok = True #DO NOT CHANGE THIS LINE
            password = random.sample(string.ascii_lowercase, specs[3]) + random.sample(string.ascii_uppercase, specs[2]) + random.sample(string.digits, specs[1]) + random.sample(spec_char, specs[0])
            random.shuffle(password)
        pass_w = ''
        for i in password:
            pass_w += ''+ i 
        return pass_w
    print('Invalid specifications!')



def check_password(password, length = 14, min_spec = 2, min_num = 0, min_upper = 1):
        min_spec2 = []
        min_count2 = []
        min_upper2 = []
        if length == len(password):
            for i in password:
                if i in string.punctuation:
                    spec = i
                    min_spec2 += [spec]
                if i in string.digits:
                    number = i
                    min_count2 += [number]
                if i in string.ascii_uppercase:
                    upper = i
                    min_upper2 += [upper]
            if(len(min_spec2) < min_spec) or (len(min_count2) < min_num) or (len(min_upper2) < min_upper):
                return False
            else:
                return True
        else:
            return False
