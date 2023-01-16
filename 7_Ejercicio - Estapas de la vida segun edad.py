# Calcular la etapa de la vida segun al cantidad de años ingresada por el usuario en pantalla.

edad = int(input('Ingrese su edad: '))

infancia = 'La infancia es increible... a veces...'
adolescencia = 'Muchos cambios y mucho estudio, aunque no en todos los casos...'
adultez = ' Bueno hermano, estas en el horno, que queres que te diga.'

if edad > 0 and edad < 11:
    print(infancia)
elif edad > 10 and edad < 21:
    print(adolescencia)
elif edad > 20 and edad < 50:
    print(adultez)
elif edad - 0:
    print ('Edad ingresada invalida, a menos que cumpla años al revez')
elif edad == str:
    print('Te pedi una edad, no cualquier otra boludes hermano/a')
else:
    print('Bueno, creo que ya no te queda mucho mas, ojala hayas aprovechado bien tu tiempo de vida.')