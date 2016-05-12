frase=str(input("ingrese una frase\n"))
def contador(frase):
    frase1=frase.splitlines()
    print(frase1)
    for i in range(len(frase1)):
        palabras=len(frase1[i].split(" "))
        print("palabra ",i,": ",palabras)

contador(frase)

def creartxt():
    archi=open('datos.txt', 'w')
    archi.close()

def grabartxt():
    archi=open('datos.txt', 'a')
    archi.write('')
    archi.close()

creartxt()
grabartxt()