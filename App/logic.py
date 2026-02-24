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


def req_3(catalog, cpu_brand, cpu_tier):
    """
    Retorna el resultado del requerimiento 3:
    Promedios por `cpu_brand` y `cpu_tier`.
    Parámetros:
    - cpu_brand: str
    - cpu_tier: int
    Retorna:
    (exec_time_ms, total_matches, details_dict)
    donde details_dict contiene: count, avg_price, avg_ram, avg_vram,
    avg_threads, most_freq_gpu, most_freq_year
    """
    start_time = get_time()

    total = al.size(catalog["computers"])
    matches = 0
    sum_price = 0.0
    sum_ram = 0
    sum_vram = 0
    sum_threads = 0

    gpu_counts = {}
    year_counts = {}

    # Iterar sobre la lista (1-based indices)
    for i in range(1, total + 1):
        comp = al.get_element(catalog["computers"], i)
        # Comparar marca de CPU (case-insensitive) y tier (int)
        if comp.get('cpu_brand') and comp.get('cpu_tier') is not None:
            try:
                if comp['cpu_brand'].strip().lower() == cpu_brand.strip().lower() and int(comp['cpu_tier']) == int(cpu_tier):
                    matches += 1
                    price = comp.get('price', 0.0) or 0.0
                    ram = comp.get('ram_gb', 0) or 0
                    vram = comp.get('vram_gb', 0) or 0
                    threads = comp.get('cpu_threads', 0) or 0

                    sum_price += float(price)
                    sum_ram += int(ram)
                    sum_vram += int(vram)
                    sum_threads += int(threads)

                    gpu = comp.get('gpu_brand') or None
                    year = comp.get('release_year') or None
                    if gpu:
                        gpu_counts[gpu] = gpu_counts.get(gpu, 0) + 1
                    if year:
                        year_counts[year] = year_counts.get(year, 0) + 1
            except Exception:
                # Ignorar filas con datos inconsistentes
                continue

    # Calcular promedios
    if matches > 0:
        avg_price = sum_price / matches
        avg_ram = sum_ram / matches
        avg_vram = sum_vram / matches
        avg_threads = sum_threads / matches
        # GPU más frecuente
        most_freq_gpu = max(gpu_counts.items(), key=lambda x: x[1])[0] if gpu_counts else None
        most_freq_year = max(year_counts.items(), key=lambda x: x[1])[0] if year_counts else None
    else:
        avg_price = 0.0
        avg_ram = 0.0
        avg_vram = 0.0
        avg_threads = 0.0
        most_freq_gpu = None
        most_freq_year = None

    end_time = get_time()
    exec_time = delta_time(start_time, end_time)

    details = {
        'count': matches,
        'avg_price': avg_price,
        'avg_ram': avg_ram,
        'avg_vram': avg_vram,
        'avg_threads': avg_threads,
        'most_freq_gpu': most_freq_gpu,
        'most_freq_year': most_freq_year
    }

    return exec_time, matches, details
    

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
