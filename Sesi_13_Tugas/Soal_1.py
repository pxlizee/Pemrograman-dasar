import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('Sesi_13_Tugas/Data_Penduduk.xlsx')
profesi_counts = df['Profesi'].value_counts()

plt.figure(figsize=(10, 6))
plt.pie(profesi_counts, labels=profesi_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Persentase Profesi Penduduk')
plt.axis('equal')  # Equal aspect ratio ensures that pie chart is a circle.
plt.show()
