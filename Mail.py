#!/usr/bin/python
import re

correo = input("Petra ahora quiere validar correo ingresa uno para verificarlo: ")
mail = ""

m = re.search('[A-Z0-9a-z._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,64}', mail)

if m:
    print(" segun Petra; El correo es valido")
else:
    print("Ufff Petra no admite tu correo!!! El Correo es Invalido")