import random

def difFacil(guessed_letters, secret_word): 
    vocales="aeiou"
    for letter in secret_word:
        if letter in vocales:
            guessed_letters.append(letter)
        else:
            guessed_letters.append("_")
    return "".join(guessed_letters) #Retorna String mostrando las vocales por defecto
            
def difMedia(guessed_letters, secret_word):
    for indice,letter in enumerate(secret_word): #indice contiene la pos actual en la que estoy iterando
        if indice==0: #Primer letra
            guessed_letters.append(letter)
        elif (indice==len(secret_word)-1): #Última letra
            guessed_letters.append(letter)
        else:
            guessed_letters.append('_')
    return "".join(guessed_letters) #Retorna String mostrando la primer y ultima letra
            
# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo","inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)
# Número máximo de fallos permitidos
max_fails = 3
# Lista para almacenar las letras adivinadas
guessed_letters = []

print("""1. Fácil
2. Media
3. Difícil""")

dif = int(input("Ingrese la dificultad en la que quiere jugar(1,2,3):"))
while not dif in range(1,4): #Comprueba que se ingrese una dificultad valida
    dif = int(input("Ingrese la dificultad en la que quiere jugar(1,2,3):"))

print("¡Bienvenido al juego de adivinanzas! | NIVEL:", "Fácil" if dif==1 else "Media" if dif==2 else "Difícil")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
print(f"Tienes solo {max_fails} fallos permitidos!!")


word_displayed = difFacil(guessed_letters,secret_word) if dif==1 else difMedia(guessed_letters,secret_word) if dif==2 else ("_"*len(secret_word))
# Mostrarla palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")

fails=0
while fails < max_fails:
    # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()
    
    #Detecta como error el string "" (no se inserto ninguna letra)
    if letter == "":
        print('Ingrese una letra valida.')
        fails+=1
        continue
    
    # Verificar si la letra ya ha sido adivinada
    if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.") #No cuenta como error
        continue

    # Agregar la letra a la lista de letras adivinadas
    guessed_letters.append(letter)

    # Verificar si la letra está en la palabra secreta
    if letter in secret_word:
        print("¡Bien hecho! La letra está en la palabra.")
    else:
        fails+=1
        print("Lo siento, la letra no está en la palabra.")

    # Mostrar la palabra parcialmente adivinada
    letters = []
    for letter in secret_word:
        if letter in guessed_letters:
            letters.append(letter)
        else:
            letters.append("_")
            
    word_displayed = "".join(letters)
    print(f"Palabra: {word_displayed}")
    # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta:{secret_word}")
        break
else:
    print(f"¡Oh no! Has llegado a la cantidad maximas de intentos | INTENTOS REALIZADOS: {max_fails}")
    print(f"La palabra secreta era: {secret_word}")