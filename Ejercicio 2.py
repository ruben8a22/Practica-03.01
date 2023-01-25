#Escribir una función que lea dos ficheros csv con una lista larga de datos de personas (50 personas y 1000 personas)
# y llame a dos funciones que pongan su nombre en formato capitalizado y calculen la letra de DNI correspondiente.
# Realiza la comprobación de rendimiento con la librería cProfile y muestra los datos. Describe que indica cada dato
# que nos proporciona cProfile.

import csv
import datetime


nif_dict = {"0": "T", "1": "R", "2": "W", "3": "A", "4": "G", "5": "M",
            "6": "Y", "7": "F", "8": "P", "9": "D", "10": "X", "11": "B",
            "12": "N", "13": "J", "14": "Z", "15": "S", "16": "Q", "17": "V",
            "18": "H", "19": "L", "20": "C", "21": "K", "22": "E"}


def check_username(nombre):
    """Esta funcion sirve para comprobar que el nombre y apellido esten en formato capitalizado o camelcase,
       independientemente que el nombre sea simple o compuesto
       -Entradas:
        Nombres o apellidos
       -Salidas:
        Nombre o apellido corregido
       """
    mayus = nombre.title()

    return mayus


def check_nif(dni):
    """Esta función realiza la comprobacion matematica para determinar si el numero del NIF se corresponde con la letra
       correcta
     -Entradas:
      NIF del usuario en formato de 8 numeros y una letra
     -Salidas:
      NIF corregido
      """
    numeroDNI = dni[0:8]
    resto = int(numeroDNI) % 23
    letraCorrecta = nif_dict[str(resto)]

    return numeroDNI + letraCorrecta








def calculo(ruta):
    """Esta funcion se encarga de abrir el archivo con todos los datos sin corregir y sobre-escribir todos los datos
       corregidosen el mismo archivo.
       -Entradas:
        Ubicacion del archivo (Rubén Ochoa Ilzarbe - DGT.csv)
        """

    with open(ruta, encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=",", dialect=csv.excel)
        encabezado = []
        for persona in reader:
            if persona[0] != "Nombre":
                nombre = ( check_username(persona[0]))

                DNI = (check_nif(persona[1]))




                encabezado.append([nombre, DNI])

        excel_escritor = csv.writer(csvfile)
    with open(ruta, encoding="utf-8") as corregido:
        ficheroc = open("corregido.csv", "w", newline="")
        corregido = csv.writer(ficheroc, quotechar='"', quoting=csv.QUOTE_ALL)
        for linea in encabezado:
            corregido.writerow(linea)

    return
start_time = datetime.datetime.now()
ruta = input("Introduce el nombre del archivo:")
calculo(ruta)
end_time = datetime.datetime.now()
print(end_time - start_time)


