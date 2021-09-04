from time import sleep


def bem_vindo():
    print("""
    Encode and Decode\n 
        | Digite C para Codificar sua mensagem:
        | Digite D para Descodificar sua mensagem usando nosos sistema:
        | Digite S para Sair: """)


def frase():
    frase = input("\n" + (" " * 4) +
                  "Digite sua frase para ela ser Codificada: ")

    return frase


def frase2():
    frase2 = input("\n" + (" " * 4) +
                   "Digite sua frase para ela ser Descodificada: ")
    return frase2


def texto1(frase):
    print("\n" + (" " * 4) + "Codificando...")
    sleep(1)

    print("\n" + (" " * 4) + "Padrão: \n" + (" " * 7) + f"{frase}")
    print("\n" + (" " * 4) + "Codificado: \n" + (" " * 7) + encode(frase))
    sleep(5)


def texto2(frase2):
    print("\n" + (" " * 4) + "Descodificando...")
    sleep(1)

    print("\n" + (" " * 4) + "Codificado: \n" + (" " * 7) + f"{frase2}")
    print("\n" + (" " * 4) + "Descodificado: \n" + (" " * 7) + decode(frase2))
    sleep(5)


def error():
    print("\n" + (" " * 4) +
          "Digite apenas C para Codificar, D para Descodificar ou S para Sair, Fechando...")
    sleep(6.8)
    exit()


def S():
    agradecimento = "\n" + (" " * 4) + \
        "Obrigado por ter usado meu software".capitalize()
    print(agradecimento)
    sleep(2.8)
    print("\n" + (" " * 4) + "Fechando...")
    sleep(3)
    exit()


def sair():
    input("\n" + (" " * 4) + "Aperte Enter para sair: ")
    print("Fechando...")
    sleep(2)


def encode(frase):
    tradutor = ""

    #------------#

    # ALFABETO (em ordem) : A B C D E F G H I J K L M N O P Q R S T U V W X Y Z.

    for letra in frase:
        if letra in "AÁaá":
            tradutor = tradutor + "$"
        elif letra in "Bb":
            tradutor = tradutor + "+"
        elif letra in "Cc":
            tradutor = tradutor + "#"
        elif letra in "Dd":
            tradutor = tradutor + "E"
        elif letra in "EÉeé":
            tradutor = tradutor + "Y"
        elif letra in "Ff":
            tradutor = tradutor + "@"
        elif letra in "Gg":
            tradutor = tradutor + "?"
        elif letra in "Hh":
            tradutor = tradutor + "ç"
        elif letra in "IÍií":
            tradutor = tradutor + "U"
        elif letra in "Jj":
            tradutor = tradutor + "^"
        elif letra in "Kk":
            tradutor = tradutor + "P"
        elif letra in "Ll":
            tradutor = tradutor + "%"
        elif letra in "Mm":
            tradutor = tradutor + "*"
        elif letra in "Nn":
            tradutor = tradutor + "~"
        elif letra in "OÓoó":
            tradutor = tradutor + 'Q'
        elif letra in "Pp":
            tradutor = tradutor + "v"
        elif letra in "Qq":
            tradutor = tradutor + "0"
        elif letra in "Rr":
            tradutor = tradutor + "1"
        elif letra in "Ss":
            tradutor = tradutor + "2"
        elif letra in "Tt":
            tradutor = tradutor + "x"
        elif letra in "UÚuú":
            tradutor = tradutor + "z"
        elif letra in "Vv":
            tradutor = tradutor + "£"

        elif letra in "Ww":
            tradutor = tradutor + "-"
        elif letra in " ":
            tradutor = tradutor + " "

    return tradutor

    # ALFABETO (em ordem) : A B C D E F G H I J K L M N O P Q R S T U V W X Y Z.

    #------------#


def decode(frase2):

    tradutor = ""

    #------------#

    # ALFABETO (em ordem) : A B C D E F G H I J K L M N O P Q R S T U V W X Y Z.

    for letra in frase2:
        if letra in "$":
            tradutor = tradutor + "a"
        elif letra in "+":
            tradutor = tradutor + "b"
        elif letra in "#":
            tradutor = tradutor + "c"
        elif letra in "E":
            tradutor = tradutor + "d"
        elif letra in "Y":
            tradutor = tradutor + "e"
        elif letra in "@":
            tradutor = tradutor + "f"
        elif letra in "?":
            tradutor = tradutor + "g"
        elif letra in "ç":
            tradutor = tradutor2 + "h"
        elif letra in "U":
            tradutor = tradutor + "i"
        elif letra in "^":
            tradutor = tradutor + "j"
        elif letra in "P":
            tradutor = tradutor + "k"
        elif letra in "%":
            tradutor = tradutor + "l"
        elif letra in "*":
            tradutor = tradutor + "m"
        elif letra in "~":
            tradutor = tradutor + "n"
        elif letra in "Q":
            tradutor = tradutor + "o"
        elif letra in "v":
            tradutor2 = tradutor2 + "p"
        elif letra in "0":
            tradutor = tradutor + "q"
        elif letra in "1":
            tradutor = tradutor + "r"
        elif letra in "2":
            tradutor = tradutor + "s"
        elif letra in "x":
            tradutor = tradutor + "t"
        elif letra in "z":
            tradutor = tradutor + "u"
        elif letra in "£":
            tradutor = tradutor + "v"

        elif letra in "-":
            tradutor = tradutor + "w"
        elif letra in " ":
            tradutor = tradutor + " "

    return tradutor.capitalize()
