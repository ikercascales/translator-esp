import random
Pass = "+-/*!&$#?=@abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890"
Longitud = int(input('Cual va a ser la longitud de la contraseña?'))
Password = ''
for i in range (Longitud):
    Password += random.choice(Pass)
    
print('Tu contraseña generada es:', Password)
