import pandas as pd
file_path = r"C:\Users\usept\Documents\Perkodingan Duniawi\Semester 2\Pemrograman Dasar\Sesi_12_Tugas\data_penjualan.xlsx"
df = pd.read_excel(file_path)

df["Total Harga"] = df["Jumlah"] * df["Harga Satuan"]

sorted_df = df.sort_values(by="Total Harga", ascending=False)
sorted_df.to_excel("data_penjualan_terurut.xlsx", index=False)

print(df.head())