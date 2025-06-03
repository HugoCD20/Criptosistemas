from collections import defaultdict
import math

entrada="LNUDVMUYRMUDVLLPXAFZUEFAIOVWVMUOVMUEVMUEZCUDVSYWCIVCFGUCUNYCGALLGRCYTIJTRNNPJQOPJEMZITYLIAYYKRYEFDUDCAMAVRMZEAMBLEXPJCCQIEHPJTYXVNMLAEZTIMUOFRUFC"
distan=[]
def encontrar_repetidos(texto, longitud=3):
    repeticiones = defaultdict(list)
    for i in range(len(texto) - longitud + 1):
        sub = texto[i:i+longitud]
        repeticiones[sub].append(i)

    for sub, posiciones in repeticiones.items():
        if len(posiciones) > 1:
            distancias = [posiciones[i+1] - posiciones[i] for i in range(len(posiciones)-1)]
            for d in distancias:
                distan.append(d)
            mcd = math.gcd(*distancias)

def dividir(entrada, mcd):
    subcriptograma=[]
    for i in range(mcd):
        auxiliar=[]
        for j in range(i,len(entrada),mcd):
            auxiliar.append(entrada[j])
        subcriptograma.append(auxiliar)
    return subcriptograma

def frecuencias(subcriptograma,alfabeto):
    auxiliar=[]
    for sub in subcriptograma:
        aux=[]
        for letra in alfabeto:
            aux.append(sub.count(letra))
        auxiliar.append(aux)
    return auxiliar

def extenderletras(datos):
    extra = 16
    repetidos = (datos * ((extra // len(datos)) + 1))[:extra]
    nueva_lista = datos + repetidos
    return nueva_lista

def buscar_mayor_frecuencia(frecuencia,alfabeto):
    resultados=""
    for i in frecuencia:
        extendida = extenderletras(i)
        print("============================================")
        superior=0
        letras= extenderletras(alfabeto)
        mayores=""
        for j,char in enumerate(i):
            x = j
            y = j + 4
            z = j + 15
            mayor=extendida[x]+extendida[y]+extendida[z]
            if mayor > superior:
                mayores=""
                superior = mayor
                mayores+= letras[j]
                mayores+= letras[y]
                mayores+= letras[z]
        resultados+= mayores[0]
    print("clave:",resultados)

def main():
    encontrar_repetidos(entrada)
    encontrar_repetidos(entrada,4)
    mcd = math.gcd(*distan)

    print("Subcriptograma:")
    subcriptograma = dividir(entrada, mcd)

    alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

    frecuencia= frecuencias(subcriptograma, alfabeto)
    buscar_mayor_frecuencia(frecuencia,alfabeto)
    for i in frecuencia:
        print(i)
    #for i, sub in enumerate(subcriptograma):
    #    print(f"Subcriptograma {i+1}: {''.join(sub)}")

main()