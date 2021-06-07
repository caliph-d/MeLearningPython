# Strong password generator

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

f_lis=[]
pwd=''

for i in range(0,nr_letters):
  x=random.randint(0,len(letters))
  f_lis.append(letters[x])
print(f_lis)

for i in range(0,nr_symbols):
  x=random.randint(0,len(symbols))
  f_lis.append(symbols[x])
print(f_lis)

for i in range(0,nr_numbers):
  x=random.randint(0,len(numbers))
  f_lis.append(numbers[x])
print(f_lis)  

lof=len(f_lis)

for x in range(0,lof):
  x=random.randint(0,len(f_lis))
  pwd+=f_lis[x]
  f_lis.pop(x)

print(f'system generated password is : {pwd}')