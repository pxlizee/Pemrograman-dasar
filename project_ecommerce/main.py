from ecommerce.pricing import hitung_diskon, hitung_pajak, hitung_total
from ecommerce.order import generate_order_id

def main():
    nama_pelanggan = input("Masukkan nama pelanggan: ")
    nama_produk = input("Masukkan nama produk: ")
    harga_asli = float(input("Masukkan harga asli produk: "))
    persentase_diskon = float(input("Masukkan persentase diskon: "))
    persentase_pajak = float(input("Masukkan persentase pajak: "))
    
    
    diskon = harga_asli * (persentase_diskon / 100)
    total = hitung_total(harga_asli, persentase_diskon, persentase_pajak)
    order_id = generate_order_id()
    
    print("="*40)
    print("Rincian Pesanan")
    print("="*40)
    print(f"{'ID Pesanan':20} {order_id}")
    print(f"{'Nama Pelanggan':20} {nama_pelanggan}")
    print(f"{'Nama Produk':20} {nama_produk}")
    print(f"{'Harga Asli':20} Rp {harga_asli:,.2f}")
    print(f"{'Diskon':20} Rp {diskon:,.2f}")
    print(f"{'pajak':20} Rp {hitung_pajak(harga_asli - diskon, persentase_pajak):,.2f}")
    print("-"*40)
    print(f"{'Total Belanja':20} Rp {total:,.2f}")
    print("="*40)
    print("Terima kasih telah berbelanja!")
    print("="*40)
if __name__ == "__main__":
    main()