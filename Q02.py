import re #regular expression library import

def __checkPassword(password):
    check = 0
    while True:   
        if (len(password)<8): 
            check = -1
            break
        elif not re.search("[a-z]", password): 
            check = -1
            break
        elif not re.search("[A-Z]", password): 
            check = -1
            break
        elif not re.search("[0-9]", password): 
            check = -1
            break
        elif re.search("\s", password): 
            check = -1
            break
        else: 
            check = 0
            return True
    
        if check ==-1:
            return False

def __main__():
    password = input("Digite a senha: ")
    if(__checkPassword(password)):
        print("Essa senha é válida")
    else:
        print("Essa senha não é válida")
        
__main__()