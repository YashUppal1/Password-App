from generatepass import *

website = input("Enter website:")
username = input("Enter username:")
password = generatepass()
f = open('password.txt',"a")
f.write(f"Website: {website}\nUsername: {username}\nPassword: {password}\n\n")
f.close()

print("New password for ",website, " is ",password, "and stored in password.txt.")