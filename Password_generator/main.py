import random
import string

def generate_password(length=12):
  #define the characters to use in the psswrd
  characters = string.ascii_letters + string.digits + string.punctuation

  #generate a password by randomly selecting characters
  password= ''.join(random.choice(characters) for _ in range(length))

  return password


password_length = int(input("Enter desired length of the password:"))

if password_length <6:
  print("Too short")
else: 
  generated_password = generate_password(password_length)
  print("Password:", generated_password)