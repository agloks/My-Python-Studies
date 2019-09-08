#Creator Agl
#I comment my code even with my bad english, to make it more understandable. If something does not make sense, i'm sorry for my English.
import random
#Function to create random password
def Magic():

    number_random=' '
    for key in range(0,password):
        number_random+= (chr(random.randrange(32,122)))
    
    return(number_random)
#Function to check the strenght of the password created in this code    
def Check():

    if total == 1:
        print("*Password Easy")
        
    elif total == 2:
        print("*Password Medium")
    
    elif total == 3:
        print("*Password Hard")
    
    elif total == 4:
        print("*Password Perfect")
        
    else:
        print("*Don't have Password")
#Perfom the function Magic() if the conditions are valid     
try:
    
    password = int(input())
    
    if password >= 8 and password <= 32:
        valuer=Magic()
        print(valuer,"\n","--"*15,"--"*15)
    elif password < 8 or password > 32:
        print("How many numbers do you need in your password between 8 to 32")
#Case use string ou null input        
except(ValueError,TypeError):
    print("Need one number between 8 to 32")
#List to special character, i'm using this method in this case to further study the command for
especial_list = []
especial_list_official = []
for especial in range(32,48):
    especial_list.append(especial)
    if especial == 47:
        for especial in range(58,65):
            especial_list.append(especial)
            if especial == 64:
                for especial in range(91,97):
                    especial_list.append(especial)
                    if especial == 96:
                        for especial in especial_list:
                            especial_list_official.append(chr(especial))
#List numbers
numbers = []
numbers_official = []
for numb in range(48,58):
    numbers.append(numb)
    if numb == 57:
        for numb in numbers:
            numbers_official.append(chr(numb))
#List capittal letter
upcase = []
upcase_official = []
for up in range(65,91):
    upcase.append(up)
    if up == 90:
        for up in upcase:
            upcase_official.append(chr(up))
#List lower case
lowcase = []
lowcase_official = []
for low in range(97,123):
    lowcase.append(low)
    if low == 122:
        for low in lowcase:
            lowcase_official.append(chr(low))
#Performs the function Check() to check password level
try:

    valuer_list=list(valuer)
    count_chr = 0
    count_nmb = 0
    count_up = 0
    count_low = 0

    for test in especial_list_official:
        count_chr+= test in valuer_list

    for test in numbers_official:
        count_nmb+= test in valuer_list

    for test in upcase_official:
        count_up+= test in valuer_list

    for test in lowcase_official:
        count_low+= test in valuer_list

    total = 0

    if count_chr != 0:
        total+= 1
    if count_nmb != 0:
        total+= 1
    if count_up != 0:
        total+= 1
    if count_low != 0:
        total+= 1

    if password >= 8 and password <= 32:
        Check()
#If the number quantity is not valid on the first try    
except(NameError,ValueError,TypeError):
    pass            