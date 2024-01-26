import random
import string

def generate_password(length=4):
    characters =  string.digits 
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example: Generate and print 5 passwords in a loop
num_passwords = 10000
for i in range(num_passwords):
    password = generate_password(4)
    print(f"Generated Password {i + 1}: {password}")
