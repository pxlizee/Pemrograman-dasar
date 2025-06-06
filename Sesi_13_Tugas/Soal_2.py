import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('Sesi_13_Tugas/Data_Penduduk.xlsx')
pendidikan_gender = df.groupby(['Pendidikan_Terakhir', 'Jenis_Kelamin']).size().unstack()

pendidikan_gender.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title("perbandingan pendidikan terakhir berdasarkan jenis kelamin")
plt.xlabel("Pendidikan Terakhir")
plt.ylabel("Jumlah Penduduk")
plt.xticks(rotation=45)
plt.legend(title='Jenis Kelamin')
plt.tight_layout()
plt.show()