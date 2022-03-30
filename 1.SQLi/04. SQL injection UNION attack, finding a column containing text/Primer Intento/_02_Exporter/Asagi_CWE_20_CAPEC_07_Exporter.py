import os
import json

def Uno(diccionario_maligno):

    print("[--] Asagi Exporter")
    '''Recepcion del diccionario desde Asagi_CWE_20_CAPEC_07.main().py'''
    diccionario_maligno = diccionario_maligno

    print("\t[i] Objetos JSON recibidos")
    print("\t[i] Iniciando serializacion")

    '''Serializacion JSON del diccionario'''
    json_object = json.dumps(diccionario_maligno, indent = 4)

    print("\t[OK] Serializacion correcta")

    '''Revisando resultado'''
    #print(json_object)

    '''Preparacion del archivo objetivo'''
    nombre_archivo_json = 'Carga_CWE_20_CAPEC_07_Portswigger.json'
    
    '''
    Creacion del archivo objetivo
    La instancia generalizada del archivo tiene el nombre de variable ARCHIVO
    mientras que se especifica su nombre especifico como una cadena inmutable
    Pueden crearse formulas para la creacion de nombre de archivos siguiendo reglas bien definidas
    '''

    '''Abrir archivo con permisos de escritura'''
    print("\t[i] Creando archivo")
    archivo = open(nombre_archivo_json, 'w+')

    print("\t[i] Escribiendo entidades JSON sobre archivo")
    '''Escribir el objeto JSON del archivo objetivo'''
    archivo.write(json_object)

    print("\t[OK] Escritura finalizada. Cerrando archivo.\n")
    '''Cerrar el archivo antes de terminar la operacion'''
    archivo.close()

    
    
