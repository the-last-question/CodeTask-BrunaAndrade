def __isPerfectNumber(num):
    Sum = 0
    for i in range(1, num):
        if(num % i == 0):
            Sum = Sum + i

    if (Sum == num):
        return True
    else:
        return False

def __main__():
    print("Numeros perfeitos entre 1 e 10000:")
    for i in range(1, 10000):
        if(__isPerfectNumber(i)):
             print(" %d é um número Perfeito:" %i)
    
        
__main__()