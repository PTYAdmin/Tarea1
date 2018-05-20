#!/usr/bin/python
import re

input = "Contact me by email /!$&@hotmail.com or at the office."

m = re.search('[A-Z0-9a-z._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,64}', input)

if m:
    print("correo valido")
else:
    print("Correo Invalido")