import time
import csv
import os
...
csv.field_size_limit(2147483647)

import sys
...
default_limit = 1000
sys.setrecursionlimit(default_limit*10)

from DataStructures import array_list as al
from DataStructures import single_linked_list as ll

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    #TODO: Llama a las funciónes de creación de las estructuras de datos
    catalog= {}
    catalog["computers"]= al.new_list()
    return catalog

# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    start_time = get_time()

    file_dir = os.path.dirname(__file__)
    file_path = os.path.join(os.path.dirname(__file__), "..", "Data", filename)

    min_computer = None
    max_computer = None

    with open(file_path, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            computer = {
                'device_type': row['device_type'],
                'brand': row['brand'],
                'model': row['model'],
                'release_year': int(row['release_year']) if row['release_year'] else None,
                'os': row['os'],
                'form_factor': row['form_factor'],
                'cpu_brand': row['cpu_brand'],
                'cpu_model': row['cpu_model'],
                'cpu_tier': int(row['cpu_tier']) if row['cpu_tier'] else None,
                'cpu_cores': int(row['cpu_cores']) if row['cpu_cores'] else None,
                'cpu_threads': int(row['cpu_threads']) if row['cpu_threads'] else None,
                'cpu_base_ghz': float(row['cpu_base_ghz']) if row['cpu_base_ghz'] else None,
                'cpu_boost_ghz': float(row['cpu_boost_ghz']) if row['cpu_boost_ghz'] else None,
                'gpu_brand': row['gpu_brand'],
                'gpu_model': row['gpu_model'],
                'gpu_tier': int(row['gpu_tier']) if row['gpu_tier'] else None,
                'vram_gb': int(row['vram_gb']) if row['vram_gb'] else None,
                'ram_gb': int(row['ram_gb']) if row['ram_gb'] else None,
                'storage_type': row['storage_type'],
                'storage_gb': int(row['storage_gb']) if row['storage_gb'] else None,
                'storage_drive_count': int(row['storage_drive_count']) if row['storage_drive_count'] else None,
                'display_type': row['display_type'],
                'display_size_in': float(row['display_size_in']) if row['display_size_in'] else None,
                'resolution': row['resolution'],
                'refresh_hz': int(row['refresh_hz']) if row['refresh_hz'] else None,
                'battery_wh': int(row['battery_wh']) if row['battery_wh'] else None,
                'charger_watts': int(row['charger_watts']) if row['charger_watts'] else None,
                'psu_watts': int(row['psu_watts']) if row['psu_watts'] else None,
                'wifi': row['wifi'],
                'bluetooth': row['bluetooth'],
                'weight_kg': float(row['weight_kg']) if row['weight_kg'] else None,
                'warranty_months': int(row['warranty_months']) if row['warranty_months'] else None,
                'price': float(row['price'])
            }
            al.add_last(catalog["computers"], computer)

            if min_computer is None or computer['price'] < min_computer['price']:
                min_computer = computer
            if max_computer is None or computer['price'] > max_computer['price']:
                max_computer = computer
    end_time = get_time()
    load_time = delta_time(start_time, end_time)
    total_computers = al.size(catalog["computers"])
    first_five = []
    last_five = []

    size = al.size(catalog["computers"])

# Primeros 5
    for i in range(1, min(6, size + 1)):
        first_five.append(al.get_element(catalog["computers"], i))

# Últimos 5
    for i in range(max(1, size - 4), size + 1):
        last_five.append(al.get_element(catalog["computers"], i))

    return load_time, total_computers, min_computer, max_computer, first_five, last_five


# Funciones de consulta sobre el catálogo


def req_1(catalog):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
