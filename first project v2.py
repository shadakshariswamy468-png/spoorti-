print("-------PASSWORD GENERATOR---------")
lendth=int(input("Enter password length:"))
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation
 
all_characters = letters + numbers + symbols
pasword =" "
for i in range(length):
     pasword+=random.choice(all_characters)
     print("your generated password is:",password)