"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd


def ingest_data():

    #
    # Inserte su código aquí
    #
    filename = 'clusters_report.txt'
    
    c1= []
    c2= []
    c3= []
    auxC4= ""
    c4= []
    license_file = open(filename, mode='r')
    comienzo_dato= True
    for index, line in enumerate(license_file):
        if(index > 3):
            lineArray= line.split()
            if(len(lineArray)>0):
                if comienzo_dato:
                    c1.append(int(lineArray[0]))
                    c2.append(int(lineArray[1]))
                    c3.append(float(lineArray[2].replace(",",".")))
                    for idx, palabra in enumerate(lineArray[4:]):
                        auxC4+= palabra +" "
                    #print(auxC4)
                    #auxC4= ""
                    comienzo_dato= False
                else:
                    for idx, palabra in enumerate(lineArray):
                        if idx== len(lineArray)-1 and "." in palabra:
                            auxC4+= palabra.replace(".", "")
                        else:
                            auxC4+= palabra +" "
            else: 
                comienzo_dato= True
                c4.append(auxC4)
                auxC4= ""
    newc4= []
    for c in c4:
        if c[-1] == " ":
            c= c[:-1] 
        newc4.append(c)

    information= {
    'cluster':c1,
    'cantidad_de_palabras_clave' :c2,
    'porcentaje_de_palabras_clave':c3,
    'principales_palabras_clave': newc4
    }
    df = pd.DataFrame(information)
    license_file.close()
    return df
