from os import system

#INICIO (Aunque parezca documentado por IA nel pastel yo lo hice :P)
while True:
    ingresoP = int(input("¿Qué desea realizar?\n 1.Matemática\n 2.Geografía\n 3.Inglés\n"))
    system('cls')

    while ingresoP != 1 and ingresoP != 2 and ingresoP != 3:
        input('Valor inválido, presione enter para intente de nuevo')
        ingresoP = int(input("¿Qué desea realizar?\n 1.Matemática\n 2.Geografía\n 3.Inglés\n"))
        system('cls')

#=========================SECCIÓN DE MATEMÁTICAS====================

    if ingresoP == 1:
        print('Preguntas de matemáticas:\n¿Cuánto es 2+2?\n')
        pregunta1 = int(input('Respuesta: '))

        while pregunta1 != 4:
            pregunta1 = int(input('Respuesta incorrecta, intenta de nuevo: '))

        if pregunta1 == 4:
            system('cls')
            input('Respuesta correcta! Pasemos a la siguiente')

            print('Preguntas de matemáticas:\n¿Cuánto es 2+5?\n')
            pregunta2 = int(input('Respuesta: '))
            
        while pregunta2 != 7:
            pregunta2 = int(input('Respuesta incorrecta, intenta de nuevo: '))

        if pregunta2 == 7:
            system('cls')
            input('Respuesta correcta! Pasemos a la siguiente')

            
        print('Preguntas de matemáticas:\n¿Cuánto es 3+3?\n')
        pregunta3 = int(input('Respuesta: '))
        while pregunta3 != 6:
            pregunta3 = int(input('Respuesta incorrecta, intenta de nuevo: '))

        if pregunta3 == 6:
            print('Respuesta correcta! Has terminado la sección de Matemáticas')


#========================SECCIÓN DE GEOGRAFÍA===================
      
    elif ingresoP == 2:
        print('Preguntas de geografía:\n¿Cuál es la capital de Francia?\n')
        preguntaG = str(input('Respuesta: '))
        
        while preguntaG != "Paris":
            preguntaG = str(input('Respuesta incorrecta, intenta de nuevo:'))

        if preguntaG == "Paris":
            system('cls')
            input('Respuesta correcta! Pasemos a la siguiente')
            
            print('Preguntas de geografía:\n¿Cuál es la capital de Italia?\n')
            preguntaG2 = str(input('Respuesta: '))
            while preguntaG2 != 'Roma':
                preguntaG2 = str(input('Respuesta incorrecta, intenta de nuevo: '))
            
            if preguntaG2 == 'Roma':
                system('cls')
                input('Respuesta correcta! Pasemos a la siguiente')

            system('cls')
            print('Preguntas de geografía:\n¿Cuál es la capital de Colombia?\n')
            preguntaG3 = str(input('Respuesta: '))

            while preguntaG3 != 'Bogota':
                preguntaG3 = str(input('Respuesta incorrecta, intenta de nuevo: '))

            if preguntaG3 == 'Bogota':
                print('Respuesta correcta! Has terminado la sección de geografía')
                
#==========================SECCIÓN DE INGLÉS================================

    elif ingresoP == 3:
        print('Preguntas de Inglés:\n¿Que significa "Water"?\n')
        preguntaI1 = str(input('Respuesta: '))
        
        while preguntaI1 != "Agua":
            preguntaI1 = str(input('Respuesta incorrecta, intenta de nuevo:'))

        if preguntaI1 == "Agua":
            system('cls')
            input('Respuesta correcta! Pasemos a la siguiente')
            
            print('Preguntas de Inglés:\n¿Qué significa "Hello"?\n')
            preguntaI2 = str(input('Respuesta: '))

            while preguntaI2 != 'Hola':
                preguntaI2 = str(input('Respuesta incorrecta, intenta de nuevo: '))
            
            if preguntaI2 == 'Hola':
                system('cls')
                input('Respuesta correcta! Pasemos a la siguiente')

            print('Preguntas de Inglés:\n¿Qué significa "Good morning?\n')
            preguntaI3 = str(input('Respuesta: '))

            while preguntaI3 != 'Buenos dias':
                preguntaI3 = str(input('Respuesta incorrecta, intenta de nuevo: '))

            system('cls')
            if preguntaI3 == 'Buenos dias':
                print('Respuesta correcta! Has terminado la sección de geografía')

#FINAL DEL CUESTIONARIO
    input("Presione enter para regresar al cuestionario")
        
