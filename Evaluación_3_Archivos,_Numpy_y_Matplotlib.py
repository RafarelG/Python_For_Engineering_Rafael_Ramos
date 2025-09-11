#Evaluación 3 Python aplicado a la Ingeniería 202520 Docente: Miguel Ortiz

#Estudiante: Rafael Gustavo Ramos Noriega

#email: rafael.ramosn@upb.edu.co

#Fecha: 9/10/2025
import numpy as np
import matplotlib.pyplot as plt

#Paso 1
data = np.genfromtxt('C:/Users/Rafa/Desktop/Octavo semestre/Python/Python_engineering/GHI_Temp_Daily_Hourly_2024.csv', skip_header=True, delimiter=';')

#Paso 2
print(data.shape)
print(data.shape[0])
print(data.shape[1])

#Pregunta: ¿Cuántas filas y columnas tiene tu archivo? ¿Qué representa cada fila?
#Respuesta:
#El archivo tiene 8785 filas y 6 columnas.
#Cada fila representa una medición horaria de datos como GHI (Irradiancia Horizontal Global) y Temperatura.

#Paso 3.1
year = 2024
month = 1
day = 1

#Paso 3.2
filtered_data = data[(data[:, 0] == year) & (data[:, 1] == month) & (data[:, 2] == day)]

#Paso 4.1
print(filtered_data)
#Paso 4.2
print(len(filtered_data))
#Paso 4.3
print(f"{day}/{month}/{year}")
# Pregunta: ¿Cuántos registros encontraste para esa fecha? ¿Te parece lógico ese número?
# Respuesta: Para esa fecha se encontraron 24 registros, lo cual me parece lógico puesto que el archivo contiene
# mediciones por hora y un día completo tiene 24 horas.

#Paso 5.1, 8 y 9
def filter_data_by_date(filepath, year, month, day):
    #Paso 8.1
    try:
        #Paso 5.2
        data = np.genfromtxt(filepath, skip_header=True, delimiter=';')
        #Paso 9.1
        print(f"\nSe cargaron {data.shape[0]} registros del archivo '{filepath}'.")

        filtered_data = data[(data[:, 0] == year) & (data[:, 1] == month) & (data[:, 2] == day)]
        
        #Paso 5.3
        if len(filtered_data) == 0:
            print(f"No se encontraron datos para la fecha {day}/{month}/{year}.")
            return None

        #Paso 9.2
        avg_temp = np.mean(filtered_data[:, 4])
        max_ghi = np.max(filtered_data[:, 5])
        print(f"Análisis para {day}/{month}/{year}:")
        print(f"  - Temperatura promedio: {avg_temp:.2f}°C")
        print(f"  - GHI máximo: {max_ghi:.2f} W/m2")

        return filtered_data
        
    #Paso 8.2
    except FileNotFoundError:
        #Paso 8.2.1
        print(f"Error: No se encontró el archivo en la ruta '{filepath}'.")
    except IndexError:
        #Paso 8.2.2
        print("Error: El archivo no tiene el formato esperado (columnas incorrectas).")
    except Exception as e:
        #Paso 8.2.3
        print(f"Ocurrió un error inesperado: {e}")
    
    return None

# Paso 7
def energy_calculations(filepath, year, month, day, n_panels, panel_area, panel_efficiency, inverter_efficiency, stc_temp=25, temp_coeff=-0.004):
    
    print(f"\n--- Iniciando cálculo de energía para {day}/{month}/{year} ---")
    
    # Invoca la función de filtrado
    ghi_temp_data = filter_data_by_date(filepath, year, month, day)
    
    if ghi_temp_data is None:
        print("Cálculo de energía cancelado debido a falta de datos.")
        return

    # Extraer columnas
    hours = ghi_temp_data[:, 3]
    temp = ghi_temp_data[:, 4]
    ghi = ghi_temp_data[:, 5]
    
    # Calcular área total
    total_area = panel_area * n_panels
    
    # Calcular corrección por temperatura
    temp_correction = 1 + temp_coeff * (temp - stc_temp)
    
    # Calcular potencia DC y AC
    dc_power = ghi * total_area * panel_efficiency * temp_correction
    ac_power = dc_power * inverter_efficiency
    
    # Calcular energía
    hourly_energy_kwh = ac_power / 1000
    total_energy_kwh = np.sum(hourly_energy_kwh)
    
    # Imprimir resultados
    print(f"Registros cargados: {len(hours)}")
    print(f"Potencia DC promedio: {np.mean(dc_power):.2f} W")
    print(f"Potencia AC promedio: {np.mean(ac_power):.2f} W")
    print(f"Energía total generada: {total_energy_kwh:.2f} kWh")

    # Crear archivo de resultados
    energy_data_filename = f"energy_data_{year}_{month:02d}_{day:02d}.csv"
    with open(energy_data_filename, 'w') as datafile:
        datafile.write("Hour,Power_DC,Power_AC,Energy_kWh\n")
        for i in range(len(hours)):
            line = f"{int(hours[i])},{dc_power[i]:.2f},{ac_power[i]:.2f},{hourly_energy_kwh[i]:.2f}\n"
            datafile.write(line)
    print(f"El archivo {energy_data_filename} fue creado exitosamente!")

    #Bonus
    plt.figure(figsize=(10, 6))
    plt.bar(hours, hourly_energy_kwh, color='skyblue')
    plt.xlabel("Hora del día")
    plt.ylabel("Energía Generada (kWh)")
    plt.title(f"Producción de Energía Horaria - {day}/{month}/{year}")
    plt.xticks(np.arange(min(hours), max(hours)+1, 1.0))
    plt.grid(axis='y', linestyle='--')
    graph_filename = f"energy_graph_{year}_{month:02d}_{day:02d}.png"
    plt.savefig(graph_filename)
    print(f"Gráfica guardada como '{graph_filename}'")
    # plt.show() # Descomenta si quieres que la gráfica se muestre en una ventana

#Paso 6.1
filename = f"filtered_data_{year}_{month:02d}_{day:02d}.csv"
#Paso 6.2 
with open(filename, 'w') as f:
    #Paso 6.3.1
    f.write("Year,Month,Day,Hour,Temperature,GHI\n")
    #Paso 6.3.2
    for row in filtered_data:
        #Paso 6.3.3
        line = f"{int(row[0])},{int(row[1])},{int(row[2])},{int(row[3])},{row[4]:.2f},{row[5]:.2f}\n"
        f.write(line)
#Paso 6.4
print(f"Archivo '{filename}' creado exitosamente.")

# Paso 8: Probar la función
if __name__ == "__main__":
    filepath_csv = 'C:/Users/Rafa/Desktop/Octavo semestre/Python/Python_engineering/GHI_Temp_Daily_Hourly_2024.csv'
    
    # Test como en la imagen
    energy_calculations(
        filepath=filepath_csv,
        year=2024, month=12, day=11,
        n_panels=10,
        panel_area=1.65,
        panel_efficiency=0.2,
        inverter_efficiency=0.95
    )
