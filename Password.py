import string
import random
import time

# Function to validate if a password has all required types of characters
def is_valid_password(s):
    has_lower = any(char.islower() for char in s)
    has_upper = any(char.isupper() for char in s)
    has_digit = any(char.isdigit() for char in s)
    has_special = any(not char.isalnum() for char in s)
    return has_lower and has_upper and has_digit and has_special

# Function to generate a valid password of given length
def pw(length):
    all_chars = string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation
    while True:
        password = ''.join(random.choice(all_chars) for _ in range(length))
        if is_valid_password(password):
            return password

print("WELCOME TO PASSWORD GENERATOR")
length = int(input("\nPlease enter the length of password to generate: "))
p = pw(length)
print(f"Your generted password :{p}")

# Brute-force part
p1 = "aB1%"

#for counting time and attempt
'''
count = 1
start = time.time()

while True:
    generated = pw(length)
    print(generated)
    print("in loop")
    if generated == p1:
        print(f"\nMatch found: {generated}")
        print(f"Count = {count}")
        break
    else:
        count += 1

end = time.time()
elapsed = end - start
print(f"\nLoop ran for {elapsed:.2f} seconds.")
time.sleep(3)
'''


