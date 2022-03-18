import random
import time
import qrcode

print("Password Generator")
print("==================")

char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMAOPQRSTUVWXYZ~`!@#$%^&*()_-+={[}]|\:;"?0123456789'
no_password = int(input("How many password? "))

len_password = int(input("Lenght of the password needed? "))


print("Please wait while we are generating your passwords\n")
time.sleep(3)
print("Generated passwords: \n")

for pwd in range(no_password):
    passwords = ''
    for c in range(len_password):
        passwords += random.choice(char)
    print(passwords)

ans = input("Do you want to create a qr code with your password choice? y/n: ")

if ans == "y":
    img = qrcode.make(passwords)
    img.save('C:/Users/Renzo/Documents/Qr/qr.png')
elif ans == "n":
    print("Thanks!")









