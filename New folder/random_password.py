
import random

alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

num = ['0','1','2','3','4','5','6','7','8','9']

sym = ['!','@','#','$','%','^','&','*','(',')','_','+','-','=','{','}','[',']',':',';','|','\',<',',','>','.','?','/','~','`']

alpha_ask = int(input("How many letters you want? :"))

num_ask = int(input("How many numbers you want? :"))

sym_ask = int(input("How many symbols you want? :"))

password_list = []

for password in range(1, alpha_ask + 1):
    password_list += random.choice(alpha)

for password in range(1, num_ask + 1):
    password_list += random.choice(num)

for password in range(1, sym_ask + 1):
    password_list += random.choice(sym)

random.shuffle(password_list)


password = ''
for i in password_list:
    password += i

print("Your genrated password is: ", password)
