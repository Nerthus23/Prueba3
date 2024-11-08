import random
import string

longitud = 10
caracteres = string.ascii_letters + string.digits 
contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
print("Contraseña:" , contraseña)

