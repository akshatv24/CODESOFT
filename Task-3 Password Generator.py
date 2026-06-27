# Task 3: Password Generator
import random
import string

print("--- Password Generator ---")
length = int(input("How long do you want the password to be? "))

# mixing letters, numbers, and symbols
all_chars = string.ascii_letters + string.digits + string.punctuation

password = ""
for i in range(length):
    # randomly pick one character and add it to our password string
    password = password + random.choice(all_chars)

print("Your new password is:", password)