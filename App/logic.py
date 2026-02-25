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


def req_2(catalog, price_min, price_max):
    """
    Retorna el resultado del requerimiento 2
    """

    start_time = get_time()

    count = 0
    sum_ram = 0
    sum_vram = 0
    sum_price = 0
    count_ram = 0
    count_vram = 0  

    min_comp = None
    max_comp = None
    mas_moderno = None

    size = al.size(catalog["computers"])

    for i in range(1, size + 1):
        computer = al.get_element(catalog["computers"], i)

        if price_min <= computer["price"] <= price_max:

            count += 1

            if computer["ram_gb"] is not None:
                sum_ram += computer["ram_gb"]
                count_ram += 1
            if computer["vram_gb"] is not None:
                sum_vram += computer["vram_gb"]
                count_vram += 1
            
            sum_price += computer["price"]
            count += 1

            # mínimo precio
            if min_comp is None or computer["price"] < min_comp["price"]:
                min_comp = computer

            # máximo precio
            if max_comp is None or computer["price"] > max_comp["price"]:
                max_comp = computer

            # más moderno (con desempate por precio)
            if mas_moderno is None:
                mas_moderno = computer
            else:
                current_year = computer["release_year"]
                best_year = mas_moderno["release_year"]

                if current_year is not None:
                    if best_year is None:
                        mas_moderno = computer
                    elif current_year > best_year:
                        mas_moderno = computer
                    elif current_year == best_year and computer["price"] > mas_moderno["price"]:
                        mas_moderno = computer

    if count > 0:
        avg_ram = sum_ram / count_ram if count_ram > 0 else 0
        avg_vram = sum_vram / count_vram if count_vram > 0 else 0
        avg_price = sum_price / count if count > 0 else 0
    else:
        avg_ram = 0
        avg_vram = 0
        avg_price = 0

    end_time = get_time()
    tiempo_ejecucion = delta_time(start_time, end_time)

    return count, avg_ram, avg_vram, avg_price, min_comp, max_comp, mas_moderno, tiempo_ejecucion  


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


def req_5(catalog, filtro, resolucion, year_min, year_max):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    start_time = get_time()

    # LinkedList temporal
    filtered_list = ll.new_list()

    count = 0
    sum_price = 0
    sum_display = 0
    sum_gpu_tier = 0

    mejor = None

    size = al.size(catalog["computers"])

    for i in range(1, size + 1):

        computer = al.get_element(catalog["computers"], i)

        # FILTRO
        if (computer["resolution"] == resolucion and
            year_min <= computer["release_year"] <= year_max):

            # Insertar en LinkedList
            ll.add_last(filtered_list, computer)

            count += 1
            sum_price += computer["price"]
            sum_display += computer["display_size_in"]
            sum_gpu_tier += computer["gpu_tier"]

            # SELECCIÓN DEL MEJOR
            if mejor is None:
                mejor = computer

            else:

                if filtro == "BARATO":

                    if computer["price"] < mejor["price"]:
                        mejor = computer

                    elif computer["price"] == mejor["price"]:
                        if computer["weight_kg"] < mejor["weight_kg"]:
                            mejor = computer

                elif filtro == "CARO":

                    if computer["price"] > mejor["price"]:
                        mejor = computer

                    elif computer["price"] == mejor["price"]:
                        if computer["weight_kg"] < mejor["weight_kg"]:
                            mejor = computer

    # PROMEDIOS
    if count > 0:
        avg_price = sum_price / count
        avg_display = sum_display / count
        avg_gpu_tier = sum_gpu_tier / count
    else:
        avg_price = 0
        avg_display = 0
        avg_gpu_tier = 0

    end_time = get_time()
    tiempo_ejecucion = delta_time(start_time, end_time)

    return (filtro, count, avg_price, avg_display, avg_gpu_tier, mejor, tiempo_ejecucion)

def req_6(catalog, year_init, year_end):
    """
    Requerimiento 6: Identificar OS más usado y OS que más recauda en un rango de años.
    Usa la estructura `single_linked_list` para procesar los datos (se copia desde el array_list).
    Parámetros:
    - year_init: int (año inicial inclusive)
    - year_end: int (año final inclusive)

    Retorna:
    (exec_time_ms, total_matches, result_dict)

    result_dict contiene:
    - most_used: {'os', 'count', 'revenue'}
    - most_revenue: {'os', 'count', 'revenue'}
    - per_os: { os_name: { 'avg_price', 'avg_weight', 'most_expensive', 'most_cheap', 'count', 'total_revenue' } }
    """
    start_time = get_time()

    # Crear una lista enlazada y copiar datos desde el array_list
    computers_ll = ll.new_list()
    total_array = al.size(catalog["computers"])
    for i in range(1, total_array + 1):
        comp = al.get_element(catalog["computers"], i)
        ll.add_last(computers_ll, comp)

    total_matches = 0
    os_stats = {}

    size_ll = ll.size(computers_ll)
    for pos in range(0, size_ll):
        try:
            comp = ll.get_element(computers_ll, pos)
        except Exception:
            continue
        year = comp.get('release_year')
        if year is None:
            continue
        try:
            if int(year) < int(year_init) or int(year) > int(year_end):
                continue
        except Exception:
            continue

        total_matches += 1
        os_name = comp.get('os') or 'Unknown'
        price = float(comp.get('price') or 0.0)
        weight = float(comp.get('weight_kg') or 0.0)

        if os_name not in os_stats:
            os_stats[os_name] = {
                'count': 0,
                'total_revenue': 0.0,
                'sum_price': 0.0,
                'sum_weight': 0.0,
                'max_comp': comp,
                'min_comp': comp
            }

        s = os_stats[os_name]
        s['count'] += 1
        s['total_revenue'] += price
        s['sum_price'] += price
        s['sum_weight'] += weight

        # actualizar max y min por precio
        try:
            if price > float(s['max_comp'].get('price') or 0.0):
                s['max_comp'] = comp
        except Exception:
            s['max_comp'] = comp
        try:
            if price < float(s['min_comp'].get('price') or float('inf')):
                s['min_comp'] = comp
        except Exception:
            s['min_comp'] = comp

    # Determinar OS más usado y OS que más recauda
    if os_stats:
        most_used_name, most_used_stats = max(os_stats.items(), key=lambda x: x[1]['count'])
        most_revenue_name, most_revenue_stats = max(os_stats.items(), key=lambda x: x[1]['total_revenue'])
    else:
        most_used_name = None
        most_used_stats = None
        most_revenue_name = None
        most_revenue_stats = None

    # Preparar detalle por OS
    per_os = {}
    for os_name, s in os_stats.items():
        cnt = s['count']
        avg_price = s['sum_price'] / cnt if cnt > 0 else 0.0
        avg_weight = s['sum_weight'] / cnt if cnt > 0 else 0.0

        def summarize_comp(c):
            if not c:
                return {'model': None, 'brand': None, 'year': None, 'cpu': None, 'gpu': None, 'price': None}
            return {
                'model': c.get('model'),
                'brand': c.get('brand'),
                'year': c.get('release_year'),
                'cpu': c.get('cpu_model'),
                'gpu': c.get('gpu_model'),
                'price': c.get('price')
            }

        per_os[os_name] = {
            'avg_price': avg_price,
            'avg_weight': avg_weight,
            'most_expensive': summarize_comp(s.get('max_comp')),
            'most_cheap': summarize_comp(s.get('min_comp')),
            'count': s['count'],
            'total_revenue': s['total_revenue']
        }

    result = {
        'most_used': {
            'os': most_used_name,
            'count': most_used_stats['count'] if most_used_stats else 0,
            'revenue': most_used_stats['total_revenue'] if most_used_stats else 0.0
        },
        'most_revenue': {
            'os': most_revenue_name,
            'count': most_revenue_stats['count'] if most_revenue_stats else 0,
            'revenue': most_revenue_stats['total_revenue'] if most_revenue_stats else 0.0
        },
        'per_os': per_os
    }

    end_time = get_time()
    exec_time = delta_time(start_time, end_time)

    return exec_time, total_matches, result


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
