import matplotlib.pyplot as plt
import numpy as np
import random
from datetime import datetime, timedelta


# 1) Gráfico de líneas: avisos por día
dias = [(datetime.now() - timedelta(days=i)).strftime("%d/%m/%Y") for i in range(6, -1, -1)]
avisos = np.random.randint(1, 10, size=7)

print(avisos)#

plt.figure(figsize=(8,4.5))
plt.plot(dias, avisos, marker="o", linestyle="-", color="skyblue", linewidth=2)
plt.title("Avisos por día")
plt.xlabel("Días")
plt.ylabel("Cantidad de avisos")
plt.grid(alpha=0.3)
plt.ylim(0, avisos.max() +1)
plt.yticks(np.arange(0, avisos.max() + 1, 1))
plt.tight_layout()
plt.show()

# 2) Gráfico de torta: gatos vs perros
labels = ["Gatos", "Perros"]
total_avisos = avisos.sum()
avisos_perros = int(total_avisos * random.uniform(0.2, 0.8))
avisos_gatos = total_avisos - avisos_perros
sizes = [avisos_perros, avisos_gatos]

print(total_avisos)
print(sizes)

colors = ["#5cc8ff", "#ff9f68"]
plt.figure(figsize=(6,6))
plt.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=90)
plt.title("Total de avisos por tipo de mascota")
plt.tight_layout()
plt.show()

# 3) Gráfico de barras: por mes (gatos vs perros)
meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
# Generar un arreglo de 12 elementos aleatorios que sumen avisos_perros
perros = np.random.multinomial(avisos_perros, np.ones(12)/12)
gatos = np.random.multinomial(avisos_gatos, np.ones(12)/12)

print(perros)
print(gatos)

x = np.arange(len(meses))
width = 0.35

plt.figure(figsize=(8,4.5))
plt.bar(x - width/2, gatos, width, label="Gatos", color="#5cc8ff")
plt.bar(x + width/2, perros, width, label="Perros", color="#ff9f68")
plt.xticks(x, meses)
plt.ylabel("Cantidad de avisos")
plt.yticks(np.arange(0, max(gatos.max(), perros.max()) + 1, 1))
plt.ylim(0, max(gatos.max(), perros.max()) + 1)
plt.title("Avisos por mes (gatos vs perros)")
plt.legend()
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()

