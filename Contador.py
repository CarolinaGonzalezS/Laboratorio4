frase=str(input("ingrese una frase\n"))
def contador(frase):
    frase1=frase.splitlines()
    print(frase1)
    for i in range(len(frase1)):
        palabras=len(frase1[i].split(" "))
        print("palabra ",i,": ",palabras)

contador(frase)