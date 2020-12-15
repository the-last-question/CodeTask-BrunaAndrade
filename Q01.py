def __Caesar__encrypt(text, shift): 
    msg = ""  
    for i in range(len(text)): 
        char = text[i] 
        if (char.isupper()): 
            msg += chr((ord(char) + shift-65) % 26 + 65)
        else: 
            msg += chr((ord(char) + shift - 97) % 26 + 97) 
    return msg 
  


def __main__():
   inputMessage = "CodeTask"
   print ("texto  : " + inputString)
   print ("Tamanho da entrada : " + str(len(inputMessage)))
   print ("Mensagem criptografada: " + __Caesar__encrypt(inputMessage,len(inputMessage)))
       
        
__main__()