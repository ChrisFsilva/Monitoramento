import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Caminho para o arquivo CSV
csv_file = 'C:/Users/evandro/Desktop/Programação/GDA/logs/ping_data.csv'

# Função para ler dados do CSV usando Pandas
def read_csv_data(file_path):
    df = pd.read_csv(file_path)
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    return df

# Função para atualizar o gráfico
def update(frame):
    df = read_csv_data(csv_file)
    ax.clear()
    for ip in df['IP'].unique():
        ip_data = df[df['IP'] == ip]
        ax.plot(ip_data['Timestamp'], ip_data['Latency'], marker='o', label=ip)
    ax.set_xlabel('Tempo')
    ax.set_ylabel('Latência (ms)')
    ax.set_title('Gráfico de Latência de Ping')
    ax.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()

# Configuração inicial do gráfico
fig, ax = plt.subplots()
ani = FuncAnimation(fig, update, interval=300000)  # Atualiza a cada 5 minutos (300000 ms)
plt.show()