fruits = {'Platano':1.35, 'Manzana':0.8, 'Pera':0.85, 'Naranja':0.7}

fruit = input('Que fruta quieres: ').title().strip()
kg = float(input('Cuantos kilos: '))

if fruit in fruits:
    print(kg, 'kilos de', fruit, 'valen', fruits[fruit]*kg, '$')
else: 
    print("Lo siento, la fruta", fruit, "no está disponible.")