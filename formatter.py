# script para manejar los exports de InvenTree

import json
import os

import editor

# ::: variables :::

items_selection = []
items_filtered = []
items_mod = []

input_path = os.path.join('data', 'StockItem-2025-09-09(1).json')
output_path = os.path.join('tests', 'StockItems-filter-20250909(1).json')

nums_path = os.path.join('tests', 'serial_sensores_batch.json')
nums = []

test_input_path = os.path.join('data', 'serial_sensores_batch.csv')
test_output_path = os.path.join('tests', 'serial_sensores_batch.json')

mod_output_path = os.path.join('results', 'StockItems-mod_batch-20250909.json')

# ::: funciones :::
# en editor.py

# ::: Preparacion de archivos :::

editor.csv_to_json(test_input_path, test_output_path)

items_selection = editor.load(input_path)
items_filtered = editor.filter_by_atr(items_selection, 'ID de Parte', [1529])
nums = editor.load(nums_path)

editor.save(items_filtered, output_path, True)


# ::: Modificacion de archivos :::

items_mod = editor.mod_batch_serial_value(items_filtered, 'Lote', 'Número de serie', nums)
editor.save(items_mod, mod_output_path, True)

print(f"Archivos generados: \n\tTest: {test_output_path}\n\tResult: {output_path}\n\tMod: {mod_output_path}")
