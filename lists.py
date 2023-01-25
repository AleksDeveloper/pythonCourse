import random

names = ["Fernanda", "Melisa del Carmen", "José", "Miriam Janet", "Natalia", "Tamara",
"Jasive", "Gabriel", "Jonathan Palacios (Emmanuel)", "Kenia", "Rodrigo", "Luis", "Yamil",
"Cinthia", "Melisa", "Miguel"
]

with open('Lista_20_Enero.txt') as lista:
    lines = lista.readlines()
print("IMPRIMO TODAS LAS LINEAS DEL ARCHIVO: \n",lines)
print("\nIMPRIMO RANDOM DEL ARCHIVO: ",random.choice(lines))
print(type(lines))

#print(random.choice(names))