import pandas as pd
file_path = r"C:\Users\usept\Documents\Perkodingan Duniawi\Semester 2\Pemrograman Dasar\Sesi_12_Tugas\data_penjualan.xlsx"
df = pd.read_excel(file_path)

df["Total Harga"] = df["Jumlah"] * df["Harga Satuan"]

elektronik_df = df[df["Kategori"] == "Elektronik"]

elektronik_df.to_excel("elektronik.xlsx", index=False)

print(df.head())