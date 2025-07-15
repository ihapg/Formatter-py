# script para manejar los exports de InvenTree

import json
import os

import editor

# ::: variables :::

items_selection = []
items_filtered = []

input_path = os.path.join('data_backup', 'StockItem-2025-07-10(1).json')
output_path = os.path.join('tests', 'nums_test.json')

nums_path = os.path.join('tests', 'numeros.txt')
nums = []

test_input_path = os.path.join('tests', 'nums_test.json')
test_output_path = os.path.join('tests', 'StockItems-nums_mod-20250715.json')

# ::: funciones :::
# en editor.py

# ::: ejecucion :::

items_selection = editor.load(input_path)
nums = editor.leer_numeros_txt(nums_path)

items_filtered = editor.filter_by_atr(items_selection, "Stock Item ID", nums)
editor.sorter(items_filtered, 'Stock Item ID', False)

editor.save(items_filtered, output_path, True)

# __ Modificacion del archivo __
items_selection = editor.load(test_input_path)
# items_filtered = editor.get_field_values(items_selection, "Installed In")
# editor.save(items_filtered, test_output_path, False)
# print(items_filtered)
items_filtered = editor.mod_fields(items_selection, "Installed In", "")
editor.save(items_filtered, test_output_path, True)

print(f"Archivo generado: {test_output_path}")
