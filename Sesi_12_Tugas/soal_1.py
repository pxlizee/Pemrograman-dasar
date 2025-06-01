import pandas as pd

file_path = r"C:\Users\usept\Documents\Perkodingan Duniawi\Semester 2\Pemrograman Dasar\Sesi_12_Tugas\data_penjualan.xlsx"
data = pd.read_excel(file_path)
'''tampilkan 5 baris pertama dari data'''
print(data.head())
# Tampilkan data
