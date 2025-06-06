import pandas as pd
import matplotlib.pyplot as plt

def kategori_penghasilan (penghasilan):
    if penghasilan < 2000000:
        return 'Sangat Rendah'
    elif penghasilan < 5000000:
        return 'Rendah'
    elif penghasilan < 10000000:
        return 'Menengah'
    else:
        return 'Tinggi'

df = pd.read_excel('Sesi_13_Tugas/Data_Penduduk.xlsx')
df['Kategori_Penghasilan'] = df['Penghasilan_Per_Bulan'].apply(kategori_penghasilan)
kategori_counts = df['Kategori_Penghasilan'].value_counts()

plt.figure(figsize=(10, 6))
plt.pie(kategori_counts, labels=kategori_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribusi Penghasilan Warga Desa Cibodas')
plt.axis('equal')  # Equal aspect ratio ensures that pie chart is a circle.
plt.show()
