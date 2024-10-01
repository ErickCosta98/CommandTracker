import plotext as plt

def generate_graph(cpu_usage, memory_usage, execution_time):
    time_points = [i * 0.1 for i in range(len(cpu_usage))]  #intervalo de 0.1s

    # Gráfico de uso de CPU
    plt.clear_data()
    plt.plot(time_points, cpu_usage, label='CPU Usage (%)', color='blue')
    plt.title('CPU Usage Over Time')
    plt.xlabel('Time (s)')
    plt.ylabel('CPU Usage (%)')
    plt.grid(True)
    plt.show()  # Muestra el gráfico en la consola

    # Gráfico de uso de memoria
    plt.clear_data()  # Limpiar el gráfico anterior
    plt.plot(time_points, memory_usage, label='Memory Usage (MB)', color='green')
    plt.title('Memory Usage Over Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Memory Usage (MB)')
    plt.grid(True)
    plt.show()  # Muestra el gráfico en la consola

