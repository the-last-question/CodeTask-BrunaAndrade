def __isPalindrome(string):
    return string == string[::-1]

def __main__():
    inputString = input("Palavra:")
    if(__isPalindrome(inputString)):
        print(inputString + " É um palíndromo.")
    else:
        print(inputString + "  Não é um palíndromo")
        
__main__()