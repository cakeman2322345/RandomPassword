import random
lenght = int(input(""))
symbol = ["*","$","&","^","@","#","!"]
Password = ""
for i in range(lenght):
    category = random.randint(1,3)
    if category == 1:
        password_add = random.choice(symbol)
    elif category == 2:
        Captal = random.randint(65,90)
        password_add = chr(Captal)
    elif category == 3:
        Small = random.randint(97,122)
        password_add = chr(Small)
    Password = Password+password_add
print("Your Password Is:",Password)       
