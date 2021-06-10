# encrypting in caesar cypher


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceasar_cypher(direction,text,shift):
  new_alpha_set=[]
  return_text=''
    
  for i in range(0,len(alphabet)):
    new_alpha_set.append(alphabet[(i+shift)%26]) # for the list index out of range cases
  

  if direction=='e':

    for i in range(0,len(text)):
      if text[i] not in alphabet:
        return_text += text[i]
      else:
        iinl=alphabet.index(text[i]) # index that we want to look for in new_alpha_sett
        return_text += new_alpha_set[iinl]
    print(f'encrypted text is : {return_text} ')
  
  else:

  	for i in range(0,len(text)):
  		if text[i] not in new_alpha_set:
  			return_text += text[i]
  		else:
  			iinl=new_alpha_set.index(text[i]) # index that we want to look for in alphabet
  			return_text += alphabet[iinl]
  	print(f'decrypted text is : {return_text} ')


  
  


ceasar_cypher(direction,text,shift)  



