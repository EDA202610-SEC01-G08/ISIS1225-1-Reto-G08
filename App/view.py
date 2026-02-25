import sys
import App.logic as logic

def new_logic():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función de la lógica donde se crean las estructuras de datos
    control = logic.new_logic()
    return control

def print_menu():
    print("Bienvenido")
    print("0- Cargar información")
    print("1- Ejecutar Requerimiento 1")
    print("2- Ejecutar Requerimiento 2")
    print("3- Ejecutar Requerimiento 3")
    print("4- Ejecutar Requerimiento 4")
    print("5- Ejecutar Requerimiento 5")
    print("6- Ejecutar Requerimiento 6")
    print("7- Salir")

def load_data(control):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    filename = "computer_prices_medium.csv"
    load_time, total_computers, min_computer, max_computer, first_five, last_five = logic.load_data(control, filename)
    print(f"Tiempo de carga: {load_time} ms")
    print(f"Total de computadores: {total_computers}")
    print(f"Primeros 5 computadores cargados:") 
    for computer in first_five:
        print(f"{computer['brand']} {computer['model']} {computer['release_year']} {computer['cpu_model']} {computer['gpu_model']}- ${computer['price']}")
    
    print(f"Últimos 5 computadores cargados:")
    for computer in last_five:
        print(f"{computer['brand']} {computer['model']} {computer['release_year']} {computer['cpu_model']} {computer['gpu_model']}- ${computer['price']}")

    print(f"Computador más barato: {min_computer['brand']} {min_computer['model']} con precio de ${min_computer['price']}")
    print(f"Computador más caro: {max_computer['brand']} {max_computer['model']} con precio de ${max_computer['price']}")


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    brand = input("Ingrese la marca del computador").strip()
    
    (exec_time,total_comp,
     avg_price,min_price,max_price,
     avg_ram,min_ram,max_ram,
     avg_vram,min_vram,max_vram,
     avg_cores,min_cores,max_cores,
     avg_year,min_year,max_year,
     max_price_comp,min_price_comp)=logic.req_1(control, brand)
    
    print("\n=== Requerimiento 1:Estadisticas por marca ===")
    print(f"Marca consultada: {brand}")
    print(f"Tiempo de ejecución: {exec_time} ms")
    print(f"Total de computadores de la marca: {total_comp}\n")
    
    if total_comp ==0:
        print("No se encontraron computadores de dicha marca.")
        return
    print("precio")
    print(f"Promedio: {avg_price}")
    print(f"minimo: {min_price}")
    print(f"maximo: {max_price}")
    
    print("Ram")
    print(f"Promedio: {avg_ram}")
    print(f"minimo: {min_ram}")
    print(f"maximo: {max_ram}")
    
    print("Vram")
    print(f"Promedio: {avg_vram}")
    print(f"minimo: {min_vram}")
    print(f"maximo: {max_vram}")
    
    print("Cores")
    print(f"Promedio: {avg_cores}")
    print(f"minimo: {min_cores}")
    print(f"maximo: {max_cores}")
    
    print("año de lanzamiento")
    print(f"Promedio: {avg_year}")
    print(f"minimo: {min_year}")
    print(f"maximo: {max_year}")
    
    if max_price_comp is not None:
        print("Computador más caro ")
        print(f"Modelo: {max_price_comp.get('model')}")
        print(f"Precio: {max_price_comp.get('price')}")
        print(f"Peso: {max_price_comp.get('weight_kg')}")
    
    if min_price_comp is not None:
        print("computador más barato ")
        print(f"Modelo: {min_price_comp.get('model')}")
        print(f"Precio: {min_price_comp.get('price')}")
        print(f"Peso: {min_price_comp.get('weight_kg')}")
        
    
  


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    try:
        price_min = float(input("Ingrese el precio mínimo: "))
        price_max = float(input("Ingrese el precio máximo: "))
    except ValueError:
        print("Entrada inválida. Debe ingresar números.")
        return

    count, avg_ram, avg_vram, avg_price, min_comp, max_comp, mas_moderno, tiempo_ejecucion = logic.req_2(control, price_min, price_max)

    print("--- Resultado Requerimiento 2 ---")
    print(f"Tiempo de ejecución (ms): {tiempo_ejecucion}")
    print(f"Total computadores en rango: {count}")
    print(f"Promedio RAM (GB): {avg_ram}")
    print(f"Promedio VRAM (GB): {avg_vram}")
    print(f"Promedio precio: {avg_price}")

    if count == 0 or min_comp is None:
        print("\nNo se encontraron computadores en ese rango.")
        return

    print("\nComputador más barato en el rango:")
    print(
        min_comp["device_type"],
        min_comp["brand"],
        min_comp["model"],
        min_comp["release_year"],
        min_comp["os"],
        min_comp["price"]
    )

    print("\nComputador más caro en el rango:")
    print(
        max_comp["device_type"],
        max_comp["brand"],
        max_comp["model"],
        max_comp["release_year"],
        max_comp["os"],
        max_comp["price"]
    )

    print("\nComputador más moderno en el rango (desempate por precio):")
    print(
        mas_moderno["device_type"],
        mas_moderno["brand"],
        mas_moderno["model"],
        mas_moderno["release_year"],
        mas_moderno["os"],
        mas_moderno["price"]
    )


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    cpu_brand = input('Ingrese la marca del CPU (ej. Intel, AMD):\n')
    cpu_tier_str = input('Ingrese el CPU tier (numero entero):\n')
    try:
        cpu_tier = int(cpu_tier_str)
    except ValueError:
        print('CPU tier inválido. Debe ser un entero.')
        return

    exec_time, total_matches, details = logic.req_3(control, cpu_brand, cpu_tier)

    print(f"Tiempo de ejecución: {exec_time} ms")
    print(f"Total de computadores que cumplieron el filtro: {total_matches}")
    if details['count'] > 0:
        print(f"Cantidad: {details['count']}")
        print(f"Promedio precio: ${details['avg_price']:.2f}")
        print(f"Promedio RAM (GB): {details['avg_ram']:.2f}")
        print(f"Promedio VRAM (GB): {details['avg_vram']:.2f}")
        print(f"Promedio hilos CPU: {details['avg_threads']:.2f}")
        print(f"GPU más frecuente: {details['most_freq_gpu']}")
        print(f"Año de lanzamiento más frecuente: {details['most_freq_year']}")
    else:
        print('No se encontraron computadores que cumplan el filtro.')


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    cpu_brand = input("Ingrese la marca del CPU").strip()
    gpu_model = input("Ingrese el modelo del GPU").strip()
    
    (exec_time,total_m,avg_price,avg_vram,avg_ram,avg_boost,top1,top2,filtered) = logic.req_4(control, cpu_brand, gpu_model)
    print("\n=== Requerimiento 4:CPU brand y GPU Model ===")
    print(f"CPU brand consultada: {cpu_brand}")
    print(f"GPU model consultada: {gpu_model}")
    print(f"Tiempo de ejecución: {exec_time} ms")
    print(f"Total de computadores que cumplen el filtro: {total_m}")
    
    if total_m==0:
        print("No se encontraron computadores que cumplan el filtro.")
        return
    print(f"Precio promedio: {avg_price}")
    print(f"VRAM promedio: {avg_vram}")
    print(f"RAM promedio: {avg_ram}")
    print(f"CPU boost promedio: {avg_boost}")
    
    
    print("Top 2 mas costosos(desempate:menor peso)")
    if top1 is not None:
        print("computador mas costoso")
        print(f"Modelo: {top1.get('model')}")
        print(f"Marca: {top1.get('brand')}")
        print(f"Año: {top1.get('release_year')}")
        print(f"CPU: {top1.get('cpu_model')}")
        print(f"Precio: {top1.get('price')}")
        print(f"Peso: {top1.get('weight_kg')}")
        
    if top2 is not None:
        print("computador segundo mas costoso")
        print(f"Modelo: {top2.get('model')}")
        print(f"Marca: {top2.get('brand')}")
        print(f"Año: {top2.get('release_year')}")
        print(f"CPU: {top2.get('cpu_model')}")
        print(f"Precio: {top2.get('price')}")
        print(f"Peso: {top2.get('weight_kg')}")
  


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5

    filtro = input("Ingrese filtro (BARATO o CARO): ").strip().upper()
    resolucion = input("Ingrese resolución (ej. 1920x1080): ").strip()
    year_min = int(input("Ingrese año mínimo: "))
    year_max = int(input("Ingrese año máximo: "))

    (filtro, count, avg_price, avg_display, avg_gpu_tier, mejor, tiempo_ejecucucion) = logic.req_5(control, filtro, resolucion, year_min, year_max)

    print("\n========== RESULTADOS REQ 5 ==========")
    print(f"Filtro aplicado: {filtro}")
    print(f"Tiempo de ejecución (ms): {tiempo_ejecucucion}")
    print(f"Total computadores que cumplen filtro: {count}")

    if count == 0:
        print("No se encontraron computadores con esos criterios.")
        return

    print("\n--- Computador seleccionado ---")
    print(f"Precio: {mejor['price']}")
    print(f"Tamaño pantalla: {mejor['display_size_in']}")
    print(f"GPU Tier: {mejor['gpu_tier']}")
    print(f"Tipo de display: {mejor['display_type']}")
    print(f"Año: {mejor['release_year']}")
    print(f"Peso (kg): {mejor['weight_kg']}")

    print("\n--- Promedios de los que cumplen el filtro ---")
    print(f"Precio promedio: {avg_price}")
    print(f"Tamaño promedio pantalla: {avg_display}")
    print(f"GPU Tier promedio: {avg_gpu_tier}")


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    year_init_str = input('Ingrese el año inicial (ej. 2015):\n')
    year_end_str = input('Ingrese el año final (ej. 2020):\n')
    try:
        year_init = int(year_init_str)
        year_end = int(year_end_str)
    except ValueError:
        print('Años inválidos. Deben ser enteros.')
        return

    exec_time, total_matches, result = logic.req_6(control, year_init, year_end)

    print(f"Tiempo de ejecución: {exec_time} ms")
    print(f"Total de computadores en el rango {year_init}-{year_end}: {total_matches}")

    most_used = result.get('most_used') if result else None
    most_revenue = result.get('most_revenue') if result else None

    if most_used and most_used.get('os'):
        print(f"OS más usado: {most_used['os']} - registros: {most_used['count']} - recaudo: ${most_used['revenue']:.2f}")
    else:
        print('OS más usado: Ninguno')

    if most_revenue and most_revenue.get('os'):
        print(f"OS que más recauda: {most_revenue['os']} - registros: {most_revenue['count']} - recaudo: ${most_revenue['revenue']:.2f}")
    else:
        print('OS que más recauda: Ninguno')

    per_os = result.get('per_os') if result else {}
    if per_os:
        print('\nDetalle por sistema operativo:')
        for os_name, d in per_os.items():
            print(f"\n- {os_name}:")
            print(f"  Cantidad: {d.get('count')}")
            print(f"  Precio promedio: ${d.get('avg_price'):.2f}")
            print(f"  Peso promedio (kg): {d.get('avg_weight'):.2f}")
            me = d.get('most_expensive')
            mc = d.get('most_cheap')
            if me:
                print(f"  Computador más costoso: {me.get('brand')} {me.get('model')} - Año: {me.get('year')} - CPU: {me.get('cpu')} - GPU: {me.get('gpu')} - Precio: ${me.get('price')}")
            if mc:
                print(f"  Computador más barato: {mc.get('brand')} {mc.get('model')} - Año: {mc.get('year')} - CPU: {mc.get('cpu')} - GPU: {mc.get('gpu')} - Precio: ${mc.get('price')}")
    else:
        print('No hay sistemas operativos en el rango de años especificado.')

# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 0:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
        elif int(inputs) == 1:
            print_req_1(control)

        elif int(inputs) == 2:
            print_req_2(control)

        elif int(inputs) == 3:
            print_req_3(control)

        elif int(inputs) == 4:
            print_req_4(control)

        elif int(inputs) == 5:
            print_req_5(control)

        elif int(inputs) == 6:
            print_req_6(control)

        elif int(inputs) == 7:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
