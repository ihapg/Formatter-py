import os
import json

ruta = os.path.join('tests', 'numeros.txt')


# ::: funciones :::

# __ Funcion para ordenar en base a un campo __
def sorter(array, field, reversed):
    array.sort(key=lambda x: x.get(field, ''), reverse=reversed)

# __ Funcion para guardar en archivo __
def save(array, path, json_bool):
    with open(path, 'w', encoding='utf-8') as out_file:
        if json_bool: 
            # __ archivo json __
            json.dump(array, out_file, ensure_ascii=False, indent=2)
        
        else:
            # __ archivo txt __
            for item in array:
                out_file.write(json.dumps(item, ensure_ascii=False) + '\n')

# __ Cargar elementos de JSON
def load(path):
    with open(path, 'r', encoding='utf-8') as f:
        items = json.load(f)

    array_items = []
    for item in items:
        array_items.append(item)
    return array_items

# __ Funcion para filtrar por atributo y valor __
def filter_by_atr(array, atr, values):
    filtered = []
    for item in array:
        for value in values:
            if item.get(atr) == value:
                filtered.append(item)
    
    return filtered
    # return [item for item in array if item.get(atr) == value]

# __ Modificar campos __
def mod_fields(array, field, value):
    array_mod = []
    for item in array:
        if field in item:
            item[field] = value
        array_mod.append(item)
    
    return array_mod

# __ Obtener valores de un campo __
def get_field_values(array, field):
    array_values = []
    for item in array:
        if field in item:
            if item[field] not in array_values:
                array_values.append(item[field])
    
    return array_values

# __ Generar números __
def generar_txt_numeros(ruta_archivo, inicio, fin):
    with open(ruta_archivo, 'w', encoding='utf-8') as txt:
        for numero in range(inicio, fin + 1):
            txt.write(f"{numero}\n")

# __ Pasar números de .txt a array __
def leer_numeros_txt(ruta_archivo):
    numeros = []
    with open(ruta_archivo, 'r', encoding='utf-8') as f:
        for linea in f:
            numero = linea.strip()
            if numero:  # Evita líneas vacías
                numeros.append(int(numero))
    return numeros

# ::: ejecucion pruebas :::
# generar_txt_numeros(ruta, 3900, 4030)
# print(leer_numeros_txt(ruta))

# Ejemplo de uso:
# numeros = leer_numeros_txt(ruta)
# print(numeros)