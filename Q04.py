def __isPalindrome(string):
    return string == string[::-1]

def __main__():
    word = input("Palavra:")
    if(__isPalindrome(word)):
        print(word + " É um palíndromo.")
    else:
        print(word + "  Não é um palíndromo")
        
__main__()