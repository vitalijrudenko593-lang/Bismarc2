from colorama import Fore, Back, Style, init

init()

#Basik colored text
print(Fore.RED + "This is red text")
print(Fore.GREEN + "This is green text"+ Style.RESET_ALL)
print(Back.YELLOW + "This is yellow background"+ Style.RESET_ALL)
print(Style.BRIGHT + Fore.CYAN + "This is bright cyan text")

#Reset to default
print(Style.RESET_ALL + "Back to normal")

login = input("Login: ")
password = input("password: ")

if login == 'admin':
    if password == 'admin':
        print(Fore.Wr)