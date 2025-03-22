from datetime import datetime
from tabulate import tabulate

data = [
    {"nama": "Nugraha", "tanggal_lahir": "1989-09-13"},
    {"nama": "John", "tanggal_lahir": "1990-01-01"},
    {"nama": "Jane", "tanggal_lahir": "1992-02-02"},
    {"nama": "Doe", "tanggal_lahir": "1994-03-03"}
]

tahun_sekarang = datetime.now().year

tabel_data = []
for i, orang in enumerate(data, 1):
    tahun_lahir = int(orang["tanggal_lahir"].split("-")[0])
    umur = tahun_sekarang - tahun_lahir
    tabel_data.append([i, orang["nama"], umur])
    
headers = ["No", "Nama", "Umur"]
print(tabulate(tabel_data, headers=headers, tablefmt="grid"))