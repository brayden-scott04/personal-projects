import random

#random password generator
#contains at least 1 Upper Case
#contains at least 1 lower case
#contains at least 1 special character (e.g. "-", "_", "!", etc.)
#contains at least 1 number
#has a length size of at least 8 characters up to 16 characters


def lst_lower_cases():
    lower_cases = []
    for number in range(97, 122 + 1): #lowercase a-z in unicode
        lower_cases += chr(number)
    return lower_cases

def lst_upper_cases():
    upper_cases = []
    for i in range(65,90+1): #uppercase A-Z in unicode
        upper_cases+=chr(i)
    return upper_cases

def special_characters():
    special_chr = []
    for symbol in range(33,48+1): #special characters such as symbols
        special_chr+=chr(symbol)
    for symbol in range(58,64+1): #another set of characters/symbols
        special_chr+= chr(symbol)
    return special_chr

def nums():
    numbers = []
    for num in range(48,57+1):   #numbers 0-9 in unicode, although 0,10 range would have sufficed
        numbers += chr(num)
    return numbers


def gen_password():
    lower = lst_lower_cases()
    upper = lst_upper_cases()
    spec = special_characters()
    numbers = nums()
    password = ""
    
    random_cnt = random.randint(8,17) #generates a password length of anywhere between 8 characters to 16 characters
    
    while len(password) <random_cnt:
        password += random.choice(lower) + random.choice(upper) + random.choice(spec) + random.choice(numbers)
        
        if len(password)>=random_cnt:
            break
            
    password_as_lst = list(password)
    shuffled = random.shuffle(password_as_lst)
    password_shuffled = ""
    for character in password_as_lst:
        password_shuffled += character
        
    return password_shuffled
        
        
gen_password()
