import pandas as pd
file_path = r"C:\Users\usept\Documents\Perkodingan Duniawi\Semester 2\Pemrograman Dasar\Sesi_12_Tugas\data_penjualan.xlsx"
df = pd.read_excel(file_path)

df["Total Harga"] = df["Jumlah"] * df["Harga Satuan"]

rekap_df = df.groupby("Kategori").agg({"Total Harga": "sum"}).reset_index()
rekap_df.columns = ["Kategori", "Total Pendapatan"]

print (rekap_df)